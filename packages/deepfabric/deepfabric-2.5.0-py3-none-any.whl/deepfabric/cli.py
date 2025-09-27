import os
import sys

from typing import NoReturn

import click
import yaml

from .config import DeepFabricConfig
from .config_manager import apply_cli_overrides, get_final_parameters, load_config
from .dataset_manager import create_dataset, save_dataset
from .exceptions import ConfigurationError
from .format_command import format_cli
from .generator import DataSetGenerator
from .graph import Graph
from .metrics import trace
from .topic_manager import load_or_build_topic_model, save_topic_model
from .tui import get_tui
from .validation import show_validation_success, validate_path_requirements


def handle_error(ctx: click.Context, error: Exception) -> NoReturn:
    """Handle errors in CLI commands."""
    _ = ctx  # Unused but required for click context
    tui = get_tui()

    # Check if this is formatted error from our event handlers
    error_msg = str(error)
    if not error_msg.startswith("Error: "):
        tui.error(f"Error: {error_msg}")
    else:
        tui.error(error_msg)

    sys.exit(1)


@click.group()
@click.version_option()
def cli():
    """DeepFabric CLI - Generate synthetic training data for language models."""
    pass


@cli.command()
@click.argument("config_file", type=click.Path(exists=True), required=False)
@click.option(
    "--dataset-system-prompt", help="System prompt for final dataset (if sys_msg is true)"
)
@click.option("--topic-prompt", help="Starting topic/seed for tree/graph generation")
@click.option("--topic-system-prompt", help="System prompt for tree/graph topic generation")
@click.option("--generation-system-prompt", help="System prompt for dataset content generation")
@click.option("--save-tree", help="Save path for the tree")
@click.option(
    "--load-tree",
    type=click.Path(exists=True),
    help="Path to the JSONL file containing the tree.",
)
@click.option("--save-graph", help="Save path for the graph")
@click.option(
    "--load-graph",
    type=click.Path(exists=True),
    help="Path to the JSON file containing the graph.",
)
@click.option("--dataset-save-as", help="Save path for the dataset")
@click.option("--provider", help="LLM provider (e.g., ollama)")
@click.option("--model", help="Model name (e.g., mistral:latest)")
@click.option("--temperature", type=float, help="Temperature setting")
@click.option("--degree", type=int, help="Degree (branching factor)")
@click.option("--depth", type=int, help="Depth setting")
@click.option("--num-steps", type=int, help="Number of generation steps")
@click.option("--batch-size", type=int, help="Batch size")
@click.option("--base-url", help="Base URL for LLM provider API endpoint")
@click.option(
    "--sys-msg",
    type=bool,
    help="Include system message in dataset (default: true)",
)
@click.option(
    "--mode",
    type=click.Choice(["tree", "graph"]),
    default="tree",
    help="Topic generation mode (default: tree)",
)
@click.option(
    "--debug",
    is_flag=True,
    help="Enable debug mode for detailed error output",
)
def generate(  # noqa: PLR0913
    config_file: str | None,
    dataset_system_prompt: str | None = None,
    topic_prompt: str | None = None,
    topic_system_prompt: str | None = None,
    generation_system_prompt: str | None = None,
    save_tree: str | None = None,
    load_tree: str | None = None,
    save_graph: str | None = None,
    load_graph: str | None = None,
    dataset_save_as: str | None = None,
    provider: str | None = None,
    model: str | None = None,
    temperature: float | None = None,
    degree: int | None = None,
    depth: int | None = None,
    num_steps: int | None = None,
    batch_size: int | None = None,
    base_url: str | None = None,
    sys_msg: bool | None = None,
    mode: str = "tree",
    debug: bool = False,
) -> None:
    """Generate training data from a YAML configuration file or CLI parameters."""
    trace(
        "cli_generate",
        {"mode": mode, "has_config": config_file is not None, "provider": provider, "model": model},
    )

    try:
        if mode == "graph" and save_tree:
            raise ConfigurationError(  # noqa: TRY301
                "Cannot use --save-tree when mode is graph. Use --save-graph to persist graph data.",
            )

        if mode == "tree" and save_graph:
            raise ConfigurationError(  # noqa: TRY301
                "Cannot use --save-graph when mode is tree. Use --save-tree to persist tree data.",
            )

        # Load configuration
        config = load_config(
            config_file=config_file,
            topic_prompt=topic_prompt,
            dataset_system_prompt=dataset_system_prompt,
            generation_system_prompt=generation_system_prompt,
            provider=provider,
            model=model,
            temperature=temperature,
            degree=degree,
            depth=depth,
            num_steps=num_steps,
            batch_size=batch_size,
            save_tree=save_tree,
            save_graph=save_graph,
            dataset_save_as=dataset_save_as,
            sys_msg=sys_msg,
            mode=mode,
        )

        # Apply CLI overrides and get override dictionaries
        tree_overrides, graph_overrides, engine_overrides = apply_cli_overrides(
            config=config,
            dataset_system_prompt=dataset_system_prompt,
            topic_prompt=topic_prompt,
            topic_system_prompt=topic_system_prompt,
            generation_system_prompt=generation_system_prompt,
            provider=provider,
            model=model,
            temperature=temperature,
            degree=degree,
            depth=depth,
            base_url=base_url,
        )

        # Get final parameters
        final_num_steps, final_batch_size, final_depth, final_degree = get_final_parameters(
            config=config,
            num_steps=num_steps,
            batch_size=batch_size,
            depth=depth,
            degree=degree,
        )

        # Validate path requirements
        validate_path_requirements(
            mode=mode,
            depth=final_depth,
            degree=final_degree,
            num_steps=final_num_steps,
            batch_size=final_batch_size,
            loading_existing=bool(load_tree or load_graph),
        )

        # Show validation success
        show_validation_success(
            mode=mode,
            depth=final_depth,
            degree=final_degree,
            num_steps=final_num_steps,
            batch_size=final_batch_size,
            loading_existing=bool(load_tree or load_graph),
        )

        # Load or build topic model
        topic_model = load_or_build_topic_model(
            config=config,
            load_tree=load_tree,
            load_graph=load_graph,
            tree_overrides=tree_overrides,
            graph_overrides=graph_overrides,
            provider=provider,
            model=model,
            base_url=base_url,
            debug=debug,
        )

        # Save topic model if newly created
        if not load_tree and not load_graph:
            save_topic_model(
                topic_model=topic_model,
                config=config,
                save_tree=save_tree,
                save_graph=save_graph,
            )

        # Create data engine
        engine = DataSetGenerator(**config.get_engine_params(**engine_overrides))

        # Create dataset
        dataset = create_dataset(
            engine=engine,
            topic_model=topic_model,
            config=config,
            num_steps=num_steps,
            batch_size=batch_size,
            sys_msg=sys_msg,
            provider=provider,
            model=model,
            engine_overrides=engine_overrides,
            debug=debug,
        )

        # Save dataset
        dataset_config = config.get_dataset_config()
        dataset_save_path = dataset_save_as or dataset_config["save_as"]
        save_dataset(dataset, dataset_save_path, config)

        # Trace metrics
        trace(
            "dataset_generated",
            {"samples": len(dataset.samples) if hasattr(dataset, "samples") else 0},
        )

    except ConfigurationError as e:
        handle_error(click.get_current_context(), e)
    except Exception as e:
        tui = get_tui()
        tui.error(f"Unexpected error: {str(e)}")
        sys.exit(1)


@cli.command()
@click.argument("dataset_file", type=click.Path(exists=True))
@click.option(
    "--repo",
    required=True,
    help="Hugging Face repository (e.g., username/dataset-name)",
)
@click.option(
    "--token",
    help="Hugging Face API token (can also be set via HF_TOKEN env var)",
)
@click.option(
    "--tags",
    multiple=True,
    help="Tags for the dataset (can be specified multiple times)",
)
def upload(
    dataset_file: str,
    repo: str,
    token: str | None = None,
    tags: list[str] | None = None,
) -> None:
    """Upload a dataset to Hugging Face Hub."""
    trace("cli_upload", {"has_tags": len(tags) > 0 if tags else False})

    try:
        # Get token from CLI arg or env var
        token = token or os.getenv("HF_TOKEN")
        if not token:
            handle_error(
                click.get_current_context(),
                ValueError("Hugging Face token not provided. Set via --token or HF_TOKEN env var."),
            )

        # Lazy import to avoid slow startup when not using HF features
        from .hf_hub import HFUploader  # noqa: PLC0415

        uploader = HFUploader(token)
        result = uploader.push_to_hub(str(repo), dataset_file, tags=list(tags) if tags else [])

        tui = get_tui()
        if result["status"] == "success":
            tui.success(result["message"])
        else:
            tui.error(result["message"])
            sys.exit(1)

    except Exception as e:
        tui = get_tui()
        tui.error(f"Error uploading to Hugging Face Hub: {str(e)}")
        sys.exit(1)


@cli.command()
@click.argument("graph_file", type=click.Path(exists=True))
@click.option(
    "--output",
    "-o",
    required=True,
    help="Output SVG file path",
)
def visualize(graph_file: str, output: str) -> None:
    """Visualize a topic graph as an SVG file."""
    try:
        # Load the graph
        with open(graph_file) as f:
            import json  # noqa: PLC0415

            graph_data = json.load(f)

        # Create a minimal Graph object for visualization
        # We need to get the args from somewhere - for now, use defaults
        from .constants import (  # noqa: PLC0415
            TOPIC_GRAPH_DEFAULT_DEGREE,
            TOPIC_GRAPH_DEFAULT_DEPTH,
        )

        # Create parameters for Graph instantiation
        graph_params = {
            "topic_prompt": "placeholder",  # Not needed for visualization
            "model_name": "placeholder/model",  # Not needed for visualization
            "degree": graph_data.get("degree", TOPIC_GRAPH_DEFAULT_DEGREE),
            "depth": graph_data.get("depth", TOPIC_GRAPH_DEFAULT_DEPTH),
            "temperature": 0.7,  # Default, not used for visualization
        }

        # Use the Graph.from_json method to properly load the graph structure
        import tempfile  # noqa: PLC0415

        # Create a temporary file with the graph data and use from_json
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as tmp_file:
            json.dump(graph_data, tmp_file)
            temp_path = tmp_file.name

        try:
            graph = Graph.from_json(temp_path, graph_params)
        finally:
            import os  # noqa: PLC0415

            os.unlink(temp_path)

        # Visualize the graph
        graph.visualize(output)
        tui = get_tui()
        tui.success(f"Graph visualization saved to: {output}.svg")

    except Exception as e:
        tui = get_tui()
        tui.error(f"Error visualizing graph: {str(e)}")
        sys.exit(1)


@cli.command()
@click.argument("config_file", type=click.Path(exists=True))
def validate(config_file: str) -> None:  # noqa: PLR0912
    """Validate a DeepFabric configuration file."""
    try:
        # Try to load the configuration
        config = DeepFabricConfig.from_yaml(config_file)

        # Check required sections
        errors = []
        warnings = []

        # Check for system prompt (with fallback check)
        engine_params = config.get_engine_params()
        if not config.dataset_system_prompt and not engine_params.get("generation_system_prompt"):
            warnings.append("No dataset_system_prompt or generation_system_prompt defined")

        # Check for either topic_tree or topic_graph
        if not config.topic_tree and not config.topic_graph:
            errors.append("Either topic_tree or topic_graph must be defined")

        if config.topic_tree and config.topic_graph:
            warnings.append("Both topic_tree and topic_graph defined - only one will be used")

        # Check data_engine section
        if not config.data_engine:
            errors.append("data_engine section is required")
        elif not config.data_engine.instructions:
            warnings.append("No instructions defined in data_engine")

        # Check dataset section
        if not config.dataset:
            errors.append("dataset section is required")
        else:
            dataset_config = config.get_dataset_config()
            if not dataset_config.get("save_as"):
                warnings.append("No save_as path defined for dataset")

        # Report results
        tui = get_tui()
        if errors:
            tui.error("Configuration validation failed:")
            for error in errors:
                tui.console.print(f"  - {error}", style="red")
            sys.exit(1)
        else:
            tui.success("Configuration is valid")

        if warnings:
            tui.console.print("\nWarnings:", style="yellow bold")
            for warning in warnings:
                tui.warning(warning)

        # Print configuration summary
        tui.console.print("\nConfiguration Summary:", style="cyan bold")
        if config.topic_tree:
            tui.info(
                f"Topic Tree: depth={config.topic_tree.depth}, degree={config.topic_tree.degree}"
            )
        if config.topic_graph:
            tui.info(
                f"Topic Graph: depth={config.topic_graph.depth}, degree={config.topic_graph.degree}"
            )

        dataset_params = config.get_dataset_config()["creation"]
        tui.info(
            f"Dataset: steps={dataset_params['num_steps']}, batch_size={dataset_params['batch_size']}"
        )

        if config.huggingface:
            hf_config = config.get_huggingface_config()
            tui.info(f"Hugging Face: repo={hf_config.get('repository', 'not set')}")

    except FileNotFoundError:
        handle_error(
            click.get_current_context(),
            ValueError(f"Config file not found: {config_file}"),
        )
    except yaml.YAMLError as e:
        handle_error(
            click.get_current_context(),
            ValueError(f"Invalid YAML in config file: {str(e)}"),
        )
    except Exception as e:
        handle_error(
            click.get_current_context(),
            ValueError(f"Error validating config file: {str(e)}"),
        )


@cli.command()
def info() -> None:
    """Show DeepFabric version and configuration information."""
    try:
        import importlib.metadata  # noqa: PLC0415

        # Get version
        try:
            version = importlib.metadata.version("deepfabric")
        except importlib.metadata.PackageNotFoundError:
            version = "development"

        tui = get_tui()
        header = tui.create_header(
            f"DeepFabric v{version}", "Large Scale Topic based Synthetic Data Generation"
        )
        tui.console.print(header)

        tui.console.print("\n📋 Available Commands:", style="cyan bold")
        commands = [
            ("generate", "Generate training data from configuration"),
            ("validate", "Validate a configuration file"),
            ("visualize", "Create SVG visualization of a topic graph"),
            ("upload", "Upload dataset to Hugging Face Hub"),
            ("info", "Show this information"),
        ]
        for cmd, desc in commands:
            tui.console.print(f"  [cyan]{cmd}[/cyan] - {desc}")

        tui.console.print("\n🔑 Environment Variables:", style="cyan bold")
        env_vars = [
            ("OPENAI_API_KEY", "OpenAI API key"),
            ("ANTHROPIC_API_KEY", "Anthropic API key"),
            ("HF_TOKEN", "Hugging Face API token"),
        ]
        for var, desc in env_vars:
            tui.console.print(f"  [yellow]{var}[/yellow] - {desc}")

        tui.console.print(
            "\n🔗 For more information, visit: [link]https://github.com/RedDotRocket/deepfabric[/link]"
        )

    except Exception as e:
        tui = get_tui()
        tui.error(f"Error getting info: {str(e)}")
        sys.exit(1)


# Add the format command to the CLI group
cli.add_command(format_cli)

if __name__ == "__main__":
    cli()

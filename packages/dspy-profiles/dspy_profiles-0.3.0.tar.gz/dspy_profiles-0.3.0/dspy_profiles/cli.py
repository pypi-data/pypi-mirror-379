"""Main CLI application for dspy-profiles."""

import typer

from dspy_profiles import __version__
from dspy_profiles.commands.delete import delete_profile
from dspy_profiles.commands.diff import diff_profiles
from dspy_profiles.commands.import_profile import import_profile
from dspy_profiles.commands.init import init_profile
from dspy_profiles.commands.list import list_profiles
from dspy_profiles.commands.run import run_command
from dspy_profiles.commands.set import set_value
from dspy_profiles.commands.show import show_profile
from dspy_profiles.commands.test import test_profile
from dspy_profiles.commands.validate import validate_profiles
from dspy_profiles.config import find_profiles_path
from dspy_profiles.logging_utils import compute_level, setup_logging


def version_callback(value: bool):
    """Prints the version of the package."""
    if value:
        print(f"dspy-profiles version: {__version__}")
        raise typer.Exit()


app = typer.Typer(
    name="dspy-profiles",
    help="A CLI for managing DSPy profiles.",
    no_args_is_help=True,
    add_completion=False,
    rich_markup_mode="markdown",
)


@app.callback()
def root_callback(
    version: bool = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the version and exit.",
        callback=version_callback,
        is_eager=True,
    ),
    verbose: int = typer.Option(
        0,
        "--verbose",
        "-V",
        count=True,
        help="Increase verbosity (-V for INFO, -VV for DEBUG).",
    ),
    quiet: int = typer.Option(
        0,
        "--quiet",
        "-q",
        count=True,
        help="Decrease verbosity (once for ERROR).",
    ),
    log_level: str | None = typer.Option(
        None,
        "--log-level",
        help="Explicit log level (DEBUG, INFO, WARNING, ERROR). Overrides -V/-q.",
    ),
):
    """Manage DSPy profiles."""
    # Configure logging once per CLI invocation
    level = compute_level(verbose=verbose, quiet=quiet, log_level=log_level)
    setup_logging(level)


# Add command functions
app.command(name="list")(list_profiles)
app.command(name="show")(show_profile)
app.command(name="delete")(delete_profile)
app.command(name="set")(set_value)
app.command(name="init")(init_profile)
app.command(name="import")(import_profile)
app.command(name="diff")(diff_profiles)
app.command(name="validate")(validate_profiles)
app.command(name="test")(test_profile)
app.command(
    name="run",
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True},
)(run_command)


# Utilities
@app.command(name="which-config")
def which_config():
    """Print the resolved profiles.toml path and whether it exists."""
    path = find_profiles_path()
    exists = path.exists()
    print(f"Resolved config path: {path}")
    print(f"Exists: {'yes' if exists else 'no'}")


def main():
    app(prog_name="dspy-profiles")


if __name__ == "__main__":  # pragma: no cover
    main()

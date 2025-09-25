import sys
from pathlib import Path

import click
from mhd_model import __version__

from mw2mhd.commands.create import creation_cli
from mw2mhd.commands.fetch_mw_study import fetch_mw_study
from mw2mhd.commands.validate import validation_cli


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(__version__)
def cli():
    """Metabomics Workbench - MHD Integration CLI with subcommands."""
    pass


cli.add_command(fetch_mw_study)
cli.add_command(creation_cli)
cli.add_command(validation_cli)

if __name__ == "__main__":
    sys.path.insert(0, str(Path.cwd()))
    if len(sys.argv) == 1:
        cli(["--help"])
    else:
        cli()

import sys
from pathlib import Path

import click
from mhd_model import __version__

from gnps2mhd.commands.create import creation_cli
from gnps2mhd.commands.fetch_gnps_study import fetch_gnps_study
from gnps2mhd.commands.validate import validation_cli


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(__version__)
def cli():
    """GNPS/MassIVE - MHD Integration CLI.

    Use this cli to create MHD model file,
    convert MHD model file to announcement file,
    and fetch GNPS/MassIVE params.xml metadata file.
    """
    pass


cli.add_command(fetch_gnps_study)
cli.add_command(creation_cli)
cli.add_command(validation_cli)

if __name__ == "__main__":
    sys.path.insert(0, str(Path.cwd()))
    if len(sys.argv) == 1:
        cli(["--help"])
    else:
        cli()

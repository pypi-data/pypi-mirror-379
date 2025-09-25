import json
import logging
from pathlib import Path

import click

from gnps2mhd.v0_1.utils import fetch_massive_metadata_file

logger = logging.getLogger(__name__)


@click.command(name="download", no_args_is_help=True)
@click.option(
    "--output-dir",
    default="outputs",
    show_default=True,
    help="Output directory for GNPS/MassIVE metadata file.",
)
@click.option(
    "--output-filename",
    default=None,
    show_default=True,
    help="Metadata json file converted from GNPS/MassIVE params.xml file."
    " Default is <study_id>.params.xml.json",
)
@click.argument("study_id")
def fetch_gnps_study(
    study_id: str,
    output_dir: str,
    output_filename: str,
):
    """Fetch a GNPS/MassIVE study params.xml and convert it to json.

    \b
    Args:
    study_id (str): GNPS/MassIVE study id (e.g. MSV000001)
    """

    data = fetch_massive_metadata_file(study_id)
    mhd_output_root_path = Path(output_dir)
    mhd_output_root_path.mkdir(exist_ok=True, parents=True)
    output_folder_path = Path(f"{output_dir.rstrip('/')}/{study_id}.params.xml.json")
    if output_filename:
        output_folder_path = Path(f"{output_dir.rstrip('/')}/{output_filename}")
    with output_folder_path.open("w") as f:
        json.dump(data, f, indent=4)
    if not data:
        click.echo(f"{study_id} failed.")
        exit(1)
    click.echo(f"{study_id} is donwloaded.")


if __name__ == "__main__":
    fetch_gnps_study(["MSV000099062"])

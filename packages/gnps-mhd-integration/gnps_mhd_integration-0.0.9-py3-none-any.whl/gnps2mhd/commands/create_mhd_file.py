import logging
from pathlib import Path

import click
from mhd_model.model.definitions import (
    MHD_MODEL_V0_1_DEFAULT_SCHEMA_NAME,
    MHD_MODEL_V0_1_LEGACY_PROFILE_NAME,
)

from gnps2mhd.convertor_factory import Gnps2MhdConvertorFactory

logger = logging.getLogger(__name__)


@click.command(name="mhd", no_args_is_help=True)
@click.option(
    "--input-file-path",
    default=None,
    help="Input file path of params.xml. If it is not defined, the params.xml will be fetched from MassIVE.",
)
@click.option(
    "--output-dir",
    default="outputs",
    show_default=True,
    help="Output directory for MHD file",
)
@click.option(
    "--output-filename",
    default=None,
    show_default=True,
    help="MHD filename (e.g., MHD000001.mhd.json, ST000001.mhd.json)",
)
@click.option(
    "--schema_uri",
    default=MHD_MODEL_V0_1_DEFAULT_SCHEMA_NAME,
    show_default=True,
    help="Target MHD model schema. It defines format of MHD model structure.",
)
@click.option(
    "--profile_uri",
    default=MHD_MODEL_V0_1_LEGACY_PROFILE_NAME,
    show_default=True,
    help="Target MHD model profile. It is used to validate MHD model",
)
@click.argument("massive_study_id")
@click.argument("mhd_identifier")
def create_mhd_file(
    massive_study_id: str,
    mhd_identifier: str,
    output_dir: str,
    output_filename: str,
    schema_uri: str,
    profile_uri: str,
    input_file_path: None | str,
):
    """Convert a GNPS/MassIVE study to MHD model file."""

    if massive_study_id == mhd_identifier:
        mhd_identifier = None

    factory = Gnps2MhdConvertorFactory()
    convertor = factory.get_convertor(
        target_mhd_model_schema_uri=schema_uri,
        target_mhd_model_profile_uri=profile_uri,
    )
    mhd_output_root_path = Path(output_dir)
    mhd_output_root_path.mkdir(exist_ok=True, parents=True)
    try:
        convertor.convert(
            repository_name="GNPS/MassIVE",
            repository_identifier=massive_study_id,
            mhd_identifier=mhd_identifier,
            mhd_output_folder_path=mhd_output_root_path,
            mhd_output_filename=output_filename,
            input_file_path=input_file_path,
        )
        click.echo(f"{massive_study_id} is converted successfully.")
    except Exception as ex:
        click.echo(f"{massive_study_id} conversion failed. {str(ex)}")


if __name__ == "__main__":
    create_mhd_file(["MSV000099062"])

import logging
from pathlib import Path

from mhd_model.model.v0_1.dataset.profiles.base import graph_nodes as mhd_domain
from mhd_model.model.v0_1.dataset.profiles.base.dataset_builder import MhDatasetBuilder
from mhd_model.model.v0_1.dataset.profiles.base.profile import MhDatasetBaseProfile
from mhd_model.model.v0_1.dataset.profiles.ms.profile import MhDatasetMsProfile
from mhd_model.shared.model import Revision

from gnps2mhd.config import Gnps2MhdConfiguration
from gnps2mhd.v0_1.utils import create_cv_term_value_object, fetch_massive_metadata_file

logger = logging.getLogger(__name__)


class MhdMsDatasetBuilder:
    def build(
        self,
        mhd_id: None | str,
        mhd_output_path: Path,
        massive_study_id: str,
        target_mhd_model_schema_uri: str,
        target_mhd_model_profile_uri: str,
        config: Gnps2MhdConfiguration,
        repository_name: str,
        revision: None | Revision = None,
        **kwargs,
    ) -> MhDatasetMsProfile:
        cache_root_path = kwargs.get("cache_root_path", None)
        # Fetch metadata from Massive. Remove if it is not needed.
        params = fetch_massive_metadata_file(
            massive_study_id, cache_root_path=cache_root_path
        )
        if not params:
            raise ValueError(f"Could not fetch metadata for study {massive_study_id}")
        # TODO: Fetch other files or connect to a database to get more ingformation

        mhd_builder = MhDatasetBuilder(
            repository_name=repository_name,
            mhd_identifier=mhd_id,
            repository_identifier=massive_study_id,
            schema_name=target_mhd_model_schema_uri,
            profile_uri=target_mhd_model_profile_uri,
            repository_revision=revision.revision if revision else 1,
            repository_revision_datetime=revision.revision_datetime
            if revision
            else None,
            change_log=[revision] if revision else None,
        )
        #####################################################################################
        # TODO: IMPLEMENT CONVERTOR
        # TODO: ....
        #####################################################################################
        dataset_provider = create_cv_term_value_object(
            type_="data-provider",
            source="NCIT",
            accession="NCIT:C189151",
            name="Study Data Repository",
            value=repository_name,
        )
        mhd_study = mhd_domain.Study(
            repository_identifier=massive_study_id,
            created_by_ref=dataset_provider.id_,
            mhd_identifier=mhd_id,
            title="",  # TODO: FILL
            description="",  # TODO: FILL
            submission_date=None,  # TODO: FILL
            public_release_date=None,  # TODO: FILL
            dataset_url_list=[],  # TODO: FILL
        )
        #####################################################################################
        # Build and save dataset
        #####################################################################################

        mhd_dataset: MhDatasetBaseProfile = mhd_builder.create_dataset(
            start_item_refs=[mhd_study.id_], dataset_class=MhDatasetMsProfile
        )
        filename = mhd_id if mhd_id else massive_study_id
        mhd_dataset.name = f"{filename} MetabolomicsHub Legacy Dataset"
        mhd_output_path.mkdir(parents=True, exist_ok=True)
        output_path = mhd_output_path / Path(f"{filename}.mhd.json")
        output_path.open("w").write(
            mhd_dataset.model_dump_json(
                indent=4, by_alias=True, exclude_none=True, serialize_as_any=True
            )
        )
        logger.info(
            "%s study MHD file is created with name: %s", massive_study_id, output_path
        )
        return mhd_dataset

import datetime
import json
import logging
from pathlib import Path
from urllib.parse import quote

from mhd_model.model.v0_1.dataset.profiles.base import graph_nodes as mhd_domain
from mhd_model.model.v0_1.dataset.profiles.base.dataset_builder import MhDatasetBuilder
from mhd_model.model.v0_1.dataset.profiles.base.profile import MhDatasetBaseProfile
from mhd_model.model.v0_1.dataset.profiles.legacy.profile import MhDatasetLegacyProfile
from mhd_model.model.v0_1.rules.managed_cv_terms import (
    COMMON_ASSAY_TYPES,
    COMMON_CHARACTERISTIC_DEFINITIONS,
    COMMON_MEASUREMENT_TYPES,
    COMMON_OMICS_TYPES,
    COMMON_PARAMETER_DEFINITIONS,
    COMMON_PROTOCOLS,
    COMMON_STUDY_FACTOR_DEFINITIONS,
)
from mhd_model.shared.model import CvTerm, Revision
from pydantic import AnyUrl, HttpUrl

from gnps2mhd.config import Gnps2MhdConfiguration
from gnps2mhd.v0_1.utils import (
    create_cv_term_object,
    create_cv_term_value_object,
    fetch_massive_metadata_file,
)

logger = logging.getLogger(__name__)


## GNPS RELATED CONFIGURATION ###
##############################################################################################################
GNPS_ASSAY_TYPES = {
    "LC-MS": COMMON_ASSAY_TYPES["OBI:0003097S"],
    "GC-MS": COMMON_ASSAY_TYPES["OBI:0003110"],
    # TODO: Add more assay types if needed
}
GNPS_MEASUREMENT_TYPES = {
    "targeted": COMMON_MEASUREMENT_TYPES["MSIO:0000100"],
    "untargeted": COMMON_MEASUREMENT_TYPES["MSIO:0000101"],
}

DEFAULT_OMICS_TYPE = COMMON_OMICS_TYPES["EDAM:3172"]

COMMON_PROTOCOLS_MAP = {
    "Sample collection": COMMON_PROTOCOLS["EFO:0005518"],
    "Extraction": COMMON_PROTOCOLS["MS:1000831"],
    "Mass spectrometry": COMMON_PROTOCOLS["CHMO:0000470"],
    "Data transformation": COMMON_PROTOCOLS["OBI:0200000"],
    "Metabolite identification": COMMON_PROTOCOLS["MI:2131"],
    "Chromatography": COMMON_PROTOCOLS["CHMO:0001000"],
    "Treatment": COMMON_PROTOCOLS["EFO:0003969"],
    "Flow Injection Analysis": COMMON_PROTOCOLS["MS:1000058"],
    "Capillary Electrophoresis": COMMON_PROTOCOLS["CHMO:0001024"],
    # TODO: Update after adding to managed CV terms
}

GNPS_PROTOCOLS_MAP = COMMON_PROTOCOLS_MAP.copy()

MANAGED_CHARACTERISTICS_MAP = {
    "organism": COMMON_CHARACTERISTIC_DEFINITIONS["NCIT:C14250"],
    "organism part": COMMON_CHARACTERISTIC_DEFINITIONS["NCIT:C103199"],
    "disease": COMMON_CHARACTERISTIC_DEFINITIONS["EFO:0000408"],
    "cell type": COMMON_CHARACTERISTIC_DEFINITIONS["EFO:0000324"],
}
MANAGED_STUDY_FACTOR_MAP = {
    "disease": COMMON_STUDY_FACTOR_DEFINITIONS["EFO:0000408"],
    "treatment": CvTerm(source="EFO", accession="EFO:0000727", name="treatment"),
}


FILE_EXTENSIONS: dict[tuple[str, bool], CvTerm] = {
    (".d", True): CvTerm(
        source="MS", accession="MS:1002302", name="Bruker Container format"
    ),
    (".raw", False): CvTerm(source="EDAM", accession="EDAM:3712", name="Thermo RAW"),
    (".raw", True): CvTerm(source="EDAM", accession="EDAM:3858", name="Waters RAW"),
    (".wiff", False): CvTerm(source="EFO", accession="EDAM:3710", name="WIFF format"),
    (".mzml", False): CvTerm(source="EDAM", accession="EDAM:3244", name="mzML"),
    (".mzdata", False): CvTerm(source="EFO", accession="EDAM:3834", name="mzData"),
    (".mzxml", False): CvTerm(source="EDAM", accession="EDAM:3654", name="mzXML"),
    (".ibd", False): CvTerm(source="EDAM", accession="EDAM:3839", name="ibd"),
}


class MhdLegacyDatasetBuilder:
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
    ) -> MhDatasetLegacyProfile:
        cache_root_path = kwargs.get("cache_root_path", None)
        params_xml_file_path = kwargs.get("input_file_path", None)
        params = None
        if params_xml_file_path:
            params_xml_path = Path(params_xml_file_path)

            if not params_xml_path.exists():
                raise ValueError(f"File does not exist: {params_xml_file_path}")
            with params_xml_path.open() as f:
                params = json.load(f)

        if not params:
            # Fetch metadata from Massive.
            params = fetch_massive_metadata_file(
                massive_study_id, cache_root_path=cache_root_path
            )

        if not params:
            raise ValueError(f"Could not fetch metadata for study {massive_study_id}")

        # Fetch other files or connect to a database to get more ingformation

        dataset_provider = create_cv_term_value_object(
            type_="data-provider",
            source="NCIT",
            accession="NCIT:C189151",
            name="Study Data Repository",
            value=repository_name,
        )

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

        study_title = params.get("desc", "")  # set value from other source if not valid
        study_description = params.get("dataset.comments", "")  # set value
        submission_date = datetime.datetime.now(
            datetime.timezone.utc
        )  # TODO:  set value. Currently no public release date
        public_release_date = datetime.datetime.now(
            datetime.timezone.utc
        )  # TODO: set value. Currently no public release date
        massive_study_repository_url = "https://massive.ucsd.edu/????"  # TODO fix
        license = params.get("default.license", "")
        license_url = None
        if license and license.lower() == "on":
            license_url = HttpUrl("https://creativecommons.org/publicdomain/zero/1.0/")
        mhd_study = mhd_domain.Study(
            repository_identifier=massive_study_id,
            created_by_ref=dataset_provider.id_,
            mhd_identifier=mhd_id,
            title=study_title,
            description=study_description,
            submission_date=submission_date,
            public_release_date=public_release_date,
            dataset_url_list=[HttpUrl(massive_study_repository_url)],
            license=license_url,
        )
        massive_volume = params.get("massive_volume", "")  # set value if not valid
        study_public_ftp_url = None
        if massive_volume:
            study_public_ftp_url = (
                f"ftp://massive-ftp.ucsd.edu/{massive_volume}/{massive_study_id}"
            )
            mhd_study.dataset_url_list.append(AnyUrl(study_public_ftp_url))

        mhd_builder.add(mhd_study)
        mhd_builder.add_node(dataset_provider)
        mhd_builder.link(
            dataset_provider,
            "provides",
            mhd_study,
            reverse_relationship_name="provided-by",
        )

        #####################################################################################
        # contact as submitter and principal investigator
        #####################################################################################

        submitter = params.get("dataset.pi", "")  # set value if not valid

        submitter_fields = submitter.split("|")
        if submitter_fields and len(submitter_fields) > 1:
            submitter_full_name = submitter_fields[0].strip()
            submitter_email = submitter_fields[1].strip()

            mhd_contact = mhd_domain.Person(
                full_name=submitter_full_name, email_list=[submitter_email]
            )
            mhd_builder.add(mhd_contact)
            # An assumption is made that PI is also submitter
            mhd_builder.link(
                mhd_contact,
                "submits",
                mhd_study,
                reverse_relationship_name="submitted-by",
            )

            mhd_builder.link(
                mhd_contact,
                "principal-investigator-of",
                mhd_study,
                reverse_relationship_name="has-principal-investigator",
            )

            # Create organization if organization name or address is available
            if len(submitter_fields) > 3:
                organization_name = submitter_fields[2].strip()
                address = submitter_fields[3].strip()
                mhd_organization = mhd_domain.Organization(
                    name=organization_name, address=address
                )
                mhd_builder.add(mhd_organization)
                mhd_builder.link(
                    mhd_organization,
                    "affiliated-with",
                    mhd_contact,
                    reverse_relationship_name="has-affiliation",
                )

        #####################################################################################
        # metadata file.
        #####################################################################################
        params_xml_file_format = create_cv_term_object(
            type_="descriptor", accession="EDAM:2332", source="EDAM", name="XML"
        )  # update if its format is different
        metadata_file_name = (
            "ccms_parameters/params.xml"  # update if its format is different
        )
        metadata_http_file_url = (
            "https://massive.ucsd.edu/ProteoSAFe/DownloadResultFile"
            f"?file=f.{massive_study_id}%2F{quote(metadata_file_name, safe='')}"
        )
        #####################################################################################

        metadata_file = mhd_domain.MetadataFile(
            name=metadata_file_name,
            url_list=[HttpUrl(metadata_http_file_url)],
            extension=Path(metadata_file_name).suffix,
            format_ref=params_xml_file_format.id_,
        )
        if study_public_ftp_url:
            metadata_file.url_list.append(
                AnyUrl(f"{study_public_ftp_url}/{metadata_file_name}")
            )
        mhd_builder.add(params_xml_file_format)
        mhd_builder.add(metadata_file)
        mhd_builder.link(
            mhd_study,
            "has-metadata-file",
            metadata_file,
            reverse_relationship_name="describes",
        )
        #####################################################################################
        # characteristic definition, characteristic type (organism), characteristic value
        #####################################################################################

        species = params.get("dataset.species", "")  # set value if not valid
        species_list = [x.strip() for x in species.split(";")]

        if species_list:
            organism = MANAGED_CHARACTERISTICS_MAP["organism"]
            organism_characteristic_type = create_cv_term_object(
                type_="characteristic-type",
                name=organism.name,
                accession=organism.accession,
                source=organism.source,
            )
            organism_characteristic_definition = mhd_domain.CharacteristicDefinition(
                characteristic_type_ref=organism_characteristic_type.id_,
                name="species",
            )
            mhd_builder.add(organism_characteristic_type)
            mhd_builder.add(organism_characteristic_definition)
            mhd_builder.link(
                organism_characteristic_definition,
                "has-type",
                organism_characteristic_type,
                reverse_relationship_name="type-of",
            )
            mhd_builder.link(
                mhd_study,
                "has-characteristic-definition",
                organism_characteristic_definition,
                reverse_relationship_name="used-in",
            )
            for item in species_list:
                # TODO: Create characteristic value with source and accession if item has valid CURIE
                accession = ""
                source = ""
                if item.upper().startswith("NCBITAXON:"):
                    identifier = item.upper().replace("NCBITAXON:", "")
                    source = "NCBITAXON"
                    accession = f"NCBITacon:{identifier}"

                val = create_cv_term_object(
                    type_="characteristic-value",
                    name=item,
                    source=source,
                    accession=accession,  # TODO?
                )
                mhd_builder.add(val)
                mhd_builder.link(
                    organism_characteristic_definition,
                    "has-instance",
                    val,
                    reverse_relationship_name="instance-of",
                )
        #####################################################################################
        # mass spectrometry protocol, mass spectrometry instrument parameters
        #####################################################################################
        ms_instrument = params.get("ms.instrument", "")  # set value if not valid

        ms_instrument_list = [x.strip() for x in ms_instrument.split(";") if x]
        if ms_instrument_list:
            ms_protocol_type_cv = COMMON_PROTOCOLS_MAP["Mass spectrometry"]
            ms_protocol_type = create_cv_term_object(
                type_="protocol-type",
                name=ms_protocol_type_cv.name,
                accession=ms_protocol_type_cv.accession,
                source=ms_protocol_type_cv.source,
            )
            ms_protocol = mhd_domain.Protocol(
                name="Mass spectrometry",
                protocol_type_ref=ms_protocol_type.id_,
                description="Mass spectrometry protocol",
            )
            mhd_builder.add(ms_protocol_type)
            mhd_builder.add(ms_protocol)
            mhd_builder.link(
                ms_protocol,
                "has-type",
                ms_protocol_type,
                reverse_relationship_name="type-of",
            )
            mhd_builder.link(
                mhd_study,
                "has-protocol",
                ms_protocol,
                reverse_relationship_name="used-in",
            )
            if not mhd_study.protocol_refs:
                mhd_study.protocol_refs = []
            mhd_study.protocol_refs.append(ms_protocol.id_)

            ms_instrument_cv = COMMON_PARAMETER_DEFINITIONS["MSIO:0000171"]
            ms_instrument_parameter_type = create_cv_term_object(
                type_="parameter-type",
                name=ms_instrument_cv.name,
                accession=ms_instrument_cv.accession,
                source=ms_instrument_cv.source,
            )
            ms_instrument_definition = mhd_domain.ParameterDefinition(
                name="Instrument",
                parameter_type_ref=ms_instrument_parameter_type.id_,
            )
            mhd_builder.link(
                ms_instrument_definition,
                "has-type",
                ms_instrument_parameter_type,
                reverse_relationship_name="type-of",
            )
            mhd_builder.link(
                ms_protocol,
                "has-parameter-definition",
                ms_instrument_definition,
                reverse_relationship_name="used-in",
            )

            for item in ms_instrument_list:
                # TODO: Create parameter value with source and accession if item has valid CURIE
                val = create_cv_term_object(
                    type_="parameter-value",
                    name=item,
                    source="",  # TODO?
                    accession="",  # TODO?
                )
                mhd_builder.add(val)
                mhd_builder.link(
                    ms_instrument_definition,
                    "has-instance",
                    val,
                    reverse_relationship_name="instance-of",
                )

        #####################################################################################
        # Submitter keywords
        #####################################################################################

        keywords = params.get("dataset.keywords", "").split(";")
        if keywords:
            keyword_items = [
                x.strip() for x in keywords[0].split(",") if x and x.strip()
            ]
            for item in keyword_items:
                keyword = create_cv_term_object(
                    type_="descriptor",
                    source="",
                    accession="",
                    name=item,
                )
                mhd_builder.add_node(keyword)
                mhd_builder.link(
                    mhd_study,
                    "has-submitter-keyword",
                    keyword,
                    reverse_relationship_name="keyword-of",
                )

        #####################################################################################
        # raw-data files
        #####################################################################################
        raw_data_files = params.get("upload_file_mapping", [])
        file_formats = {}
        file_format = None
        for file in raw_data_files:
            peak_file_name, raw_file_path = file.split("|")
            subpaths = raw_file_path.split("/")
            if len(subpaths) > 1:
                raw_file_path = "/".join(subpaths[1:])
            extension = Path(raw_file_path).suffix
            extension_lower = extension.lower()
            if (extension_lower, False) in FILE_EXTENSIONS:
                data_format_cv = FILE_EXTENSIONS[(extension_lower, False)]

                if (extension_lower, False) not in file_formats:
                    file_format = create_cv_term_object(
                        type_="descriptor",
                        accession=data_format_cv.accession,
                        source=data_format_cv.source,
                        name=data_format_cv.name,
                    )
                    mhd_builder.add_node(file_format)
                    file_formats[(extension_lower, False)] = file_format
                file_format = file_formats[(extension_lower, False)]

            file_node = mhd_domain.RawDataFile(
                name=raw_file_path,
                metadata_file_refs=None,
                compression_format_ref=None,
                format_ref=file_format.id_ if file_format else None,
                extension=extension if extension else None,
                url_list=[],
            )
            if study_public_ftp_url:
                # TODO: validate URL and update
                file_node.url_list.append(
                    AnyUrl(f"{study_public_ftp_url}/peak/{raw_file_path}")
                )
            mhd_builder.add_node(file_node)
            mhd_builder.link(
                mhd_study,
                "has-raw-data-file",
                file_node,
                reverse_relationship_name="created-in",
            )

        #####################################################################################
        # Build and save dataset
        #####################################################################################

        mhd_dataset: MhDatasetBaseProfile = mhd_builder.create_dataset(
            start_item_refs=[mhd_study.id_], dataset_class=MhDatasetLegacyProfile
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

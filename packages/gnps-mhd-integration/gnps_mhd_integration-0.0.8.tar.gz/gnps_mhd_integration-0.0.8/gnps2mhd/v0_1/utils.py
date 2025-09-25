import json
import logging
from pathlib import Path
from urllib.parse import quote

import httpx
import xmltodict
from mhd_model.model.v0_1.dataset.profiles.base import graph_nodes as mhd_domain
from mhd_model.shared.model import UnitCvTerm

logger = logging.getLogger(__name__)


def create_cv_term_object(
    type_: str, accession: str, source: str, name: str
) -> mhd_domain.CvTermObject:
    if not source or not accession:
        return mhd_domain.CvTermObject(type_=type_, name=name)

    return mhd_domain.CvTermObject(
        type_=type_, accession=accession, source=source, name=name
    )


def create_cv_term_value_object(
    type_: str,
    accession: str = "",
    source: str = "",
    name: str = "",
    value: None | str = None,
    unit: None | UnitCvTerm = None,
) -> mhd_domain.CvTermValueObject:
    unit_cv = None
    if unit:
        if not source or not accession:
            unit_cv = UnitCvTerm(name=unit.name) if unit else None

    if not source or not accession:
        return mhd_domain.CvTermValueObject(
            type_=type_, name=name, value=value, unit=unit_cv
        )

    return mhd_domain.CvTermValueObject(
        type_=type_,
        accession=accession,
        source=source,
        name=name,
        value=value,
        unit=unit_cv,
    )


def fetch_massive_metadata_file(
    massive_study_id: str, cache_root_path: None | str = None
):
    cache_path = None
    if cache_root_path:
        cache_path = Path(f"{cache_root_path}/{massive_study_id}.params.xml.json")
        try:
            if cache_path.exists():
                with cache_path.open() as f:
                    json_data = json.load(f)
                return json_data
        except Exception as ex:
            logger.error("Error loading from cache. %s", ex)
            pass

    metadata_file_name = "ccms_parameters/params.xml"
    metadata_http_file_url = (
        "https://massive.ucsd.edu/ProteoSAFe/DownloadResultFile"
        f"?file=f.{massive_study_id}%2F{quote(metadata_file_name, safe='')}"
    )
    try:
        response = httpx.get(metadata_http_file_url, timeout=5)
        response.raise_for_status()

        # Parse XML to OrderedDict
        json_data = xmltodict.parse(response.text)
        params = json_data.get("parameters", {}).get("parameter", [])
        params_dict = {}
        for x in params:
            name = x.get("@name")
            val = x.get("#text")
            if name not in params_dict:
                params_dict[name] = val
            else:
                if isinstance(params_dict[name], list):
                    params_dict[name].append(val)
                else:
                    params_dict[name] = [val]
        if cache_path:
            with cache_path.open("w") as f:
                json.dump(params_dict, f, indent=4)
        return params_dict

    except Exception as e:
        import traceback

        traceback.print_exc()
        logger.error("Error fetching massive metadata file %s: %s", massive_study_id, e)

    return None

from cytoolz.curried import curry, unique, concat
from glom import Coalesce

from genomoncology.kms.match import (
    transform_match_response, vie_results_to_alts,
)
from genomoncology.parse import DocType, __TYPE__
from genomoncology.parse.ensures import ensure_collection
import gosdk


@curry
def match_trials(calls, **kwargs):
    diseases = None
    dob = None
    gender = None
    alterations, benign_alterations = vie_results_to_alts(calls)

    diseases = ensure_collection(kwargs.get('diseases') or ["ANY"])

    response = gosdk.call_with_retry(
        gosdk.sdk.trials.match_trials_post,
        alterations=alterations,
        benign_alterations=benign_alterations,
        diseases=diseases,
        date_of_birth=dob,
        gender=gender,
    )

    return transform_match_response(response, DEFAULT_SPEC)


DEFAULT_SPEC = {
    __TYPE__: Coalesce(default=DocType.TRIAL.value),
    "nct_id": "nct_id",
    "title": "title",
    "phase": "phase",
    "recruiting_status": "recruiting_status",
    "trigger_alterations": (
        "detected_alterations",
        ["trigger_alterations"],
        lambda x: list(unique(concat(x))),
    ),
    "trigger_diseases": (
        "matched_diseases",
        ["matched_disease"],
        lambda x: list(unique(x)),
    ),
}

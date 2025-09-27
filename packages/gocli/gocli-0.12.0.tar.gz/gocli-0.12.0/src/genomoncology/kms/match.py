from cytoolz.curried import filter, map, compose, concat

from genomoncology.parse import DocType
from genomoncology.parse.ensures import ensure_collection
from genomoncology.pipeline.converters import non_null
from genomoncology.pipeline.transformers import get_in_field, transform


def calls_to_alterations(calls):
    calls = ensure_collection(calls)
    pipeline = compose(
        concat, filter(non_null), map(get_in_field("annotations.alteration"))
    )
    alterations = list(pipeline(calls))
    return alterations


def vie_results_to_alts(vies):
    vies = ensure_collection(vies)

    # using the VIE response, loop through each variant and add it to either
    # the alterations or benign_alterations lists, depending on the
    # "match_field" value
    alterations = []
    benign_alterations = []

    # now, let's loop through each item and get the vie info
    for vie_result in vies:
        if DocType.HEADER.is_a(vie_result):
            continue
        vie_data = vie_result.get("variant_interpretations", [])
        try:
            alt_name = vie_data[0].get("alteration")
            match_field = vie_data[0].get("match_field")
        except IndexError:
            raise IndexError("This is missing alts or match_field")
        if match_field == "alteration":
            alterations.append(alt_name)
        elif match_field == "benign_alteration":
            benign_alterations.append(alt_name)
    return alterations, benign_alterations


def transform_match_response(response, default_spec):
    transformer = transform(default_spec)
    results = getattr(response, "results", None)
    results = results or response.get("results")
    return map(transformer, results)

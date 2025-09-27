from cytoolz.functoolz import curry
import gosdk
from genomoncology.kms.match import vie_results_to_alts


@curry
def post_match_consolidated_therapies(data, **kwargs):
    # get the alterations and benign alterations from the vie response.
    alterations, benign_alterations = vie_results_to_alts(data)

    consolidated_therapies = gosdk.call_with_retry(
        gosdk.sdk.therapies.therapies_raw_drug_matches_post,
        alterations=alterations,
        benign_alterations=benign_alterations,
        **kwargs
    )
    return consolidated_therapies.marshal()

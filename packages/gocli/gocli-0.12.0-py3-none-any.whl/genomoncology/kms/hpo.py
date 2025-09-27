import gosdk
from cytoolz.curried import curry


@curry
async def load_hpo_records(data, data_set, data_set_version):
    hpo_records = await gosdk.async_call_with_retry(
        gosdk.sdk.hpo.load_hpo,
        data_set=data_set,
        data_set_version=data_set_version,
        data=data,
    )

    return hpo_records

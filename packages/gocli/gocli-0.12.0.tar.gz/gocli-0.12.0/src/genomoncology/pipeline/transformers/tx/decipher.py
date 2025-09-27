from cytoolz.curried import assoc, compose
from genomoncology.parse.doctypes import DocType, __CHILD__, __TYPE__
from genomoncology.pipeline.transformers import register, name_mapping


def parse_float(f):
    try:
        return float(f)
    except ValueError:
        return None


def parse_int(i):
    try:
        return int(i)
    except ValueError:
        return None


def parse_values(x):
    # have to do these conversions due to scientific
    # notation and possible "NA" values
    for name, value in x.items():
        if name.endswith("__float"):
            x[name] = parse_float(value)
        elif name.endswith("__int"):
            x[name] = parse_int(value)
    return x


NAME_MAPPING = {
    "chr": "chr",
    "fusion_partner_chr": "chr",
    "pos": "start",
    "fusion_partner_position": "end",
    "deletion_observations": "deletion_observations",
    "deletion_frequency": "deletion_frequency",
    "duplication_observations": "duplication_observations",
    "duplication_frequency": "duplication_frequency",
    "observations": "observations",
    "frequency": "frequency",
    "sample_size": "sample_size"
}

register(
    input_type=DocType.TSV,
    output_type=DocType.DECIPHER,
    transformer=compose(
        lambda x: assoc(x, __TYPE__, DocType.DECIPHER.value),
        lambda x: parse_values(x),
        name_mapping(NAME_MAPPING),
    ),
)

register(
    input_type=DocType.TSV,
    output_type=DocType.DECIPHER,
    transformer=compose(
        lambda x: assoc(x, __CHILD__, DocType.DECIPHER.value)
    ),
    is_header=True,
)

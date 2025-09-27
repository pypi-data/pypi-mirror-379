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


def remove_unwanted_records(x):
    if x.get("canonical") == "true" and x.get("transcript").startswith("NM") and x.get(
            "mane_select") == "true":
        x.pop("canonical")
        x.pop("transcript")
        x.pop("mane_select")
        return x
    else:
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
    "gene": "gene",
    "ncbi_id": "gene_id",
    "pLI_score__float": "lof.pLI",
    "mis_z__float": "mis.z_score",
    "syn_z__float": "syn.z_score",
    "lof_z__float": "lof.z_score",
    "oe_lof_upper_rank__int": "lof.oe_ci.upper_rank",
    "oe_lof_upper_bin__int": "lof.oe_ci.upper_bin_decile",
    "oe_mis__float": "mis.oe",
    "oe_lof__float": "lof.oe",
    "oe_mis_pphen__float": "mis_pphen.oe",
    "oe_syn__float": "syn.oe",
    "oe_syn_lower__float": "syn.oe_ci.lower",
    "oe_syn_upper__float": "syn.oe_ci.upper",
    "oe_mis_lower__float": "mis.oe_ci.lower",
    "oe_mis_upper__float": "mis.oe_ci.upper",
    "oe_lof_lower__float": "lof.oe_ci.lower",
    "oe_lof_upper__float": "lof.oe_ci.upper",
    # fields for parsing
    "transcript": "transcript",
    "canonical": "canonical",
    "mane_select": "mane_select"
}

register(
    input_type=DocType.TSV,
    output_type=DocType.GNOMAD_GENE,
    transformer=compose(
        lambda x: remove_unwanted_records(x),
        lambda x: parse_values(x),
        lambda x: assoc(x, __TYPE__, DocType.GNOMAD_GENE.value),
        lambda x: assoc(x, "is_gene_annotation", True),
        name_mapping(NAME_MAPPING, ignore_period=True),
    ),
)

register(
    input_type=DocType.TSV,
    output_type=DocType.GNOMAD_GENE,
    transformer=compose(
        lambda x: assoc(x, __CHILD__, DocType.GNOMAD_GENE.value)
    ),
    is_header=True,
)

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
    "gene": "Gene",
    "disease__string": "Disease",
    "genomenon_classification__string": "Genomenon Classification",
    "inheritance__string": "Inheritance",
    "case_pmids__mstring": "Case PMIDs",
    "functional_pmids__mstring": "Functional PMIDs",
    "protein_shift__string": "Protein Shift",
    "clingen_haploinsufficiency_score__float":
        "ClinGen haploinsufficiency score",
    "clingen_haploinsufficiency_evidence__string":
        "ClinGen haploinsufficiency evaluation",
    "decipher_haploinsufficiency_score__float":
        "DECIPHER haploinsufficiency score (pHaplo)",
    "decipher_haploinsufficiency_evidence__string":
        "DECIPHER haploinsufficiency evaluation",
    "clinvar_pathogenic_lof__string":
        "ClinVar (#P/LP LOF variants)/(all P/LP variants) for that gene",
    "clinvar_pathogenic_lof_eval__string":
        "ClinVar (#P/LP LOF variants)/(all P/LP variants) for that gene evaluation",
    "clinvar_pathogenic_lof_cnv__string":
        "ClinVar (# of P/LP LOF + CNV)/(# all P/LP)",
    "clinvar_pathogenic_lof_cnv_eval__string":
        "ClinVar (# of P/LP LOF + CNV)/(# all P/LP) evaluation",
    "gnomad_pli__float": "pLI from gnomAD",
    "gnomad_pli_eval__string": "pLI from gnomAD evaluation",
    "gnomad_loeuf__float": "LOEUF from gnomAD",
    "gnomad_loeuf_eval__string": "LOEUF from gnomAD evaluation",
    "clinvar_pathogenic_ms__string":
        "ClinVar (P/LP missense)/(all P/LP) for that gene",
    "clinvar_pathogenic_ms_eval__string":
        "ClinVar (P/LP missense)/(all P/LP) for that gene evaluation",
    "gnomad_z_score__float": "Z-score gnomAD",
    "gnomad_z_score_eval__string": "Z-score gnomAD evaluation",
    "95percent_of_pathogenic_lof__string":
        "≥95% of P/LP variants are LOF and there are over 100 variants in CV"
}

register(
    input_type=DocType.TSV,
    output_type=DocType.GENOMENON_GENE,
    transformer=compose(
        lambda x: parse_values(x),
        lambda x: assoc(x, __TYPE__, DocType.GENOMENON_GENE.value),
        lambda x: assoc(x, "is_gene_annotation", True),
        name_mapping(NAME_MAPPING),
    ),
)

register(
    input_type=DocType.TSV,
    output_type=DocType.GENOMENON_GENE,
    transformer=compose(
        lambda x: assoc(x, __CHILD__, DocType.GENOMENON_GENE.value)
    ),
    is_header=True,
)

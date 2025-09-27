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


def parse_genomic_location_and_pmids(x):
    """Parse genomic location and PMID fields, then clean up temporary fields"""

    genomic_location = x.get("genomic_location", "")

    if genomic_location and genomic_location.strip():
        try:
            # Parse format like "chr15:32925116-34671002"
            chr_part, position_part = genomic_location.split(':')
            c = chr_part.replace('chr', '')
            start_pos, end_pos = position_part.split('-')

            x['chr'] = c
            x['fusion_partner_chr'] = c
            x['pos'] = int(start_pos)
            x['fusion_partner_position'] = int(end_pos)
        except (ValueError, AttributeError, IndexError):
            x['chr'] = ''
            x['fusion_partner_chr'] = ''
            x['pos'] = None
            x['fusion_partner_position'] = None
    else:
        x['chr'] = ''
        x['fusion_partner_chr'] = ''
        x['pos'] = None
        x['fusion_partner_position'] = None

    # Collect Triplosensitivity PMIDs (using LEFT side field names from mapping)
    triplosensitivity_pmids = []
    for i in range(1, 7):
        pmid_field = f"triplo_pmid{i}"  # LEFT side of mapping
        pmid_value = x.get(pmid_field, '')
        if pmid_value and pmid_value.strip():
            triplosensitivity_pmids.append(pmid_value.strip())

    # Collect Haploinsufficiency PMIDs (using LEFT side field names from mapping)
    haploinsufficiency_pmids = []
    for i in range(1, 7):
        pmid_field = f"haplo_pmid{i}"  # LEFT side of mapping
        pmid_value = x.get(pmid_field, '')
        if pmid_value and pmid_value.strip():
            haploinsufficiency_pmids.append(pmid_value.strip())

    # Add the new fields
    x['triplosensitivity_pubmed_id__mstring'] = triplosensitivity_pmids
    x['haploinsufficiency_pubmed_id__mstring'] = haploinsufficiency_pmids

    # Clean up temporary fields (remove the LEFT side mapped field names)
    x.pop('genomic_location', None)
    for i in range(1, 7):
        x.pop(f'triplo_pmid{i}', None)
        x.pop(f'haplo_pmid{i}', None)

    return x


NAME_MAPPING = {
    "region_id": "ISCA ID",
    "cytoband": "cytoBand",
    "haploinsufficiency_score__int": "Haploinsufficiency Score",
    "haploinsufficiency_evidence__string": "Haploinsufficiency Description",
    "triplosensitivity_score__int": "Triplosensitivity Score",
    "triplosensitivity_evidence__string": "Triplosensitivity Description",
    "haploinsufficient_phenotype_ID__mstring": "Haploinsufficiency Disease ID",
    "triplosensitive_phenotype_ID__mstring": "Triplosensitivity Disease ID",
    # Add genomic location and PMID fields to mapping
    "genomic_location": "Genomic Location",
    "triplo_pmid1": "Triplosensitivity PMID1",
    "triplo_pmid2": "Triplosensitivity PMID2",
    "triplo_pmid3": "Triplosensitivity PMID3",
    "triplo_pmid4": "Triplosensitivity PMID4",
    "triplo_pmid5": "Triplosensitivity PMID5",
    "triplo_pmid6": "Triplosensitivity PMID6",
    "haplo_pmid1": "Haploinsufficiency PMID1",
    "haplo_pmid2": "Haploinsufficiency PMID2",
    "haplo_pmid3": "Haploinsufficiency PMID3",
    "haplo_pmid4": "Haploinsufficiency PMID4",
    "haplo_pmid5": "Haploinsufficiency PMID5",
    "haplo_pmid6": "Haploinsufficiency PMID6",
}

register(
    input_type=DocType.TSV,
    output_type=DocType.CLINGEN_DOSAGE_REGION,
    transformer=compose(
        lambda x: assoc(x, __TYPE__, DocType.CLINGEN_DOSAGE_REGION.value),
        parse_genomic_location_and_pmids,
        lambda x: parse_values(x),
        name_mapping(NAME_MAPPING),
    ),
)

register(
    input_type=DocType.TSV,
    output_type=DocType.CLINGEN_DOSAGE_REGION,
    transformer=compose(
        lambda x: assoc(x, __CHILD__, DocType.CLINGEN_DOSAGE_REGION.value)
    ),
    is_header=True,
)

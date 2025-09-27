import json
import re
from collections import defaultdict

from cytoolz.curried import assoc, compose
from genomoncology.parse.doctypes import DocType, __CHILD__, __TYPE__
from genomoncology.pipeline.transformers import register, name_mapping

NAME_MAPPING = {
    "variant_id__string": "variant_id",
    "gene": "gene_symbol",
    "effect_type__string": "effect_type",
    "significance__string": "acmg_call",
    "variant_desc": "variant_desc",
    "full_ontology_paths": "full_ontology_paths",
    "interpretation_summary__string": "json_record",
    "ontology_relations": "ontology_relations",
    "codes__mstring": "curated_categories",
    "canonical_transcript": "canonical_transcript",
    "hgvs_g": "hgvs_g"
}


def get_alterations(x):
    variant_description = x["variant_desc"].replace("p.", "")
    variant_description = variant_description.replace("X", "*")
    x.update({"alterations": [x.get("gene") + " " + variant_description]})
    return x


def parse_and_get_ontologies(x):
    for ontology in x.get("full_ontology_paths", []):
        if ontology.startswith("disease"):
            x["disease_names__mstring"] = ontology.replace("disease/", "")
        if ontology.startswith("fx"):
            x["fx_names__mstring"] = ontology.replace("fx/", "")
    x.pop("full_ontology_paths")
    return x


def json_dump(x):
    # load the interpretation_summary as a json string
    return json.dumps(x.get("interpretation_summary__string"))


def get_ontology_relations(x):
    # get the ontology_relations full_path. It will have a prefix of disease/
    # we want the prefix up until the /
    # create a dict that looks like: {"diseases": [{disease ontology},
    #                                  "mutations": [{mutation ontology}}
    ontology_dict = defaultdict(list)
    for ontology_relation in x.get("ontology_relations", []):
        ontology_name = re.match(r'(.+?)(/)', ontology_relation.get("full_path"))
        if ontology_name:
            ontology_dict[ontology_name.group(1) + "_details"].append(ontology_relation)

    x.update({k: json.dumps(v) for k, v in ontology_dict.items()})
    x.pop("ontology_relations")
    return x


register(
    input_type=DocType.AGGREGATE,
    output_type=DocType.GENOMENON,
    transformer=compose(
        lambda x: assoc(x, __TYPE__, DocType.GENOMENON.value),
        lambda x: assoc(x, "interpretation_summary__string", json_dump(x)),
        get_alterations,
        parse_and_get_ontologies,
        get_ontology_relations,
        name_mapping(NAME_MAPPING),
    ),
)

register(
    transformer=compose(lambda x: assoc(x, __CHILD__, DocType.GENOMENON.value)),
    input_type=DocType.AGGREGATE,
    output_type=DocType.GENOMENON,
    is_header=True,
)

import xml.etree.cElementTree as etree
import re
from cytoolz import curry

from genomoncology.pipeline.sources.base import LazyFileSource
# flake8: noqa

VARIANT_TYPE_BLACKLIST = [
    "Phase unknown",
    "Haplotype",
    "fusion",
    "Translocation",
    "Complex",
    "copy number loss",
    "copy number gain",
    "CompoundHeterozygote",
    "Diplotype",
]

ACCESSION = "Accession"
ASSEMBLY = "Assembly"
CLASSIFICATION = "Classification"
CLASSIFICATIONS = "Classifications"
CLASSIFIED_CONDITION = "ClassifiedCondition"
CLASSIFIED_CONDITION_LIST = "ClassifiedConditionList"
CLASSIFIED_RECORD = "ClassifiedRecord"
CLINICAL_ASSERTION = "ClinicalAssertion"
CLINICAL_ASSERTION_ID = "ClinicalAssertionID"
CLINICAL_ASSERTION_LIST = "ClinicalAssertionList"
CLINVAR_ACCESSION = "ClinVarAccession"
CLINICAL_IMPACT_ASSERTION_TYPE = "ClinicalImpactAssertionType"
CLINICAL_IMPACT_CLINICAL_SIGNIFICANCE = "ClinicalImpactClinicalSignificance"
DESCRIPTION = "Description"
ELEMENT_VALUE = "ElementValue"
ID = "ID"
GENE = "Gene"
GENE_LIST = "GeneList"
GERMLINE_CLASSIFICATION = "GermlineClassification"
GRCH_37 = "GRCh37"
GRCH_38 = "GRCh38"
INCLUDED_RECORD = "IncludedRecord"
INTERPRETATION = "Interpretation"
INTERPRETATIONS = "Interpretations"
INTERPRETED_CONDITION = "InterpretedCondition"
INTERPRETED_CONDITION_LIST = "InterpretedConditionList"
INTERPRETED_RECORD = "InterpretedRecord"
LOCATION = "Location"
MAPPING_REF = "MappingRef"
MAPPING_VALUE = "MappingValue"
MED_GEN = "MedGen"
NAME = "Name"
OBSERVED_IN = "ObservedIn"
OBSERVED_IN_LIST = "ObservedInList"
ONCOGENICITY_CLASSIFICATION = "OncogenicityClassification"
ORIGIN = "Origin"
PREFERRED = "Preferred"
PROTEIN_CHANGE = "ProteinChange"
RCV_ACCESSION = "RCVAccession"
RCV_CLASSIFICATIONS = "RCVClassifications"
RCV_LIST = "RCVList"
REVIEW_STATUS = "ReviewStatus"
SAMPLE = "Sample"
SEQUENCE_LOCATION = "SequenceLocation"
SIMPLE_ALLELE = "SimpleAllele"
SOMATIC_CLINICAL_IMPACT = "SomaticClinicalImpact"
SUBMITTER_NAME = "SubmitterName"
TRAIT = "Trait"
TRAIT_MAPPING = "TraitMapping"
TRAIT_MAPPING_LIST = "TraitMappingList"
TRAIT_SET = "TraitSet"
VARIATION_ARCHIVE = "VariationArchive"
VARIATION_ID = "VariationID"
VARIATION_TYPE = "VariationType"
XREF_LIST = "XRefList"
XREF = "XRef"


@curry
class ClinvarXMLSource(LazyFileSource):
    def __init__(self, file_path, is_grch38=False, **kwargs):
        self.file_path = file_path
        self.is_grch38 = is_grch38

    def __iter__(self):
        return self.parse_clinvar_xml()

    def create_combined_xref(self, interpreted_record):
        total_xref_val = []
        try:
            xrefs = (
                interpreted_record.find(SIMPLE_ALLELE)
                .find(XREF_LIST)
                .findall(XREF)
            )
            for xref in xrefs:
                db_vals = [xref.attrib.get("DB"), xref.attrib.get("Type")]
                db_str = (
                    "_".join(db_vals) if db_vals[1] is not None else db_vals[0]
                )
                total_xref_val.append(f"{db_str}:{xref.attrib.get('ID')}")
            return "|".join(total_xref_val)
        except Exception:
            return None

    def get_origin_vals_list(self, clinical_assertion):
        return [
            oi.find(SAMPLE).find(ORIGIN).text
            for oi in clinical_assertion.find(OBSERVED_IN_LIST).findall(
                OBSERVED_IN
            )
        ]

    def get_submission_conditions(
            self, clinical_assertion, classified_record
    ):
        try:
            all_trait_mappings = classified_record.find(
                TRAIT_MAPPING_LIST
            ).findall(TRAIT_MAPPING)
            conditions = self.get_conditions_from_trait_mapping(
                clinical_assertion, all_trait_mappings
            )
        except Exception:
            conditions = self.get_conditions_from_traitset(clinical_assertion)
        return conditions

    def get_conditions_from_trait_mapping(self, assertion, all_trait_mappings):
        assertion_id = assertion.attrib.get(ID)
        conditions = []
        for trait_mapping in all_trait_mappings:
            has_assertion = (
                trait_mapping.attrib.get(CLINICAL_ASSERTION_ID) == assertion_id
            )
            is_preferred = (
                trait_mapping.attrib.get(MAPPING_REF, False) == PREFERRED
            )
            if has_assertion and not is_preferred:
                conditions.append(trait_mapping.find(MED_GEN).attrib.get(NAME))
            elif has_assertion and is_preferred:
                conditions.append(trait_mapping.attrib.get(MAPPING_VALUE))
        # if an assertion has multiple diseases associated,
        # we went them as a comma seperated string.
        if len(conditions) > 1:
            conditions = [", ".join(conditions)]
        return conditions

    def get_conditions_from_traitset(self, clinical_assertion):
        try:
            element_values = (
                clinical_assertion.find(TRAIT_SET)
                .find(TRAIT)
                .find(NAME)
                .findall(ELEMENT_VALUE)
            )
        except Exception:
            return None
        if len(element_values) > 1:
            conditions = [
                e.text
                for e in element_values
                if e.attrib.get("Type") == "Preferred"
            ]
        else:
            conditions = [element_values[0].text]
        conditions = self.clean_string_list(conditions)
        return conditions

    def get_classified_conditions(self, rcv_accessions, condition):
        classified_conditions = []
        for rcva in rcv_accessions:
            if (rcvClassifications := rcva.find(RCV_CLASSIFICATIONS)) is not None:
                if rcvClassifications.find(condition) is not None:
                    conditions = rcva.find(CLASSIFIED_CONDITION_LIST).findall(
                        CLASSIFIED_CONDITION
                    )
                    if len(conditions) > 1:
                        multiple_conditions = [
                            condition.text for condition in conditions
                        ]
                        classified_conditions.append(", ".join(multiple_conditions))
                    else:
                        classified_conditions.extend(conditions)
        return self.clean_string_list(classified_conditions)

    def clean_string_list(self, value_list):
        result = []
        for value in value_list:
            if isinstance(value, etree.Element):
                words = (
                    value.text.replace("\r", "").replace("\n", "").split(" ")
                )
            else:
                words = value.replace("\r", "").replace("\n", "").split(" ")
            result.append(" ".join([w for w in words if len(w) > 0]))
        return result

    def get_alteration_string(self, interpreted_record):
        try:
            protein_change = (
                interpreted_record.find(SIMPLE_ALLELE)
                .find(PROTEIN_CHANGE)
                .text
            )
        except Exception:
            protein_change = None
        genes, is_submitted = self.get_genes(interpreted_record)
        if len(genes) > 0 and is_submitted and protein_change:
            gene_name = genes[0]
            return f"{gene_name} {protein_change}"
        else:
            return None

    def get_genes(self, interpreted_record):
        """
        Returns list of gene names and
        whether the gene was submitted or not.
        """
        try:
            genes = (
                interpreted_record.find(SIMPLE_ALLELE)
                .find(GENE_LIST)
                .findall(GENE)
            )
            for gene in genes:
                if gene.attrib.get("Source") == "submitted":
                    return [gene.attrib.get("Symbol")], True
            return [g.attrib.get("Symbol") for g in genes], False
        except Exception:
            return [], False

    def get_assembly(self):
        return GRCH_38 if self.is_grch38 else GRCH_37

    def create_csra(self, interpreted_record, assembly_name=None):
        try:
            sequence_locations = (
                interpreted_record.find(SIMPLE_ALLELE)
                .find(LOCATION)
                .findall(SEQUENCE_LOCATION)
            )
            if sequence_locations:

                valid_sequence_locations = [
                    sl
                    for sl in sequence_locations
                    if sl.attrib.get(ASSEMBLY) == assembly_name
                ]
                for sl in valid_sequence_locations:
                    chr, pos = (
                        sl.attrib.get("Chr"),
                        sl.attrib.get("positionVCF"),
                    )
                    ref, alt = (
                        sl.attrib.get("referenceAlleleVCF"),
                        sl.attrib.get("alternateAlleleVCF"),
                    )
                    if ref == alt or not all([chr, pos, ref, alt]):
                        return None
                    else:
                        return f"chr{chr}|{pos}|{ref}|{alt}|{assembly_name}"
            else:
                return None
        except Exception:
            return None

    def get_description(self, element):
        result = []
        for elem in element:
            result = [
                i.strip()
                for i in re.split(
                    "[,;]", elem.find(DESCRIPTION).text
                )
            ]
        return result

    def get_somatic_review_status(self, somatic_clinical_impacts):
        if somatic_clinical_impacts is not None:
            for sci in somatic_clinical_impacts:
                return [sci.find(REVIEW_STATUS).text]
        return None

    def iterate_individual_submissions(self, clinical_assertions, record, classified_record):  # noqa: E501
        submission_origins = None
        submission_conditions = None
        record["all_submission_interpretations__mstring"] = []
        record["all_submission_review_statuses__mstring"] = []
        record["all_submission_conditions__mstring"] = []
        record["all_submission_submitter__mstring"] = []
        record["all_submission_origin__mstring"] = []
        # somatic submissions
        record["somatic_all_submissions_interpretations__mstring"] = []
        record["somatic_all_submission_review_statuses__mstring"] = []
        record["somatic_all_submission_submitter__mstring"] = []
        record["somatic_all_submission_conditions__mstring"] = []
        record["somatic_all_submission_origin__mstring"] = []

        # oncogenicity submissions
        record["oncogenicity_all_submission_origin__mstring"] = []
        record["oncogenicity_all_submission_review_statuses__mstring"] = []
        record["oncogenicity_all_submission_conditions__mstring"] = []
        record["oncogenicity_all_submission_submitter__mstring"] = []

        for clinical_assertion in clinical_assertions:
            if (classification := clinical_assertion.find(CLASSIFICATION)) is not None:
                if (germline_classification := classification.find(
                        GERMLINE_CLASSIFICATION)) is not None:
                    record["all_submission_interpretations__mstring"].append(
                        germline_classification.text)
                    if (review_status := classification.find(
                            REVIEW_STATUS).text) is not None:
                        record["all_submission_review_statuses__mstring"].append(
                            review_status)

                    submission_origins = (
                        clinical_assertion.find(OBSERVED_IN_LIST)
                        .find(OBSERVED_IN)
                        .find(SAMPLE)
                        .find(ORIGIN)
                        .text
                    )

                    if (clinvar_accession := clinical_assertion.find(
                            CLINVAR_ACCESSION)) is not None:
                        if (submitter_name := clinvar_accession.attrib.get(
                                SUBMITTER_NAME)) is not None:
                            record["all_submission_submitter__mstring"].append(
                                submitter_name)

                    submission_conditions = self.get_submission_conditions(
                        clinical_assertion, classified_record
                    )
                # get somatic submissions
                if (somatic_clinical_impact := classification.find(
                        SOMATIC_CLINICAL_IMPACT)) is not None:
                    clinical_impact_assertion_type = somatic_clinical_impact.attrib.get(
                        CLINICAL_IMPACT_ASSERTION_TYPE)
                    clinical_impact_clinical_significance = (
                        somatic_clinical_impact.attrib.get(
                            CLINICAL_IMPACT_CLINICAL_SIGNIFICANCE))
                    somatic_description = somatic_clinical_impact.text
                    record["somatic_all_submissions_interpretations__mstring"].append(
                        f"{somatic_description}, "
                        f"{clinical_impact_clinical_significance}, "
                        f"{clinical_impact_assertion_type}")

                    if (somatic_review_status := classification.find(
                            REVIEW_STATUS)) is not None:
                        record[
                            "somatic_all_submission_review_statuses__mstring"].append(
                            somatic_review_status.text)

                    if (clinvar_accession := clinical_assertion.find(
                            CLINVAR_ACCESSION)) is not None:
                        if (submitter_name := clinvar_accession.attrib.get(
                                SUBMITTER_NAME)) is not None:
                            record["somatic_all_submission_submitter__mstring"].append(
                                submitter_name)

                    if (
                    somatic_all_submission_conditions := self.get_submission_conditions(
                            clinical_assertion, classified_record
                    )) is not None:
                        record["somatic_all_submission_conditions__mstring"].extend(
                            somatic_all_submission_conditions)

                    if (somatic_submission_origins := (
                            clinical_assertion.find(OBSERVED_IN_LIST)
                                    .find(OBSERVED_IN)
                                    .find(SAMPLE)
                                    .find(ORIGIN)
                                    .text
                    )) is not None:
                        record["somatic_all_submission_origin__mstring"].append(
                            somatic_submission_origins)

                # get oncogenicity submissions
                if (oncogenicity_classifications := classification.find(
                        ONCOGENICITY_CLASSIFICATION)) is not None:
                    record["oncogenicity_all_submissions_interpretations__mstring"] = [
                        oncogenicity_classifications.text]
                    if (oncogenicity_review_status := classification.find(
                            REVIEW_STATUS)) is not None:
                        record["oncogenicity_all_submission_origin__mstring"].append(
                            oncogenicity_review_status.text)
                    if (oncogenicity_review_status := classification.find(
                            REVIEW_STATUS).text) is not None:
                        record[
                            "oncogenicity_all_submission_review_statuses__mstring"].append(
                            oncogenicity_review_status)

                    if (oncogenicity_all_submission_conditions := self.get_submission_conditions(
                            clinical_assertion, classified_record
                    )) is not None:
                        record["oncogenicity_all_submission_conditions__mstring"].extend(
                            oncogenicity_all_submission_conditions)

                    if (oncogenicity_submission_origins := (
                        clinical_assertion.find(OBSERVED_IN_LIST)
                        .find(OBSERVED_IN)
                        .find(SAMPLE)
                        .find(ORIGIN)
                        .text
                    )) is not None:
                        record["oncogenicity_all_submission_submitter__mstring"].append(oncogenicity_submission_origins)

            if submission_conditions is not None:
                record["all_submission_conditions__mstring"].extend(
                    submission_conditions
                )

            if submission_origins is not None:
                record["all_submission_origin__mstring"].append(
                    submission_origins
                )

        return record

    def should_parse_varchive(self, varchive):
        classified_record = varchive.find(CLASSIFIED_RECORD)
        hgvs_g = self.create_csra(classified_record, self.get_assembly())
        is_missing_hgvs_and_alteration = (
            hgvs_g is None
            and self.get_alteration_string(classified_record) is None
        )
        if (
                varchive.attrib.get(VARIATION_TYPE) in VARIANT_TYPE_BLACKLIST
                or varchive.find(INCLUDED_RECORD)
                or is_missing_hgvs_and_alteration
        ):
            return False
        else:
            return True

    def var_archive_parse(self, variation_archive):  # pragma: no mccabe
        # common tree elements
        classified_record = variation_archive.find(CLASSIFIED_RECORD)
        germline_classifications = classified_record.find(CLASSIFICATIONS).findall(
            GERMLINE_CLASSIFICATION
        )
        somatic_clinical_impacts = classified_record.find(CLASSIFICATIONS).findall(SOMATIC_CLINICAL_IMPACT)
        oncogenicity_classifications = classified_record.find(CLASSIFICATIONS).findall(ONCOGENICITY_CLASSIFICATION)
        clinical_assertions = classified_record.find(
            CLINICAL_ASSERTION_LIST
        ).findall(CLINICAL_ASSERTION)
        rcv_accessions = classified_record.find(RCV_LIST).findall(
            RCV_ACCESSION
        )

        # values
        clinsig = self.get_description(germline_classifications)
        variation_id = variation_archive.attrib.get(VARIATION_ID)
        review_statuses = germline_classifications[0].find("ReviewStatus").text
        clnvi = [self.create_combined_xref(classified_record)]
        clndn = self.get_classified_conditions(rcv_accessions, GERMLINE_CLASSIFICATION)
        csra = self.create_csra(classified_record, self.get_assembly())
        grch38_csra = self.create_csra(classified_record, GRCH_38)
        hgvs_g = csra
        csra_array = csra.split("|") if csra else []
        chromosome = None
        position = None
        if len(csra_array) > 1:
            chromosome = csra_array[0].replace("chr", "")
            position = csra_array[1]
        genes, _ = self.get_genes(classified_record)
        accession = variation_archive.attrib.get(ACCESSION)
        # somatic impact fields
        somatic_impact_description = self.get_description(somatic_clinical_impacts)
        somatic_review_status = self.get_somatic_review_status(somatic_clinical_impacts)
        somatic_conditions = self.get_classified_conditions(rcv_accessions, SOMATIC_CLINICAL_IMPACT)

        # oncogenicity fields
        oncogenicity_description = self.get_description(oncogenicity_classifications)
        oncogenicity_review_status = self.get_somatic_review_status(
            oncogenicity_classifications)
        oncogenicity_conditions = self.get_classified_conditions(rcv_accessions,
                                                                 ONCOGENICITY_CLASSIFICATION)

        # build top-level result dict with fields that could be parsed
        record = {}
        if clinsig is not None:
            record["CLNSIG__mstring"] = clinsig
        if variation_id is not None:
            record["variant_ID__string"] = variation_id
        if review_statuses is not None:
            record["CLNREVSTAT__mstring"] = review_statuses
        if clnvi is not None:
            record["CLNVI__mstring"] = clnvi
        if clndn is not None:
            record["CLNDN__mstring"] = clndn
        if hgvs_g:
            record["hgvs_g"] = hgvs_g
        if chromosome:
            record["chr"] = chromosome
        if position:
            record["position"] = position
        if len(genes) > 0:
            record["gene"] = genes
        if accession is not None:
            record["accession__string"] = accession
        record["csra"] = csra
        record["grch38_csra"] = grch38_csra

        # get all submissions for all classifications
        record = self.iterate_individual_submissions(
            clinical_assertions, record, classified_record
        )
        # somatic top level fields
        if somatic_impact_description is not None:
            record["somatic_impact__mstring"] = somatic_impact_description
        if somatic_review_status is not None:
            record["SOMREVSTAT__mstring"] = somatic_review_status
        if somatic_conditions is not None:
            record["SOMDN__mstring"] = somatic_conditions

        # oncogenicity top level fields
        if oncogenicity_description is not None:
            record["oncogenicity__mstring"] = oncogenicity_description
        if oncogenicity_review_status is not None:
            record["ONCREVSTAT__mstring"] = oncogenicity_review_status
        if oncogenicity_conditions is not None:
            record["ONCDN__mstring"] = oncogenicity_conditions

        return record

    def determine_and_parse_record(self, variation_archive):
        if self.should_parse_varchive(variation_archive):
            return self.var_archive_parse(variation_archive)
        else:
            return None

    def parse_clinvar_xml(self):  # pragma: no mccabe
        parse_error_var_ids = []
        try:
            for event, elem in etree.iterparse(
                    self.file_path, events=("start", "end")
            ):
                if event == "end" and elem.tag == VARIATION_ARCHIVE:
                    if self.should_parse_varchive(elem):
                        try:
                            yield self.var_archive_parse(elem)
                            elem.clear()
                        except Exception:
                            parse_error_var_ids.append(
                                elem.attrib.get(VARIATION_ID)
                            )
                    else:
                        elem.clear()
                        continue
                else:
                    continue
            if len(parse_error_var_ids) > 0:
                print(
                    "\n\nHere are the variation ids of "
                    "records in which a parsing error occurred..."
                )
                for id in parse_error_var_ids:
                    print(f"{id}\n")

        except etree.ParseError:
            print("Parse error. Check the format of your file.")
            exit()

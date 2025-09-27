from .base import Source, JsonlFileSource, TextFileSource, NullSource
from .bed import BedFileSource
from .delimited import DelimitedFileSource
from .paths import CollectFilePathsSource
from .excel import ExcelSource
from .aggregated import (
    AggregatedCOSMICSources,
    AggregatedFileSource,
    AggregatedGenieSNVFileSource,
    AggregatedGenieCNVFileSource,
    AggregatedGenieCTXFileSource,
    AggregatedOmimFileSource,
    AggregatedCOSMICNonSNVSources,
    AggregatedGenieGenes,
    AggregateHpoJson,
    ParseGenomenonJson
)
from .maf import MAFSource
from .xml import XMLSource
from . import one_off_sources
from .annotations_filter import AnnotationsFilterFileSource

__all__ = (
    "Source",
    "BedFileSource",
    "JsonlFileSource",
    "TextFileSource",
    "NullSource",
    "DelimitedFileSource",
    "CollectFilePathsSource",
    "ExcelSource",
    "AggregatedCOSMICSources",
    "AggregatedCOSMICNonSNVSources",
    "AggregatedFileSource",
    "AggregatedGenieSNVFileSource",
    "AggregatedGenieCNVFileSource",
    "AggregatedGenieCTXFileSource",
    "MAFSource",
    "XMLSource",
    "AnnotationsFilterFileSource",
    "AggregatedOmimFileSource",
    "AggregatedGenieGenes",
    "AggregateHpoJson",
    "ParseGenomenonJson"
)


def get_one_off_source(source_name):
    return one_off_sources.source_name_map.get(source_name)

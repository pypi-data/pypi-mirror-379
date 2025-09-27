from tidytcells._standardized_gene_symbol.standardized_ig_symbol import (
    StandardizedIgSymbol,
)
from tidytcells._resources import VALID_HOMOSAPIENS_IG, HOMOSAPIENS_IG_SYNONYMS


class StandardizedHomoSapiensIgSymbol(StandardizedIgSymbol):
    _synonym_dictionary = HOMOSAPIENS_IG_SYNONYMS
    _valid_ig_dictionary = VALID_HOMOSAPIENS_IG

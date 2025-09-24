from __future__ import annotations
from rbceq2.core_logic.constants import AlleleState

from rbceq2.core_logic.alleles import Allele, BloodGroup, Pair
from rbceq2.core_logic.utils import Zygosity

from icecream import ic

def flatten_alleles(pairs: list[Pair]) -> set[Allele]:
    """Flatten the pairs into a set of alleles.

    Args:
        pairs (list[Pair]): A list of Pair objects, where each Pair is an
            iterable containing Allele objects.

    Returns:
        set[Allele]: A set containing all Allele objects from the given pairs.
    """
    return {allele for pair in pairs for allele in pair}


def all_hom(variant_pool: dict[str, str], current_allele: Allele) -> bool:
    """if > 1 het vars in an alleles defiing variant set, this shouldnt apply
    unless phased, which is handled elsewhere - TODO ensure its handled elsewhere"""

    return all(
        variant_pool.get(allele_var) == Zygosity.HOM
        for allele_var in current_allele.defining_variants
    )


def identify_unphased(bg: BloodGroup, alleles: list[Allele]) -> list[Allele]:
    '''
    logic to check if an alleles varaints are in phase or not'''
    def get_var_phase_info(current_var):
        return bg.variant_pool_phase[current_var], bg.variant_pool_phase_set[current_var]
    
    def variant_not_phased(current_phase):
        return '/' in current_phase
    
    def variant_not_HET(current_var):
        return bg.variant_pool.get(current_var) != Zygosity.HET
    
    
    to_remove = []
    for allele in alleles:
        allele_added = False
        for variant in allele.defining_variants:
            if variant_not_HET(variant):
                continue
            phase, phase_set = get_var_phase_info(variant)
            if variant_not_phased(phase):
                continue
            for variant2 in allele.defining_variants:
                if variant == variant2:
                    continue
                if variant_not_HET(variant2):
                    continue
                phase2, phase_set2 = get_var_phase_info(variant2)
                if variant_not_phased(phase2):
                    continue
                if phase_set == phase_set2 and phase != phase2:
                    to_remove.append(allele)
                    allele_added = True
                    break
            if allele_added:
                break
        if allele_added:
            continue
    return to_remove


def proceed(bg: BloodGroup, allele_state: AlleleState) -> bool:
    '''Some filter functions iterate over AlleleStates
    ie for allele_state in [AlleleState.NORMAL, AlleleState.CO]:
    
    if CO, we only want to process knops and then only if there are 
    instances of co_exsisting alleles'''

    if allele_state != AlleleState.CO:
        return True
    if bg.type != "KN" or bg.alleles[allele_state] is None:
        return False
    return True

def check_var(bg: BloodGroup, pair: Pair, allele_state: AlleleState, variant: str) -> int:
    '''checks that HET vars are used'''
    allele1_vars_plus_het_var = set(pair.allele1.defining_variants) | {
        variant
    }
    allele2_vars_plus_het_var = set(pair.allele2.defining_variants) | {
        variant
    }
    flattened = {
        allele
        for pair2 in bg.alleles[allele_state]
        for allele in pair2
        if pair2 != pair
    }
    hits = 0
    for a in flattened:
        if a not in pair:
            flat_vars = set(a.defining_variants)
            if (
                flat_vars == allele1_vars_plus_het_var
                or flat_vars == allele2_vars_plus_het_var
            ):
                hits += 1
    return hits
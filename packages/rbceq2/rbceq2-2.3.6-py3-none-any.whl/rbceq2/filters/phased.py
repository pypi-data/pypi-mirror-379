from __future__ import annotations

from functools import partial
from collections.abc import Callable
from rbceq2.core_logic.alleles import BloodGroup, Pair
from rbceq2.core_logic.constants import AlleleState
from rbceq2.core_logic.utils import (
    Zygosity,
    apply_to_dict_values,
)
from rbceq2.filters.shared_filter_functionality import (
    flatten_alleles,
    all_hom,
    identify_unphased,
    proceed,
)
from rbceq2.core_logic.alleles import Allele


@apply_to_dict_values
def remove_unphased(bg: BloodGroup, phased: bool) -> BloodGroup:
    """Remove unphased alleles from the BloodGroup's FILT state if phased flag is set.

    This function iterates through the alleles in the FILT state and checks their
    phasing. Alleles with more than two distinct phases trigger a warning. If an
    allele has exactly two phases and no placeholder ('.') is present, it is marked
    for removal. Alleles with a single phase remain, as they are assumed to align
    with the reference.

    Args:
        bg (BloodGroup): A BloodGroup object containing allele states and phasing
            information.
        phased (bool): A flag indicating whether phasing should be enforced.

    Returns:
        BloodGroup: The updated BloodGroup with improperly phased alleles removed.

    #Example:
    Genotypes count: 1
    Genotypes: JK*01W.06/JK*02
    Phenotypes (numeric): JK:1w,2
    Phenotypes (alphanumeric): Jk(a+wb+)

    #Data:
    Vars:
    18:45739554_ref : Heterozygous
    18:45730450_G_A : Heterozygous
    18:45736573_A_G : Homozygous
    18:45739554_G_A : Heterozygous
    Vars_phase:
    18:45739554_ref : 1|0
    18:45730450_G_A : 1|0
    18:45736573_A_G : 1/1
    18:45739554_G_A : 0|1
    Vars_phase_set:
    18:45739554_ref : 20911244
    18:45730450_G_A : 20911244
    18:45736573_A_G : .
    18:45739554_G_A : 20911244


    #Filters applied:
    remove_unphased:
     Vars_phase:
    18:45739554_ref : 1|0
    18:45730450_G_A : 1|0
    18:45736573_A_G : 1/1
    18:45739554_G_A : 0|1
    Allele
    genotype: JK*02W.03
    defining_variants:
            18:45736573_A_G 1/1
            18:45730450_G_A 1|0
            18:45739554_G_A 0|1
    weight_geno: 1000
    phenotype: JK:-1,2w or Jk(a-),Jk(b+w)
    reference: False

    Allele
    genotype: JK*02W.04
    defining_variants:
            18:45730450_G_A 1|0
            18:45739554_G_A 0|1
    weight_geno: 1000
    phenotype: JK:-1,2w or Jk(a-),Jk(b+w)
    reference: False
    """

    if not phased:
        return bg

    to_remove = identify_unphased(bg, bg.alleles[AlleleState.FILT])
    if to_remove:
        bg.remove_alleles(to_remove, "remove_unphased", AlleleState.FILT)
    return bg


def _get_allele_phase_info(allele, phase_dict):
    """ """
    return [phase_dict[variant] for variant in allele.defining_variants]


@apply_to_dict_values
def filter_if_all_HET_vars_on_same_side_and_phased(
    bg: BloodGroup, phased: bool
) -> BloodGroup:
    """
    All HET vars on same side so can only have ref/HOMs on other side

    Example
    Sample: GM18501 BG Name: GYPB

    #Results:
        Genotypes count: 3
        Genotypes:
        GYPB*03/GYPB*03.06
        GYPB*03/GYPB*06.02
        GYPB*03.06/GYPB*06.02 # not possible
        Phenotypes (numeric): MNS:3,-4 | MNS:3,-4,6
        Phenotypes (alphanumeric): S+,s- | S+,s-,He+

    #Data:
    Vars:
    4:143999443_G_A : Homozygous
    4:143997537_C_T : Heterozygous
    4:144001261_T_C : Heterozygous
    4:144001254_T_A : Heterozygous
    4:144001262_A_C : Heterozygous
    4:144001249_C_A : Heterozygous
    4:144001250_T_C : Heterozygous
    Vars_phase:
    4:143999443_G_A : 1/1
    4:143997537_C_T : 0|1
    4:144001261_T_C : 0|1
    4:144001254_T_A : 0|1
    4:144001262_A_C : 0|1
    4:144001249_C_A : 0|1
    4:144001250_T_C : 0|1
    Vars_phase_set:
    4:143999443_G_A : .
    4:143997537_C_T : 129362934
    4:144001261_T_C : 129362934
    4:144001254_T_A : 129362934
    4:144001262_A_C : 129362934
    4:144001249_C_A : 129362934
    4:144001250_T_C : 129362934
    Raw:
    Allele
    genotype: GYPB*03
    defining_variants:
            4:143999443_G_A #hom
    weight_geno: 1000
    phenotype: MNS:3,-4 or S+,s-
    reference: False

    Allele
    genotype: GYPB*03.06
    defining_variants:
            4:143997537_C_T #this is on same side as
            4:143999443_G_A #hom
    weight_geno: 1000
    phenotype: MNS:3,-4 or S+,s-
    reference: False

    Allele
    genotype: GYPB*06.02
    defining_variants:
            4:144001250_T_C #all these, so cant be opposite
            4:144001249_C_A
            4:143999443_G_A #hom
            4:144001261_T_C
            4:144001262_A_C
            4:144001254_T_A
    weight_geno: 1000
    phenotype: MNS:3,-4,6 or S+,s-,He+
    reference: False

    """

    if not phased:
        return bg

    for allele_state in [AlleleState.NORMAL, AlleleState.CO]:
        if not proceed(bg, allele_state):
            continue
        to_remove = []
        for pair in bg.alleles[allele_state]:
            for variant in pair.allele1.defining_variants:
                if bg.variant_pool.get(variant) != Zygosity.HET:
                    continue
                phase = bg.variant_pool_phase[variant]
                for variant2 in pair.allele2.defining_variants:
                    if bg.variant_pool.get(variant2) != Zygosity.HET:
                        continue
                    phase2 = bg.variant_pool_phase[variant2]
                    if phase == phase2 and "|" in phase:
                        to_remove.append(pair)
        if to_remove:
            bg.remove_pairs(
                to_remove,
                "filter_if_all_HET_vars_on_same_side_and_phased",
                allele_state,
            )

    return bg


@apply_to_dict_values
def filter_on_in_relationship_if_HET_vars_on_dif_side_and_phased(
    bg: BloodGroup, phased: bool
) -> BloodGroup:
    """
    If an allele is HOM and it's 'in' every other properly phased allele
    AND the there's at least 1 of those on each side, it can't exist

    Sample: HG03774 BG Name: LU

    #Results:
    Genotypes count: 3
    Genotypes:
    LU*02.-13/LU*02.19
    LU*02/LU*02.-13 #not possible, HET SNPs on opposite sides so LU*02 'in'
    LU*02/LU*02.19  #not possible, HET SNPs on opposite sides
    Phenotypes (numeric): LU:-1,2,13 | LU:-1,2,13,18,19 | LU:-1,2,18,19
    Phenotypes (alphanumeric): Lu(a-b+),Au(a+b+) | Lu(a-b+),Au(a+b+),Lu13+ | Lu(a-b+),Lu13+

    #Data:

    Vars:
    19:44812188_ref : Homozygous
    19:44819059_C_T : Heterozygous
    19:44819705_A_T : Heterozygous
    19:44819634_C_T : Heterozygous
    19:44819487_A_G : Heterozygous
    Vars_phase:
    19:44812188_ref : 1/1
    19:44819059_C_T : 1|0
    19:44819705_A_T : 1|0
    19:44819634_C_T : 1|0
    19:44819487_A_G : 0|1
    Vars_phase_set:
    19:44812188_ref : .
    19:44819059_C_T : 43975436
    19:44819705_A_T : 43975436
    19:44819634_C_T : 43975436
    19:44819487_A_G : 43975436

    Raw:
    Allele
    genotype: LU*02
    defining_variants:
            19:44812188_ref
    weight_geno: 1000
    phenotype: LU:-1,2 or Lu(a-),Lu(b+)
    reference: True

    Allele
    genotype: LU*02.-13
    defining_variants:
            19:44812188_ref
            19:44819634_C_T #1|0
            19:44819705_A_T #1|0
            19:44819059_C_T #1|0
    weight_geno: 1000
    phenotype: LU:-1,2,-13 or Lu(a-),Lu(b+),Lu13-
    reference: False

    Allele
    genotype: LU*02.19
    defining_variants:
            19:44812188_ref
            19:44819487_A_G #0|1
    weight_geno: 1000
    phenotype: LU:-1,2,-18,19 or Lu(a-),Lu(b+),Au(a-),Au(b+)
    reference: False
    """

    # If an allele is HOM and it's 'in' every other properly phased allele
    # AND the there's at least 1 of those on each side, it can't exist
    def find_phase(allele: Allele) -> set[str | None]:
        """find phase"""
        return set(
            [
                bg.variant_pool_phase.get(variant)
                for variant in allele.defining_variants
                if bg.variant_pool_phase.get(variant) not in ["1/1", "0/1", "1/0"]
            ]
        )

    def allele_phased(allele: Allele, phase_dict: dict[str, str]) -> bool:
        """check if alleles phase sets are the same, if not can't be phased"""
        phase_sets = [
            phase_dict.get(variant, "None") for variant in allele.defining_variants
        ]
        return (
            len(set([phase_set for phase_set in phase_sets if phase_set.isdigit()]))
            == 1
        )

    if not phased:
        return bg
    for allele_state in [AlleleState.NORMAL, AlleleState.CO]:
        if not proceed(bg, allele_state):
            continue
        to_remove = []
        pair_with_unphased_HETs = False
        for pair in bg.alleles[allele_state]:
            if not allele_phased(pair.allele1, bg.variant_pool_phase_set):
                continue  # TODO - next refactor this type of functionality
            # should move into a new PhasedAllele class
            if not allele_phased(pair.allele2, bg.variant_pool_phase_set):
                continue
            phase1 = find_phase(pair.allele1)
            phase2 = find_phase(pair.allele2)
            assert len(phase1) < 2
            assert len(phase2) < 2

            if phase1 == {None} or phase2 == {None}:
                continue
            if phase1 == {"unknown"} or phase2 == {"unknown"}:
                continue
            if len(phase1) == 1 and len(phase2) == 1:
                assert phase1.union(phase2) == {"1|0", "0|1"}
                pair_with_unphased_HETs = True
                break
        if pair_with_unphased_HETs:
            flattened_alleles = flatten_alleles(bg.alleles[allele_state])
            for pair in bg.alleles[allele_state]:
                for allele in pair:
                    if all_hom(bg.variant_pool, allele) and any(
                        allele in flat_allele for flat_allele in flattened_alleles
                    ):
                        to_remove.append(pair)

        if to_remove:
            bg.remove_pairs(
                to_remove,
                "filter_on_in_relationship_if_HET_vars_on_dif_side_and_phased",
                allele_state,
            )

    return bg


@apply_to_dict_values
def filter_pairs_by_phase(
    bg: BloodGroup, phased: bool, reference_alleles
) -> BloodGroup:
    """
    Filters out allele pairs where both alleles are in the same phase.

    This function is intended to remove allele pairs from a BloodGroup object when both
    alleles in a pair are in the same phase, indicating they are on the same
    chromosome and cannot be inherited together. The function operates under the
    following logic:

    - If `phased` is False, the function returns the BloodGroup object unchanged.
    - For each allele pair in `bg.alleles[AlleleState.NORMAL]`:
        - If the pair contains a reference allele, it is retained.
        - Extract the phase sets (`p1` and `p2`) for each allele in the pair.
        - If both alleles are homozygous (phase sets are {"."}), the pair is retained.
        - If the phase sets are identical, the pair is removed.
        - If the non-homozygous phase sets differ, the pair is retained.
        - If the non-homozygous phase sets are identical, the pair is removed.
        - If none of the above conditions are met, a ValueError is raised.

    - If all pairs are removed and there were pairs with phase information, new pairs
    are created by pairing each allele with the reference allele for the blood group
    type.

    Args:
        bg (BloodGroup): The BloodGroup object containing allele pairs.
        phased (bool): A flag indicating whether phase information is available.
        reference_alleles (dict): A dictionary mapping blood group types to reference
        alleles.

    Returns:
        BloodGroup: The updated BloodGroup object with inconsistent allele pairs removed.


    Example:
    ----------
    Suppose you have allele pairs where both alleles are on the same phase strand.
    This function will remove such pairs, ensuring that only valid allele combinations
    are retained. If all pairs are removed and phase information is present, it will
    create new pairs with the reference allele to represent possible allele
    combinations.


    Meant to remove pairs where both alleles are on the same strand ie
    to_remove: [[Allele(genotype='FUT2*01N.16',
                        defining_variants=frozenset({'19:48703728_G_A'}),
                        weight_geno=8,
                        weight_pheno=5,
                        reference=False,
                        sub_type='FUT2*01',
                        phase=0|1),
                 Allele(genotype='FUT2*01N.02',
                        defining_variants=frozenset({'19:48703417_G_A'}),
                        weight_geno=1,
                        weight_pheno=5,
                        reference=False,
                        sub_type='FUT2*01',
                        phase=0|1)]]

    dont remove if ref in pair
    if there is only 1 pair and they are phased then change to 2 pairs (or &) with ref
    """

    if not phased:
        return bg
    to_remove = []
    for pair in bg.alleles[AlleleState.NORMAL]:
        if pair.contains_reference:
            continue
        p1_phases = set(_get_allele_phase_info(pair.allele1, bg.variant_pool_phase))
        p1_zygo = set(_get_allele_phase_info(pair.allele1, bg.variant_pool))
        p1_phase_sets = set(
            _get_allele_phase_info(pair.allele1, bg.variant_pool_phase_set)
        )
        p2_phases = set(_get_allele_phase_info(pair.allele2, bg.variant_pool_phase))
        p2_zygo = set(_get_allele_phase_info(pair.allele2, bg.variant_pool))
        p2_phase_sets = set(
            _get_allele_phase_info(pair.allele2, bg.variant_pool_phase_set)
        )

        phase_set = p1_phase_sets.union(p2_phase_sets)
        if len(phase_set) != 1:
            continue  # can't use phasing info

        if p1_zygo == {Zygosity.HOM} and p2_zygo == {Zygosity.HOM}:  # all hom
            continue
        elif p1_phases == p2_phases:
            to_remove.append(pair)
    if len(bg.alleles[AlleleState.NORMAL]) == len(to_remove):
        for pair in to_remove:
            bg.alleles[AlleleState.NORMAL].append(
                Pair(reference_alleles[bg.type], pair.allele1)
            )
            bg.alleles[AlleleState.NORMAL].append(
                Pair(reference_alleles[bg.type], pair.allele2)
            )
    if to_remove:
        bg.remove_pairs(to_remove, "filter_pairs_by_phase")

    return bg


@apply_to_dict_values
def impossible_alleles_phased(bg: BloodGroup, phased: bool) -> BloodGroup:
    """
    Filters alleles in a BloodGroup object based on phasing consistency and subsumption.

    When `phased` is True, this function attempts to simplify the set of possible
    alleles (`bg.alleles[AlleleState.]`) by looking for alleles that are impossibe
    due to being 'in' (defining variants are subset of) another allele:
        1. A1 is A2, all vars HOM (should be removed above - not phased dependant)
        2. A1 is A2, all vars HET and in same phase
        2. A1 is A2, vars are mix of HET and HOM, all HET are in same phase


    The function modifies `bg.alleles[AlleleState.]` in-place by removing the
    alleles deemed "impossible" under these phased conditions. Details of removed
    allele pairs due to subsumption are stored in
    `bg.filtered_out["allele_subsumed_by_other_phased"]`.

    Args:
        bg (BloodGroup): A BloodGroup object containing allele states, variant pool
            (with observed zygosities), and phasing information within Allele objects.
        phased (bool): A flag indicating whether phasing rules should be applied.
            If False, the function returns the BloodGroup object unmodified.

    Returns:
        BloodGroup: The modified BloodGroup object. The `alleles[AlleleState.]`
            list may be reduced, and `filtered_out` may be updated.


    Example (same phase mainly HET):
    GYPB*03/GYPB*03N.03 - in GYPB*03N.04
    GYPB*03/GYPB*03N.04 - is the only posibility as all vars in phase
    GYPB*03/GYPB*06.02 - in GYPB*03N.04
    Phenotypes (numeric): MNS:3,-4,5 | MNS:3,-4,6
    Phenotypes (alphanumeric): S+,s-,He+ | S+,s-,U+

    #Data:
    Vars: {
    '4:143999443_G_A': 'Homozygous',
    '4:144001261_T_C': 'Heterozygous',
    '4:144001254_T_A': 'Heterozygous',
    '4:144001250_T_C': 'Heterozygous',
    '4:144001249_C_A': 'Heterozygous',
    '4:144001262_A_C': 'Heterozygous',
    '4:143997535_C_A': 'Heterozygous'}

    Filtered:
    Allele
    genotype: GYPB*03
    defining_variants:
            4:143999443_G_A #hom
    weight_geno: 1000
    phenotype: MNS:3,-4 or S+,s-
    reference: False
    phases: ('.',)

    Allele
    genotype: GYPB*06.02
    defining_variants:
            4:144001249_C_A
            4:143999443_G_A #hom
            4:144001254_T_A
            4:144001262_A_C
            4:144001261_T_C
            4:144001250_T_C
    weight_geno: 1000
    phenotype: MNS:3,-4,6 or S+,s-,He+
    reference: False
    phases: ('143997535', '143997535', '143997535',
      '143997535', '143997535', '.')

    Allele
    genotype: GYPB*03N.03
    defining_variants:
            4:143997535_C_A
            4:143999443_G_A #hom
    weight_geno: 1000
    phenotype: MNS:-3,-4,5w or S-,s-,U+w
    reference: False
    phases: ('.', '143997535')

    Allele
    genotype: GYPB*03N.04
    defining_variants:
            4:143997535_C_A
            4:144001249_C_A
            4:143999443_G_A #hom
            4:144001254_T_A
            4:144001262_A_C
            4:144001261_T_C
            4:144001250_T_C
    weight_geno: 1000
    phenotype: MNS:-3,-4,5w or S-,s-,U+w
    reference: False
    phases: ('143997535', '143997535', '143997535',
      '143997535', '143997535', '143997535', '.')


    """
    if not phased:
        return bg
    for allele_state in [AlleleState.NORMAL, AlleleState.CO]:
        if not proceed(bg, allele_state):
            continue
        if len(bg.alleles[allele_state]) in [1, 0]:
            return bg
        # process alleles
        alleles = list(flatten_alleles(bg.alleles[allele_state]))
        alleles_with_variants_in_same_phase_set = [
            allele
            for allele in alleles
            if check_phase(bg.variant_pool_phase_set, allele, ".")
        ]
        alleles_with_variants_in_same_phase = [
            allele
            for allele in alleles_with_variants_in_same_phase_set
            if check_phase(bg.variant_pool_phase, allele, "1/1")
        ]
        # split by phase
        l1, l2 = [], []
        for allele in sorted(
            alleles_with_variants_in_same_phase,
            key=lambda allele: len(allele.defining_variants),
            reverse=True,
        ):
            phases = set([])
            for variant in allele.defining_variants:
                phase = bg.variant_pool_phase[variant]
                if phase != "1/1":
                    phases.add(bg.variant_pool_phase[variant])

            assert len(phases) == 1
            phase = phases.pop()
            if phase == "1|0":
                l1.append(allele)
            elif phase == "0|1":
                l2.append(allele)
            else:
                assert phase in "unknown" or "/" in phase
        # figure out what to remove
        alleles_to_remove = iterate_over_list(l1)
        alleles_to_remove += iterate_over_list(l2)
        to_remove = []
        for pair in bg.alleles[allele_state]:
            if pair.allele1 in alleles_to_remove or pair.allele2 in alleles_to_remove:
                to_remove.append(pair)
        assert len(to_remove) != len(bg.alleles[allele_state])

        if to_remove:
            bg.remove_pairs(to_remove, "filter_impossible_alleles_phased", allele_state)
        assert bg.alleles[allele_state]

    return bg


def check_phase(variant_pool: dict[str, str], current_allele: Allele, hom: str) -> bool:
    """
    True if all same phase set and or HOM
    """

    phase_sets = [
        phase
        for variant, phase in variant_pool.items()
        if variant in current_allele.defining_variants and phase != hom
    ]

    return len(set(phase_sets)) == 1


def iterate_over_list(allele_list: list[Allele]) -> list[Allele]:
    """
    Identifies if any alleles in the list are in any other allele in the list"""
    alleles_to_remove: list[Allele] = []
    for allele in allele_list:
        for allele2 in allele_list:
            if allele in allele2:
                alleles_to_remove.append(allele)
    return alleles_to_remove


@apply_to_dict_values
def rm_ref_if_2x_HET_phased(bg: BloodGroup, phased: bool) -> BloodGroup:
    """
    ref is often added by NoHomMultiVariantStrategy when all HETs variants
    need to remove if properly phased

    Example:
    2025-09-08 10:22:21.891 | DEBUG    | Sample: HG02737.vcf BG Name: ABCC4

    #Results:
    Genotypes count: 3
    Genotypes:
    ABCC4*01.02W/ABCC4*01.03W
    ABCC4*01/ABCC4*01.02W #remove
    ABCC4*01/ABCC4*01.03W #remove
    Phenotypes (numeric): PEL:1
    PEL:1w
    Phenotypes (alphanumeric): PEL+
    PEL+w

    #Data:
    Vars:
    13:95206781_C_A : Heterozygous
    13:95163161_C_T : Heterozygous
    Vars_phase:
    13:95206781_C_A : 1|0
    13:95163161_C_T : 0|1
    Vars_phase_set:
    13:95206781_C_A : 94972116
    13:95163161_C_T : 94972116
    Raw:
    Allele
    genotype: ABCC4*01.02W
    defining_variants:
            13:95206781_C_A
    weight_geno: 1000
    phenotype: PEL:1w or PEL+w
    reference: False

    Allele
    genotype: ABCC4*01.03W
    defining_variants:
            13:95163161_C_T
    weight_geno: 1000
    phenotype: PEL:1w or PEL+w
    reference: False
    """

    if not phased:
        return bg
    to_remove = []
    phased_ref_free_pair_exists = False
    same_phase_set = partial(check_phase, bg.variant_pool_phase_set)
    same_phase = partial(check_phase, bg.variant_pool_phase)
    for pair in bg.alleles[AlleleState.NORMAL]:
        if pair.allele1.reference or pair.allele2.reference:
            to_remove.append(pair)
            continue
        if possible_to_use_phase(same_phase_set, same_phase, pair):
            phase1 = allele_phase(bg.variant_pool_phase, pair.allele1)
            phase2 = allele_phase(bg.variant_pool_phase, pair.allele2)
            assert phase1 != phase2
            phased_ref_free_pair_exists = True
    if to_remove and phased_ref_free_pair_exists:
        bg.remove_pairs(to_remove, "rm_ref_if_2x_HET_phased")

    return bg


def allele_phase(variant_pool, allele):
    return set(
        [
            phase
            for variant, phase in variant_pool.items()
            if variant in allele.defining_variants
        ]
    )


def possible_to_use_phase(same_phase_set: Callable, same_phase: Callable, pair: Pair):
    return (same_phase_set(pair.allele1, ".") and same_phase(pair.allele2, "1/1")) and (
        same_phase_set(pair.allele2, ".") and same_phase(pair.allele2, "1/1")
    )


@apply_to_dict_values
def low_weight_hom(bg: BloodGroup, phased: bool) -> BloodGroup:
    """
    Case where there's a hom but it isn't in the top 2 ranked chunk,
    so SomeHomMultiVariantStrategy has to let it pass to here. in this
    example the 2 highest weights are in in opposite phase.
    no example where they're in phase, yet

    2025-09-17 08:08:58.947 | DEBUG | Sample: HG03437.vcf BG Name: FUT2

    #Results:
    Genotypes count: 4
    Genotypes:
    FUT2*01N.02/FUT2*01N.04 #only this is possible as in opposite phase
                            #and are the 2 biggest weights
    FUT2*01N.02/FUT2*01N.14
    FUT2*01N.02/FUT2*01N.16

    Phenotypes (numeric):
    Phenotypes (alphanumeric): Se-

    #Data:
    Vars:
    19:48703417_G_A : Heterozygous
    19:48703560_C_T : Heterozygous
    19:48703939_C_T : Heterozygous
    19:48703728_G_A : Homozygous
    Vars_phase:
    19:48703417_G_A : 0|1
    19:48703560_C_T : 1|0
    19:48703939_C_T : 1|0
    19:48703728_G_A : 1/1
    Vars_phase_set:
    19:48703417_G_A : 48646783
    19:48703560_C_T : 48646783
    19:48703939_C_T : 48646783
    19:48703728_G_A : .
    Raw:
    Allele
    genotype: FUT2*01N.02
    defining_variants:
            19:48703417_G_A
    weight_geno: 1
    phenotype: . or Se-
    reference: False

    Allele
    genotype: FUT2*01N.04
    defining_variants:
            19:48703560_C_T
    weight_geno: 2
    phenotype: . or Se-
    reference: False

    Allele
    genotype: FUT2*01N.14
    defining_variants:
            19:48703939_C_T
    weight_geno: 8
    phenotype: . or Se-
    reference: False

    Allele
    genotype: FUT2*01N.16
    defining_variants:
            19:48703728_G_A
    weight_geno: 8
    phenotype: . or Se-
    reference: False
    """

    if not phased:
        return bg
    same_phase_set = partial(check_phase, bg.variant_pool_phase_set)
    same_phase = partial(check_phase, bg.variant_pool_phase)
    # store as list of tuples: (weight, pair)
    pairs: list[tuple[float, Pair]] = []
    for pair in bg.alleles[AlleleState.NORMAL]:
        if possible_to_use_phase(same_phase_set, same_phase, pair):
            phase1 = allele_phase(bg.variant_pool_phase, pair.allele1)
            phase2 = allele_phase(bg.variant_pool_phase, pair.allele2)
            assert phase1 != phase2
            pairs.append((pair.allele1.weight_geno + pair.allele2.weight_geno, pair))
    if not pairs:
        return bg
    if len(pairs) == 1:
        return bg
    weights = set([pair_tup[0] for pair_tup in pairs])
    if len(weights) == 1:
        return bg
    # select the lowest-weighted pair
    best_weight, best_pair = min(pairs, key=lambda x: x[0])

    to_remove = [pair for pair in bg.alleles[AlleleState.NORMAL] if pair != best_pair]
    if to_remove:
        bg.remove_pairs(to_remove, "low_weight_hom")

    return bg


@apply_to_dict_values
def no_defining_variant(bg: BloodGroup, phased: bool) -> BloodGroup:
    """
    need to rm ref as 1:25390874_ref not possible
    as 1:25390874_C_G: Homozygous

    bg.variant_pool_phase: {'1:25390874_C_G': '1/1',
                            '1:25408711_G_A': '0|1',
                            '1:25408711_ref': '1|0',
                            '1:25408815_T_C': '0|1',
                            '1:25408817_T_C': '0|1',
                            '1:25408840_G_T': '0|1',
                            '1:25408868_G_A': '0|1',
                            '1:25420739_G_C': '1|0',
                            '1:25420739_ref': '0|1'}
    bg.variant_pool: {'1:25390874_C_G': 'Homozygous',
                      '1:25408711_G_A': 'Heterozygous',
                      '1:25408711_ref': 'Heterozygous',
                      '1:25408815_T_C': 'Heterozygous',
                      '1:25408817_T_C': 'Heterozygous',
                      '1:25408840_G_T': 'Heterozygous',
                      '1:25408868_G_A': 'Heterozygous',
                      '1:25420739_G_C': 'Heterozygous',
                      '1:25420739_ref': 'Heterozygous'}
    ic| allele: Allele
                genotype: RHCE*04
                defining_variants:
                        1:25390874_C_G
                        1:25408815_T_C
                        1:25408868_G_A
                        1:25408711_G_A
                        1:25420739_ref
                        1:25408840_G_T
                        1:25408817_T_C
                weight_geno: 1000
                phenotype: RH:2,3,-4,-5,22 or C+,E+,c-,e-,CE+
                reference: False
    ic| allele: Allele
                genotype: RHCE*01
                defining_variants:
                        1:25420739_G_C
                        1:25408711_ref
                        1:25390874_ref
                weight_geno: 1000
                phenotype: RH:-2,-3,4,5,6 or C-,E-,c+,e+,f+
                reference: True
    """

    if not phased:
        return bg
    to_remove = []

    for pair in bg.alleles[AlleleState.NORMAL]:
        for allele in pair.alleles:
            if not allele.reference:
                continue
            if all(variant.endswith(".") for variant in allele.defining_variants):
                continue
            for variant in allele.defining_variants:
                if variant == "9:133257521_T_TC" or variant == "136132908_T_TC":
                    continue
                if variant not in bg.variant_pool:
                    # ic(variant)
                    to_remove.append(pair)
                    break
    if to_remove:
        # ic(1,bg.sample, bg.type,to_remove, bg.alleles[AlleleState.NORMAL], bg.variant_pool)
        bg.remove_pairs(to_remove, "no_defining_variant")
        # ic(2,to_remove, bg.alleles[AlleleState.NORMAL], bg.variant_pool)

    return bg

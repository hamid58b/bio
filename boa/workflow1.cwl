#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: Workflow
label: "Unaligned BAM to BQSR and VCF"
requirements:
    - class: ScatterFeatureRequirement
    - class: SubworkflowFeatureRequirement
    - class: MultipleInputFeatureRequirement

inputs:
    GFFs:
        type: File[]
    Assembly_stats:
        type: File[]
    Fasta:
        type: File[]
    Taxonomy:
        type: File
    known_indels:
        type: File
        secondaryFiles: [.tbi]
outputs:
    Summary_stats:
        type: File
        outputSource: apply_bqsr/bqsr_bam
        secondaryFiles: [^.csv]
steps:
    align:
        scatter: [bam, readgroup]
        scatterMethod: dotproduct
        run: align.cwl
        in:
            bam: bams
            readgroup: readgroups
            reference: reference
        out:
            [tagged_bam]
    merge:
        run: merge.cwl
        in:
            bams: [align/tagged_bam]
        out:
            [merged_bam]
    name_sort:
        run: name_sort.cwl
        in:
            bam: merge/merged_bam
        out:
            [name_sorted_bam]
    mark_duplicates_and_sort:
        run: mark_duplicates_and_sort.cwl
        in:
            bam: name_sort/name_sorted_bam
        out:
            [sorted_bam]
    bqsr:
        run: bqsr.cwl
        in:
            reference: reference
            bam: mark_duplicates_and_sort/sorted_bam
            known_sites: [dbsnp, mills, known_indels]
        out:
            [bqsr_table]
    apply_bqsr:
        run: apply_bqsr.cwl
        in:
            reference: reference
            bam: mark_duplicates_and_sort/sorted_bam
            bqsr_table: bqsr/bqsr_table
        out:
            [bqsr_bam]

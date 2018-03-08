cwlVersion: v1.0
class: CommandLineTool
baseCommand: echo

hints:
    clauses:
      c1: [ "0.90: Annotate(FASTA, GFF) :- input(Fastq)"]
      
label: 'Genome Annotation'

inputs:
    Assembled_Genome:
        type: File
    
outputs:
    Gene_Features: 
        type: File
    Assembly_Stats: 
        type: File

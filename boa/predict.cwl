cwlVersion: v1.0
class: CommandLineTool
baseCommand: echo

label: 'Genome Annotation'

hints:
    clauses:
      c1: [ "0.90: Annotate(FASTA, GFF) :- input(Fastq)"]
      
      
inputs:
    Assembled_Genome:
        type: File
    
outputs:
    Gene_Features: 
        type: File
    Assembly_Stats: 
        type: File

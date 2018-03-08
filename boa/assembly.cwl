
cwlVersion: v1.0
class: CommandLineTool
baseCommand: echo

hints:
    clauses:
      c1: [ "0.5: Alignment(FASTA) :- input(Cleaned_Genome)"]
      c2: [ "0.99: output(Assembled_Genome) :- input(FASTA)"]

      
      
label: 'Genome Assembly'

inputs:
    Cleaned_Genome:
        type: File
  
outputs:
    Assembled_Genome: 
        type: File

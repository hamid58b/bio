cwlVersion: v1.0
class: CommandLineTool
baseCommand: echo    
label: 'Genome Assembly'
hints:
    clauses:
      c1: [ "0.5: Alignment(FASTA) :- input(Cleaned_Genome)"]
      c2: [ "0.99: output(Assembled_Genome) :- input(FASTA)"]

inputs:
    Cleaned_Genome:
        type: File
  
outputs:
    Assembled_Genome: 
        type: File


cwlVersion: v1.0
class: CommandLineTool
baseCommand: echo

hints:
    clauses:
      c1: [ "0.99: assemble(Assembled_Genome) :- input(Cleaned_Genome)"]
      c2: [ "0.99: output(Assembled_Genome) :- input(Cleaned_Genome)"]

      
      
label: 'Genome Assembly'

inputs:
    Cleaned_Genome:
        type: File
  
outputs:
    Assembled_Genome: 
        type: File

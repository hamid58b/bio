
cwlVersion: v1.0
class: CommandLineTool
baseCommand: echo

hints:
    clauses:
      c1: [ "0.94: corrected(Fastq) :- input(Fastq)"]
      
label: 'pPreprocessing'

inputs:
    Short_Reads:
        type: File
    Quality_Score: 
        type: File
  
outputs:
    Cleaned_Fastq: 
        type: File

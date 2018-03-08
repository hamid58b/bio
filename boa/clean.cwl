
cwlVersion: v1.0
class: CommandLineTool
baseCommand: echo

hints:
    clauses:
      c1: [ "0.94: corrected(Cleaned_Fastq) :- input(Short_Reads,Quality_Score)"]
      
label: 'pPreprocessing'

inputs:
    Short_Reads:
        type: File
    Quality_Score: 
        type: File
  
outputs:
    Cleaned_Fastq: 
        type: File

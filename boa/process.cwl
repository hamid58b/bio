cwlVersion: v1.0

class: CommandLineTool
baseCommand: echo

label: 'Query Processing'

inputs:
    Schema:
        type: File
    sequence_file:
        type: File
outputs:
    Comparative_Genomics_Stats:
        type: File
    Assembly_Stats:
        type: File    

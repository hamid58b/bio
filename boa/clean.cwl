
cwlVersion: v1.0
class: CommandLineTool
baseCommand: echo

label: 'Data Cleaning'

inputs:
    GFF_Files:
        type: File[]
    Fasta_Files: 
        type: File[]
    Assembly_Stats_Files: 
        type: File[]

  
outputs:
    GFFs:
        type: File[]
    Fasta: 
        type: File[]
    Assembly_Stats: 
        type: File[]

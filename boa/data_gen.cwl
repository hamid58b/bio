cwlVersion: v1.0

class: CommandLineTool
baseCommand: echo

label: 'Data Generation'

inputs:
    GFFs:
        type: File[]
    Fasta: 
        type: File[]
    Assembly_Stats: 
        type: File[]
    Taxonomy_database: 
        type: File
    Schema: 
        type: File   

  
outputs:
    Hadoop_Sequence_File:
        type: File

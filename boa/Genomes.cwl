cwlVersion: v1.0
class: Workflow
doc: |
   This workflow describes the comparative genomics
   and genome assembly summary statistics 
   
requirements:
  - class: DockerRequirement
    dockerPull: https://hub.docker.com/cwlviewer/
  
inputs:
  GFF_Files: File[]
  Fasta_Files: File[]
  Assembly_Stats_Files: File[]
  Taxonomy_database: File
  Gene_Ontology: File
  

outputs:
  Comparative_Genomics_Stats:
    type: File
    outputSource: process/Comparative_Genomics_Stats
  Assembly_Stats:
    type: File
    outputSource: process/Assembly_Stats
    
steps:
  cleaning:
    run: clean.cwl
    in:
      GFF_Files: GFF_Files
      Fasta_Files: Fasta_Files
      Assembly_Stats_Files: Assembly_Stats_Files
    out: [GFFs,Fasta,Assembly_Stats]
    
  schema_gen:
    run: schema.cwl
    in:
      Gene_Ontology: Gene_Ontology
    out: [Schema]  
  
  data_gen:
    run: data_gen.cwl
    in:
      Taxonomy_database: Taxonomy_database
      GFFs: cleaning/GFFs
      Fasta: cleaning/Fasta
      Assembly_Stats: cleaning/Assembly_Stats
      Schema : schema_gen/Schema
    out: [Hadoop_Sequence_File]  
  
  process:
    run: process.cwl
    in:
      sequence_file: data_gen/Hadoop_Sequence_File
      Schema: schema_gen/Schema 
    out: [Comparative_Genomics_Stats , Assembly_Stats]  
  

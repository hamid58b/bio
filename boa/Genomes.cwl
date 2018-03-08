cwlVersion: v1.0
class: Workflow
doc: |
   This workflow describes the geonome assembly and annoation prcoess
   
requirements:
  - class: DockerRequirement
    dockerPull: https://hub.docker.com/cwlviewer/
  
inputs:
  Short_Reads: File
  Quality_Score: File
  

outputs:
  Gene_Features:
    type: File
    outputSource: gene_prediction/Gene_Features
  Assembly_Stats:
    type: File
    outputSource: gene_prediction/Assembly_Stats
    
steps:
  cleaning:
    run: clean.cwl
    in:
      Short_Reads: Short_Reads
      Quality_Score: Quality_Score
    out: [Cleaned_Fastq]
    
  
  genome_assembly:
    run: assembly.cwl
    in:
      Assembly_Stats: cleaning/Cleaned_Fastq
    out: [Assembled_Genome]  
  
  gene_prediction:
    run: predict.cwl
    in:
      assembled_genome: genome_assembly/Assembled_Genome
    out: [Gene_Features , Assembly_Stats]  
  

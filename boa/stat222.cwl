cwlVersion: v1.0
class: Workflow

inputs:
  GFFs: File[]
  Fasta: File[]
  Assembly_Stats: File[]
  Taxonomy: File[]
  

outputs:
  Summary_stats:
    type: File
    outputSource: md5sum/output_file1
  
    
steps:
  md5sum:
    run: dockstore-tool-md5sum.cwl
    in:
      GFFs: GFFs
      Fasta: Fasta
      Assembly_Stats: Assembly_Stats
      Taxonomy: Taxonomy
    out: [output_file1, output_file2]

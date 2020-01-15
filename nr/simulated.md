# Simulated dataset

## steps
- take all the NR taxa
  - file location: ``` /Users/hbagheri/Downloads/mis-ann/seqCount2019V3/nr_taxa_list_from_Boa```
- take 100k proteins from the RefSeq database (manually curated database)
- for each protein from samples:
  - add a mislabel s.t it is not from the same phylum or class.


## Take NR sample
* location on disk: ``` /Users/hbagheri/Downloads/mis-ann/simulated```
* take RefSeq sample by command shuf: ```  ```

## find misannotation

* run the script ``` python verify_seq_parallel.py mislabeled_samples  ``` to check tree for LCA
* find protein ids that have misannotations: ``` python get_misann_ids.py . ```
* we need to remove those IDs that already are suspicious, make sure we havre a verified sample of RefSeq: ``` python sample_verified.py misannotated_keys sample_RefSeq  ```

# Related works on finding misclassified taxa

## Phylogeny-aware work (SATIVA)
* https://github.com/amkozlov/sativa
* examples works currently for RNA
* examples work for one taxa at a time.


## Others related works

* https://metagenomics-workshop.readthedocs.io/en/latest/annotation/taxonomic_annotation.html

## Analysis

### Methods on running our approach on the SATIVA dataset
* dataset is RNA
* commands to generate the cluster at 95% similarity
  ```

  ```

### Detect misannotations
* Example: based on the consensus data the sequence with id UlaSpe11 is misannotated with ```g__Cupriavidus ```. It belongs to cluster id 4576 that most sequences suggest ```g__Burkholderia```  

 ```
 >Cluster 4576
 0	1458nt, >UlaAcidi... *
 1	1458nt, >UlaSabia... at 1:1458:1:1458/+/95.54%
 2	1457nt, >UlaSpe11... at 1:1457:1:1458/+/96.64%
 3	1458nt, >UlaSp292... at 1:1458:1:1458/+/95.13%
 4	1458nt, >UlaSp960... at 1:1458:1:1458/+/96.23%
 5	1458nt, >UlaFerra... at 1:1458:1:1458/+/95.27%
 6	1457nt, >UlaPhyma... at 1:1457:1:1458/+/95.61%
 ```

* run time?
* important time: Alignment time was not reported in the Phylogeny-aware paper

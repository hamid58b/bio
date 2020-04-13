# NR experiments

## on local machine
* location on the local machine: ```/Users/hbagheri/Documents/nr_database```

## Misclassified/misannotation dataset of BoaG
* Output of BoaG scripts
* Location: ```/Users/hbagheri/Downloads/mis-ann/```

```text
atan-115B-01:mis-ann hbagheri$ pwd
/Users/hbagheri/Downloads/mis-ann
atan-115B-01:mis-ann hbagheri$ ls -lht
total 315048
-rw-r--r--      1 hbagheri  IASTATE\Domain Users   3.5K Jan 29 17:31 seq_clstr_conflict.py
-rw-r--r--      1 hbagheri  IASTATE\Domain Users   4.8M Jan 27 16:04 Log_common0
-rw-r--r--      1 hbagheri  IASTATE\Domain Users    71M Jan 27 15:51 Log_Conflict3
-rw-r--r--      1 hbagheri  IASTATE\Domain Users    55M Jan 27 15:06 Log_Conflict2
-rw-r--r--      1 hbagheri  IASTATE\Domain Users    23M Jan 24 15:31 log_conflicts
drwxr-xr-x     18 hbagheri  IASTATE\Domain Users   612B Jan 16 11:21 simulated
drwxr-xr-x     26 hbagheri  IASTATE\Domain Users   884B Jan 15 14:58 seqCount2019V3
drwxr-xr-x     14 hbagheri  IASTATE\Domain Users   476B Nov  7 12:01 clstrCount2019V3
drwxr-xr-x     19 hbagheri  IASTATE\Domain Users   646B Jun 18  2019 seqCount2019V2
drwxr-xr-x     15 hbagheri  IASTATE\Domain Users   510B May 10  2019 clstrCount2019V2
drwxr-xr-x      9 hbagheri  IASTATE\Domain Users   306B May  9  2019 clstrCount2019
drwxr-xr-x      9 hbagheri  IASTATE\Domain Users   306B May  8  2019 seqCount2019
drwxr-xr-x  33419 hbagheri  IASTATE\Domain Users   3.2M Apr  3  2019 clusters
drwxr-xr-x  11327 hbagheri  IASTATE\Domain Users   2.5M Apr  3  2019 sequences

```

## Clustering dataset for the NR paper

```text
/Users/hbagheri/Documents/tmp/cd-hit

```

## Simulated dataset for the misclassification paper
```text
atan-115B-01:simulated hbagheri$ pwd
/Users/hbagheri/Downloads/mis-ann/simulated
atan-115B-01:simulated hbagheri$ ls -lht
total 528
drwxr-xr-x  5 hbagheri  IASTATE\Domain Users   170B Jan 16 11:21 genus
drwxr-xr-x  6 hbagheri  IASTATE\Domain Users   204B Jan 16 11:19 tmp
-rw-r--r--  1 hbagheri  IASTATE\Domain Users    42K Jan 16 11:16 sample
-rw-r--r--  1 hbagheri  IASTATE\Domain Users    30K Jan 16 11:15 sample_verified_mislabeled
-rw-r--r--@ 1 hbagheri  IASTATE\Domain Users   3.1K Jan 16 11:15 mislabel_nr.py
-rw-r--r--  1 hbagheri  IASTATE\Domain Users   297B Jan 16 10:17 get_ids_from_boa.py
-rw-r--r--@ 1 hbagheri  IASTATE\Domain Users   287B Jan 16 10:10 get_misann_ids.py
-rw-r--r--  1 hbagheri  IASTATE\Domain Users    27K Jan 16 10:05 sample_verified
-rw-r--r--@ 1 hbagheri  IASTATE\Domain Users    12K Jan 16 10:05 sample_verified2
-rw-r--r--@ 1 hbagheri  IASTATE\Domain Users   4.2K Jan 16 09:56 misannotated_keys
-rw-r--r--@ 1 hbagheri  IASTATE\Domain Users   721B Jan 16 09:55 sample_verified.py
-rw-r--r--  1 hbagheri  IASTATE\Domain Users   599B Jan 15 15:58 misannotated_clusters_keys
-rw-r--r--  1 hbagheri  IASTATE\Domain Users    41K Jan 15 15:56 sample_verified1
-rw-r--r--  1 hbagheri  IASTATE\Domain Users    61K Jan 15 15:27 sample_RefSeq
-rw-r--r--@ 1 hbagheri  IASTATE\Domain Users   9.0K Jan 15 14:16 verify_seq_parallel.py

``` 
## Dataset of related works
* location: ```/Users/hbagheri/Documents/MyGithub/mislabels16-data/sim```
```text
atan-115B-01:sim hbagheri$ pwd
/Users/hbagheri/Documents/MyGithub/mislabels16-data/sim
atan-115B-01:sim hbagheri$ ls -lht
total 63839848
drwxr-xr-x  31 hbagheri  IASTATE\Domain Users   1.0K Jan 30 12:05 ali
-rw-r--r--   1 hbagheri  IASTATE\Domain Users   2.3K Jan 29 10:35 experiment.md
-rw-r--r--   1 hbagheri  IASTATE\Domain Users    30G Jan 26 11:44 VnjHydro_files
drwxr-xr-x   7 hbagheri  IASTATE\Domain Users   238B Jan 26 11:06 eval
drwxr-xr-x  13 hbagheri  IASTATE\Domain Users   442B Jan 26 11:06 script
drwxr-xr-x   7 hbagheri  IASTATE\Domain Users   238B Jan 26 11:06 tax
drwxr-xr-x  21 hbagheri  IASTATE\Domain Users   714B Jan 25 15:24 ltp123_tree
drwxr-xr-x   6 hbagheri  IASTATE\Domain Users   204B Jan 25 15:24 part

```
#### SATIVA dataset
* Location: ```/Users/hbagheri/Downloads/tmp/sativa```
```text
atan-115B-01:sativa hbagheri$ ls -lt
total 1294096
drwxr-xr-x   8 hbagheri  IASTATE\Domain Users        272 Jan 30 09:54 example
drwxr-xr-x  16 hbagheri  IASTATE\Domain Users        544 Jan 30 09:54 tmp
-rw-r--r--   1 hbagheri  IASTATE\Domain Users        696 Jan 30 09:52 syntest.log
-rw-r--r--   1 hbagheri  IASTATE\Domain Users      32715 Jan 30 09:49 epa_trainer.pyc
-rwxr-xr-x   1 hbagheri  IASTATE\Domain Users      38086 Jan 30 09:48 epa_trainer.py
-rw-r--r--   1 hbagheri  IASTATE\Domain Users  662376686 Jan 30 09:36 log
drwxr-xr-x  24 hbagheri  IASTATE\Domain Users        816 Jan 30 09:22 epac
drwxr-xr-x  11 hbagheri  IASTATE\Domain Users        374 Jan 25 15:22 tests
drwxr-xr-x   8 hbagheri  IASTATE\Domain Users        272 Jan 20 18:43 raxml
-rwxr-xr-x   1 hbagheri  IASTATE\Domain Users       2205 Jan 20 18:29 install.sh
-rw-r--r--   1 hbagheri  IASTATE\Domain Users        855 Jan 20 18:29 sativa.cfg
-rwxr-xr-x   1 hbagheri  IASTATE\Domain Users      35404 Jan 20 18:29 sativa.py
-rwxr-xr-x   1 hbagheri  IASTATE\Domain Users         52 Jan 20 18:29 test.sh
-rw-r--r--   1 hbagheri  IASTATE\Domain Users      35122 Jan 20 18:29 LICENSE
-rw-r--r--   1 hbagheri  IASTATE\Domain Users       4280 Jan 20 18:29 README.md
-rwxr-xr-x   1 hbagheri  IASTATE\Domain Users      24186 Jan 20 18:29 epa_classifier.py
atan-115B-01:sativa hbagheri$ pwd
/Users/hbagheri/Downloads/tmp/sativa

```

## BoaG script on command line
* Location: ```/Users/hbagheri/Documents/BoaG```
* BoaG scripts for NR on the repository: ```/Users/hbagheri/Documents/MyGithub/NR/compiler/bioExamples/NR```


## Compiler source code & GitHub repository:
* Location: ```/Users/hbagheri/Documents/MyGithub/compiler/Boa4Genomics```
* Jupyter notebooks: ```/Users/hbagheri/Documents/MyGithub/NR/jupyter_notebooks```
* Other Jupyter notebooks from RefSeq paper that also has NR content (Andrew Repo): ```/Users/hbagheri/Documents/MyGithub/BoaISMB/Notebook_Hamid```

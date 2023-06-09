# Exploration of CE-PL CAZymes

Explore the sequence, structure and function of CAZymes containing a CE and PL9 domain.

The 4 proteins in CAZy that are annotated with a CE0 and PL9 domain are, and which based on sequence similarity fall into two groups: (i) AEI43346.1, AFH63317.1, and AFK65394.1, and (ii) QYM77803.1.

## BLASTP proteins

The four proteins were queried against one another using BLASTP, via the NCBI BLASTP server (2023-04-01).

The output was downloaded from the website and stored in `results/blastp/four_proteins/` dir.

## Proteins

| Group | Accession        | Species                              | NCBI:txid | Locus tag |      Genome      | Length (Aa) | Mass (KDa) | Signal peptide (Y/N) (CS) |
|-------|------------------|--------------------------------------|-----------|-----------|------------------|-------------|------------|---------------------------|
| 1     | AEI43346.1 (AEI) | _Paenibacillus mulilaginosus KNP414_ | 1036673   | QYM77803  | GCA_019464535.1  | 993         | 107.36     |         Y (39:40)         |
| 1     | AFH63317.1 (AFH) | _Paenibacillus mucilaginosus K02_    | 997761    | AFH63317  | GCA_000258535.2  | 777         | 84.68      |         Y (38:39)         |
| 1     | AFK65394.1 (AFK) | _Paenibacillus mucilaginosus K02_    | 997761    | AFK65394  | CDS (JN225200.1) | 784         | 85.65      |         Y (45:46)         |
| 2     | QYM77803.1 (QYM) | _Horticoccus luteus_                 | 2862869   | QYM77803  | GCA_019464535.1  | 4380        | 445.71     |         Y (18:19)         |

_Paenibacillus mucilaginosus_ NCBI:txid 61624.

_Protein mass was predicted using [Science Gateway Protein Molecular Weight Calculator](https://www.sciencegateway.org/tools/proteinmw.htm)_

_The presence/absence of signal peptides was predicted using [SignalP version 6](https://services.healthtech.dtu.dk/services/SignalP-6.0/) (Teufel et al., 2022)_

> Teufel, F., Almagro Armenteros, J.J., Johansen, A.R. et al. SignalP 6.0 predicts all five types of signal peptides using protein language models. Nat Biotechnol 40, 1023–1025 (2022). https://doi.org/10.1038/s41587-021-01156-3

## Sequences

* AEI sequence available in `data/seqs/aie_seq.fasta`.
* AFH sequence available in `data/seqs/afh_seq.fasta`.
* AFK sequence available in `data/seqs/afk_seq.fasta`.
* QYM sequence available in `data/seqs/qym_seq.fasta`.

## Build a local CAZyme db

All CAZyme records were downloaded from CAZy in 2023-03-31, and compiled into a local SQLite3 database using `cazy_webscraper`:
```bash
scripts/cazy/build_cazyme_db <email>
```

## Predict CAZyme domains

### dbCAN

The CAZyme classifier `dbCAN` (Zhange et al., 2018) was used to predict CAZyme domains in all proteins.

> Zhang H, Yohe T, Huang L, Entwistle S, Wu P, Yang Z, Busk PK, Xu Y, Yin Y. dbCAN2: a meta server for automated carbohydrate-active enzyme annotation. Nucleic Acids Res. 2018 Jul 2;46(W1):W95-W101. doi: 10.1093/nar/gky418. PMID: 29771380; PMCID: PMC6031026.

dbCAN was used to predict CAZyme domains in the full length protein sequences, via the dbCAN website ([2023-03-31](https://bcb.unl.edu/dbCAN2/index.php)) using HMMER-dbCAN, DIAMOND and HMMER-subdbCAN - running dbCAN version 3 - although it isn't it's running dbCAN version 4.

The output was saved to results `results/dbcan/dbcan_output.csv`, and are presented here.

| Gene ID    | EC#              | HMMER                                        | DIAMOND       | dbCAN_sub              | Signal Peptide | # of Tools |
|------------|------------------|----------------------------------------------|---------------|------------------------|----------------|------------|
| AEI43346.1 | -                | PL9(34-424)+CE12(622-832)                    | CE0+PL9_1     | PL9_e16+CE12_e7        | N              | 3          |
| AFH63317.1 | -                | PL9(33-423)+CE12(621-743)                    | CE0+PL9_1     | PL9_e16+CE12_e49       | Y (1-39)       | 3          |
| AFK65394.1 | -                | PL9(40-430)+CE12(628-750)                    | CE0+PL9_1     | PL9_e16+CE12_e49       | Y (1-46)       | 3          |
| QYM77803.1 | 4.2.2.2\|4.2.2.- | CE8(696-981)+PL9_1(1695-2096)+PL1(3003-3209) | CE8+PL1+PL9_1 | CE8_e77+PL9_e8+PL1_e79 | Y (1-19)       | 3          |

### Blast CAZy families PL1, PL9, CE8 and CE12

`cazy_webscraper` was used to retrieve the protein sequences from the NCBI Protein database for all CAZymes in CAZy families PL1, PL9 and CE8.

```bash
scripts/cazy/download_fam_seqs.sh <email>
```

For each CAZy family (PL1, PL9 and CE8), the protein sequences of CAZymes in the family were extracted from the local CAZyme database and written to a multi-sequence FASTA file using `cazy_webscraper`:
```bash
scripts/cazy/get_fam_seqs.sh
```

Downloaded data:

| Family | Num of accessions | Num of seqs |
|--------|-------------------|-------------|
| PL1    | 12,296            | 9,190       |
| PL9    | 3,497             | 41          |
| CE8    | 10,662            | 8,204       |
| CE12   | 4,579             | 3,421       |

The number of unique protein accessions for each family of interest in the local CAZyme database was retrieved using the bash script `count_fam_accs.sh`, and the output was written to `results/fam_counts/num_of_accs.csv`.
```bash
scripts/cazy/count_fam_accs.sh
```

The number of protein sequences downloaded fro each family of interest and written to a mutli-sequence FASTA File was retrieved using the Python script `count_fam_seqs.py`, and the output was written to `results/fam_counts/num_of_seqs.csv`
```bash
scripts/cazy/count_fam_seqs.py
```

BLASTP was run locally (BLAST+), query QMY against each CAZy family protein sequence FASTA file, generating a TSV file for each run summarising the alignments and alignemnt FASTA files.
```bash
# query AIE against CE12 and PL9
scripts/blast/blast_aie.sh

# query AFH against CE12 and PL9
scripts/blast/blast_afh.sh

# query AFK against CE12 and PL9
scripts/blast/blast_afk.sh

# query QYM against CE8, PL1 and PL9
scripts/blast/blast_qym.sh
```

The BLASTP output was written to the following files:
1. AIE
    * AIE vs CE12 - `results/blastp/aie/aie_ce12.tsv`
    * AIE vs PL9 - `results/blastp/aie/aie_pl9.tsv`
2. AFH
    * AFH vs CE12 - `results/blastp/afh/afh_ce12.tsv`
    * AFH vs PL9 - `results/blastp/afh/afh_pl9.tsv`
3. AFK
    * AFK vs CE12 - `results/blastp/afk/afk_ce12.tsv`
    * AFK vs PL9 - `results/blastp/afk/afk_pl9.tsv`
1. QYM
    * QYM vs CE8 - `results/blastp/qym/qym_ce8.tsv`
    * QYM vs PL1 - `results/blastp/qym/qym_pl1.tsv`
    * QYM vs PL9 - `results/blastp/qym/qym_pl9.tsv`

### BLASTP via the NCBI server

To generate the raw alignment (FASTA) files, the proteins of interest were also queried against the protein sequences of the other family members using BLASTP via the NCBI server. 

To do this a plain text file was generated for each family listing the accessions of proteins in the family:
```bash
scripts/cazy/get_fam_acc.sh
```

The four resulting files were written to `data/accessions`

The protein of interest was used as the query sequence id, all protein accessions extracted from the local CAZyme database for the family of interest were used as the subject ids.

The results (the graphical alignment and alignment FASTA file - for the 100 highest scoring hits) were written to the respect protein subdirs in `results/blastp`.

### Query against the nr-database

The full length protein sequence of each protein was queried against the nr-database using BLASTP via the NCBI server (2023-04-01). 

The results were written to `results/blastp/nr/`.

### Domain annotations

By combining the BLASTP and dbCAN output, so as to cover the maximum range of each CAZyme domain, the following CAZyme domain ranges were produced:

QYM
* dbCAN: CE8(696-981)+PL9_1(1695-2096)+PL1(3003-3209)
* CE8 261-1200 (against ATC63710.1)
* PL9 1512-2132 ()
* PL1 2456-3368 (against ATC64129.1)

FASTA files of the predicted domains in QYM were written to `data/seqs/qym_domains/*.fasta`:
* `qym_ce8.fasta`
* `qym_pl9.fasta`
* `qym_pl1.fasta`

## Predict protein structures

https://www.biorxiv.org/content/10.1101/2021.08.15.456425v1

### Predict domains individually

### Chunk predict and structural superimposition

In an attempt to predict the orientation of the three domains in QYM relative to one another, the full length protein sequence (minus signal peptide) was broken down into blocks of 500 Aa, which overlapped one another by 150 Aa.

The blocks were as follows:

1. 20-520
2. 370-870
3. 720-1220
4. 1070-1570
5. 1420-1920
6. 1770-2270
7. 2120-2620
8. 2470-2970
9. 2820-3320
10. 3170-3670
11. 3520-4020
12. 3870-4380

The Python script `get_qym_chunks.py` generated a FASTA file for each chunk, which were written to `data/seqs/qym_chunks/*.fasta`.
```bash
mkdir data/seqs/qym_chunks -p
scripts/structure/get_qym_chunks.py
```

The protein structure for each block was predicted using colabfold, via the Google Colab notebook.

The structures were saved to `results/structures/qym/full`.

## Structural superimposition

### CAZy

### HHpred

### PDB

### Structural alignments
...

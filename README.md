# Exploration of CE-PL CAZymes

Explore the sequence, structure and function of CAZymes containing a CE and PL9 domain.

The 4 proteins in CAZy that are annotated with a CE0 and PL9 domain are, and which based on sequence similarity fall into two groups.

## Proteins



| Group | Accession        | Species                              | NCBI:txid | Length (Aa) | Mass (KDa) | Signal peptide (Y/N) |
|-------|------------------|--------------------------------------|-----------|-------------|------------|----------------|
| 1     | AEI43346.1 (AEI) | _Paenibacillus mulilaginosus KNP414_ | 1036673   | 993         | 107.36     |                |
| 1     | AFH63317.1 (AFH) | _Paenibacillus mucilaginosus K02_    | 997761    | 777         | 84.68      |                |
| 1     | AFK65394.1 (AFK) | _Paenibacillus mucilaginosus K02_    | 997761    | 784         | 85.65      |                |
| 2     | QYM77803.1 (QYM) | _Horticoccus luteus_                 | 2862869   | 4380        | 445.71     |                |

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
```
scripts/cazy/get_fam_seqs.sh
```

Downloaded data:

| Family | Num of accessions | Num of seqs |
|--------|-------------------|-------------|
| PL1    | x                 | x           |
| PL9    | x                 | x           |
| CE8    | x                 | x           |

BLASTP was run locally (BLAST+), query QMY against each CAZy family protein sequence FASTA file.

```

```

### Domain annotations

...

## Predict protein structures

https://www.biorxiv.org/content/10.1101/2021.08.15.456425v1

## Structural supersistion

...

# A proteins

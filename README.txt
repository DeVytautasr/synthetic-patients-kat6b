synthetic-patients-kat6b
========================

Overview
--------
Synthetic chr10 genomes and variant sets for KAT6B-related in silico patients and controls,
generated with simuG on top of hg38 chr10.

Reference
---------
- ref/chr10.fa – hg38 chr10 reference (length ~133,797,422 bp).

Patients
--------
Patient1 (KAT6B LoF + benign chr10 variant)
- VCF inputs:
  - vcf/patients/synthetic_patient1_chr10_only.vcf
  - vcf/patients/synthetic_patient1_chr10_all.vcf
- simuG outputs:
  - sim/patients/kat6b_patient1_chr10_only.simseq.genome.fa
  - sim/patients/kat6b_patient1_chr10_only.refseq2simseq.{SNP.vcf,map.txt}
  - sim/patients/kat6b_patient1_chr10_all.simseq.genome.fa
  - sim/patients/kat6b_patient1_chr10_all.refseq2simseq.{SNP.vcf,map.txt}

Controls
--------
Control chr10 (wild-type reference + benign chr10 variant definition)
- Genome:
  - ref/chr10.fa (used as wild-type control sequence)
- VCF + mapping:
  - vcf/control/synthetic_control_chr10_all.vcf
  - sim/control/control_chr10_all.refseq2simseq.{SNP.vcf,map.txt}
- Note:
  - For now, control simseq.genome.fa is not generated; the reference chr10.fa
    is used directly as the control genome. This is enough for variant-level
    comparisons and can be extended later if needed.

What worked
-----------
- Successfully installed and ran simuG for SNP/INDEL simulations on hg38 chr10.
- Generated synthetic chr10 genomes for Patient1 with:
  - KAT6B nonsense LoF on chr10 (10q22) plus a benign SNP.
- Verified that simseq chr10 lengths match hg38 chr10 (133,797,422 bp).
- Set up a clean project structure (ref/vcf/sim/simuG), initialized git,
  and pushed the code + configs to GitHub (large FASTA/simseq files kept local).

What did not fully work yet / open items
----------------------------------------
- Control simseq.genome.fa:
  - simuG successfully produced refseq2simseq mapping and SNP VCF for the control,
    but currently does not output a simseq.genome.fa file in this configuration.
  - For now, the control genome is represented by ref/chr10.fa (wild-type),
    plus the control VCF/mapping files.
- Next steps:
  - Add Patient2 with a different KAT6B LoF variant on chr10.
  - Optionally extend to whole-genome simulations (full GRCh38).
  - Later: simulate reads from patient/control genomes and run a small variant-calling pipeline.

big_files_backup/ – local-only large FASTA/simseq files (not tracked in git/GitHub due to the 100 MB file size limit).

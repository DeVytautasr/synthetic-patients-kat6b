synthetic-patients-kat6b
========================

Overview
--------
This repository contains synthetic chr10 genomes and variant sets for
KAT6B-related in silico patients and controls. The genomes are generated
with simuG on top of a hg38 chr10 reference. The goal is to have a small,
well-controlled testbed for KAT6B loss-of-function (LoF) variants and
benign background variation on chr10.

Repository structure
--------------------
- ref/
  - chr10.fa
    hg38 chr10 reference sequence (133,797,422 bp). Kept locally; not
    pushed to GitHub due to file size.

- vcf/
  - control/
    - synthetic_control_chr10_benign_only.vcf
  - patients/
    - synthetic_patient1_kat6b_lof_only.vcf
    - synthetic_patient1_kat6b_lof_plus_benign.vcf
    - synthetic_patient2_kat6b_lof_only.vcf
    - synthetic_patient2_kat6b_lof_plus_benign.vcf

- sim/
  - control/   simuG outputs for the control (see sim/control/README.txt)
  - patients/  simuG outputs for Patient1 and Patient2
               (see sim/patients/README.txt)

- simuG/
  Local copy of the simuG tool used to generate synthetic genomes.

- vcf_compare.py
  Python script that parses all VCF files and prints a presence/absence
  comparison table across all samples.

- vcf_visualize.py
  Python script that generates two figures:
    variant_heatmap.png          – presence/absence matrix across samples
    chr10_variant_positions.png  – variant positions on chr10 (hg38)

- variant_heatmap.png
- chr10_variant_positions.png
  Pre-generated figures for quick reference and presentation use.

Variant design (2x2)
--------------------
  Control   – wild-type chr10 + benign background SNP (BENIGN1, pos 101,000,000)
  Patient1  – KAT6B nonsense LoF (C>A, pos 74,975,481) ± BENIGN1
  Patient2  – KAT6B frameshift LoF (C>CC, pos 75,028,821) ± BENIGN1

  Both KAT6B variants are in the KAT6B gene region on 10q22.

Git and large file notes
------------------------
- Large FASTA files (ref/*.fa, sim/*/*.simseq.genome.fa) and the Python
  virtual environment (.venv/) are excluded via .gitignore.
- Git history has been cleaned; no oversized files remain in past commits.

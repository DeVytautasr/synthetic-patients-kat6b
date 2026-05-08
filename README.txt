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
    hg38 chr10 reference sequence used as the baseline genome for all
    simulations.

- vcf/
  - control/
    - synthetic_control_chr10_benign_only.vcf
      VCF defining the benign chr10 background variant for the control.
  - patients/
    - synthetic_patient1_kat6b_lof_only.vcf
      VCF defining a Patient1 KAT6B LoF variant on chr10 without extra
      benign chr10 variation.
    - synthetic_patient1_kat6b_lof_plus_benign.vcf
      VCF defining the same KAT6B LoF variant for Patient1 together with
      the benign chr10 background variant.
    - synthetic_patient2_kat6b_lof_only.vcf
      VCF defining a Patient2 KAT6B frameshift LoF variant without extra
      benign chr10 variation.
    - synthetic_patient2_kat6b_lof_plus_benign.vcf
      VCF defining the same Patient2 KAT6B frameshift LoF variant together
      with the benign chr10 background variant.

- sim/
  - control/
    - control_chr10_benign_only.refseq2simseq.SNP.vcf
    - control_chr10_benign_only.refseq2simseq.map.txt
      simuG mapping outputs describing how the benign chr10 variant is
      applied on top of the reference. A full simulated control genome
      FASTA can be generated later if needed.
  - patients/
    - patient1_kat6b_lof_only.simseq.genome.fa
    - patient1_kat6b_lof_only.refseq2simseq.SNP.vcf
    - patient1_kat6b_lof_only.refseq2simseq.map.txt
      simuG outputs for Patient1 with a KAT6B LoF variant on chr10 only.
    - patient1_kat6b_lof_plus_benign.simseq.genome.fa
    - patient1_kat6b_lof_plus_benign.refseq2simseq.SNP.vcf
    - patient1_kat6b_lof_plus_benign.refseq2simseq.map.txt
      simuG outputs for Patient1 with the KAT6B LoF variant plus the
      benign chr10 background variant.
    - patient2_kat6b_lof_only.simseq.genome.fa
    - patient2_kat6b_lof_only.refseq2simseq.SNP.vcf
    - patient2_kat6b_lof_only.refseq2simseq.map.txt
      simuG outputs for Patient2 with a KAT6B frameshift LoF variant only.
    - patient2_kat6b_lof_plus_benign.simseq.genome.fa
    - patient2_kat6b_lof_plus_benign.refseq2simseq.SNP.vcf
    - patient2_kat6b_lof_plus_benign.refseq2simseq.map.txt
      simuG outputs for Patient2 with the KAT6B frameshift LoF variant plus
      the benign chr10 background variant.

- simuG/
  Local copy of the simuG tool (Perl scripts and example data) used to
  generate synthetic variants and genomes on chr10.

Patients and controls
---------------------
- Control:
  - Uses ref/chr10.fa as the wild-type baseline sequence.
  - The benign chr10 background variant is defined in
    vcf/control/synthetic_control_chr10_benign_only.vcf and projected onto
    the reference via the refseq2simseq mapping files in sim/control/.
  - A dedicated control simseq.genome.fa is not strictly required for
    variant-level comparisons and can be generated later if needed.

- Patient1:
  - Patient1 carries a KAT6B loss-of-function variant on chr10 (10q22),
    with two VCF configurations:
    - KAT6B LoF only on chr10.
    - KAT6B LoF on chr10 plus the benign chr10 background variant.
  - simuG is used to apply these VCFs on top of ref/chr10.fa, producing
    simulated patient genomes and corresponding refseq2simseq mappings.

- Patient2:
  - Patient2 carries a different KAT6B frameshift LoF variant on chr10
    (c.3998dup-like, chr10:75028821 C>CC, p.Ser1334fs), with two VCF
    configurations:
    - KAT6B frameshift LoF only on chr10.
    - KAT6B frameshift LoF on chr10 plus the benign chr10 background variant.
  - simuG is used to apply these VCFs on top of ref/chr10.fa, producing
    simulated patient genomes and corresponding refseq2simseq mappings.

Current status
--------------
- simuG is successfully installed and running for SNP/INDEL simulations on
  hg38 chr10 with the provided VCF files.
- Synthetic chr10 genomes and mapping files for Patient1, Patient2, and the
  control have been generated and organised into ref/, vcf/, sim/, and simuG/
  directories.
- The repository implements a clean 2x2 design: two patients, each with a
  lof_only and a lof_plus_benign VCF configuration, plus a wild-type control.
- The repository is set up as a small, reproducible test system for
  KAT6B-related variant scenarios on chr10.

Large files and Git/GitHub notes
--------------------------------
- Large FASTA and simulated genome FASTA files (ref/*.fa and
  sim/*/*.simseq.genome.fa) are kept locally and excluded from version
  control using .gitignore so they are not pushed to GitHub.
- This keeps the repository under GitHub's 100 MB per-file size limit for
  regular Git repositories and avoids pushing unnecessary large binary
  files.
- The Git history has been cleaned so that no over-sized files remain in
  past commits. The current main branch on GitHub can be treated as a
  clean baseline for further patient/control additions and downstream
  analyses.

sim/patients/
=============

simuG outputs for Patient1 and Patient2 chr10 genome simulations.

Patient1 – KAT6B nonsense LoF (chr10:74,975,481 C>A)
-----------------------------------------------------
Input VCF: vcf/patients/synthetic_patient1_kat6b_lof_only.vcf
- patient1_kat6b_lof_only.refseq2simseq.SNP.vcf
- patient1_kat6b_lof_only.refseq2simseq.map.txt
- patient1_kat6b_lof_only.simseq.genome.fa         [local only]

Input VCF: vcf/patients/synthetic_patient1_kat6b_lof_plus_benign.vcf
- patient1_kat6b_lof_plus_benign.refseq2simseq.SNP.vcf
- patient1_kat6b_lof_plus_benign.refseq2simseq.map.txt
- patient1_kat6b_lof_plus_benign.simseq.genome.fa  [local only]

Patient2 – KAT6B frameshift LoF (chr10:75,028,821 C>CC)
--------------------------------------------------------
Input VCF: vcf/patients/synthetic_patient2_kat6b_lof_only.vcf
- patient2_kat6b_lof_only.refseq2simseq.SNP.vcf
- patient2_kat6b_lof_only.refseq2simseq.map.txt
- patient2_kat6b_lof_only.simseq.genome.fa         [local only]

Input VCF: vcf/patients/synthetic_patient2_kat6b_lof_plus_benign.vcf
- patient2_kat6b_lof_plus_benign.refseq2simseq.SNP.vcf
- patient2_kat6b_lof_plus_benign.refseq2simseq.map.txt
- patient2_kat6b_lof_plus_benign.simseq.genome.fa  [local only]

Notes
-----
- All *.simseq.genome.fa files are kept locally and excluded from
  GitHub via .gitignore (file size >100 MB).
- The .refseq2simseq.SNP.vcf and .refseq2simseq.map.txt files are
  tracked in GitHub and are sufficient for variant-level comparisons.
- Reference used for all simulations: ref/chr10.fa (hg38, 133,797,422 bp)

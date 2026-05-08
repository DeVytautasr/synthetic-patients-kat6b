vcf/patients/
=============

Input VCF files defining synthetic KAT6B variant sets for Patient1 and Patient2.
All VCFs target hg38 chr10 and follow VCFv4.2 format with tab-separated fields.

Files
-----
- synthetic_patient1_kat6b_lof_only.vcf
  Patient1: KAT6B nonsense LoF only.
  Variant: chr10:74,975,481 C>A (KAT6B_LOF, EFFECT=nonsense_LOF)

- synthetic_patient1_kat6b_lof_plus_benign.vcf
  Patient1: KAT6B nonsense LoF + benign chr10 background SNP.
  Variants: chr10:74,975,481 C>A + chr10:101,000,000 G>A (BENIGN1)

- synthetic_patient2_kat6b_lof_only.vcf
  Patient2: KAT6B frameshift LoF only.
  Variant: chr10:75,028,821 C>CC (PATIENT2_KAT6B_LOF_FS, EFFECT=lof_frameshift)

- synthetic_patient2_kat6b_lof_plus_benign.vcf
  Patient2: KAT6B frameshift LoF + benign chr10 background SNP.
  Variants: chr10:75,028,821 C>CC + chr10:101,000,000 G>A (BENIGN1)

Notes
-----
- VCFs use tab-separated fields (required by simuG parser).
- BENIGN1 (G>A at pos 101,000,000) is shared across all plus_benign
  configurations and the control, enabling consistent background variation.
- These VCFs are used as input to simuG; outputs go to sim/patients/.

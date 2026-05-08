ref/  – reference sequences (currently only chr10.fa, hg38)
vcf/  – input VCFs:
        synthetic_patient1_chr10_only.vcf – only KAT6B LoF on chr10
        synthetic_patient1_chr10_all.vcf  – KAT6B LoF + benign chr10 variant(s)
        synthetic_patient1_full_backup.vcf – original patient VCF draft
sim/  – simuG outputs:
        kat6b_patient1_chr10_only.* – sim genome with only KAT6B LoF
        kat6b_patient1_chr10_all.*  – sim genome with KAT6B + benign chr10
simuG/ – simuG scripts and yeast example data

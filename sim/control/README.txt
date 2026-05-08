sim/control/
============

simuG outputs for the control chr10 genome simulation.

Files
-----
- control_chr10_benign_only.refseq2simseq.SNP.vcf
  VCF describing the benign SNP (BENIGN1, chr10:101000000 G>A) as
  projected onto the simulated control genome by simuG.

- control_chr10_benign_only.refseq2simseq.map.txt
  Position mapping file from the reference (hg38 chr10) to the
  simulated control genome.

- control_chr10_benign_only.simseq.genome.fa  [local only, not in GitHub]
  Full simulated control chr10 genome FASTA produced by simuG.
  Excluded from version control due to file size (>100 MB).

Input VCF
---------
  vcf/control/synthetic_control_chr10_benign_only.vcf

Reference
---------
  ref/chr10.fa  (hg38, 133,797,422 bp)

Notes
-----
- The control genome carries only the benign background SNP (BENIGN1)
  and no KAT6B LoF variants.
- ref/chr10.fa can be used directly as the wild-type baseline for
  variant-level comparisons without requiring the simseq.genome.fa.

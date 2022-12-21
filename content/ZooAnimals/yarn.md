---
title: "YARN"
date: 2018-06-02T08:50:52-04:00
draft: false
---

{{< rawhtml >}}
<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>
{{< /rawhtml >}}
{{< rawhtml >}}
<div data-badge-popover="right" data-badge-type="donut" data-doi="doi.org/10.1186/s12859-017-1847-x" data-hide-no-mentions="true" class="altmetric-embed"></div>
{{< /rawhtml >}}
### Reference

Tissue-aware RNA-Seq processing and normalization for heterogeneous and sparse data

Joseph N. Paulson, Cho-Yi Chen, Camila M. Lopes-Ramos, Marieke L. Kuijjer, John Platig, Abhijeet R. Sonawane, Maud Fagny, Kimberly Glass & John Quackenbush

BMC Bioinformatics

[doi.org/10.1186/s12859-017-1847-x](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-017-1847-x)

### Abstract

Background

Although ultrahigh-throughput RNA-Sequencing has become the dominant technology for genome-wide transcriptional profiling, the vast majority of RNA-Seq studies typically profile only tens of samples, and most analytical pipelines are optimized for these smaller studies. However, projects are generating ever-larger data sets comprising RNA-Seq data from hundreds or thousands of samples, often collected at multiple centers and from diverse tissues. These complex data sets present significant analytical challenges due to batch and tissue effects, but provide the opportunity to revisit the assumptions and methods that we use to preprocess, normalize, and filter RNA-Seq data – critical first steps for any subsequent analysis.

Results

We find that analysis of large RNA-Seq data sets requires both careful quality control and the need to account for sparsity due to the heterogeneity intrinsic in multi-group studies. We developed Yet Another RNA Normalization software pipeline (YARN), that includes quality control and preprocessing, gene filtering, and normalization steps designed to facilitate downstream analysis of large, heterogeneous RNA-Seq data sets and we demonstrate its use with data from the Genotype-Tissue Expression (GTEx) project.

Conclusions

An R package instantiating YARN is available at http://bioconductor.org/packages/yarn.

### Implementation

[netZooR](https://github.com/netZoo/netZooR)

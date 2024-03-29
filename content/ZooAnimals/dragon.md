---
title: "DRAGON"
date: 2018-07-02T08:50:52-04:00
draft: false
---

{{< rawhtml >}}
<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>
{{< /rawhtml >}}
{{< rawhtml >}}
<div data-badge-popover="right" data-badge-type="donut" data-doi="10.1093/nar/gkac1157" data-hide-no-mentions="true" class="altmetric-embed"></div>
{{< /rawhtml >}}
### Reference

DRAGON: Determining Regulatory Associations using Graphical models on multi-Omic Networks

Katherine H Shutta, Deborah Weighill, Rebekka Burkholz, Marouen Ben Guebila, Dawn L DeMeo, Helena U Zacharias, John Quackenbush, Michael Altenbuchinger

OUP Nucleic Acids Research

[10.1093/nar/gkac1157](https://academic.oup.com/nar/advance-article/doi/10.1093/nar/gkac1157/6931867)

### Abstract


The increasing quantity of multi-omic data, such as methylomic and transcriptomic profiles collected on the same specimen or even on the same cell, provides a unique opportunity to explore the complex interactions that define cell phenotype and govern cellular responses to perturbations. We propose a network approach based on Gaussian Graphical Models (GGMs) that facilitates the joint analysis of paired omics data. This method, called DRAGON (Determining Regulatory Associations using Graphical models on multi-Omic Networks), calibrates its parameters to achieve an optimal trade-off between the network’s complexity and estimation accuracy, while explicitly accounting for the characteristics of each of the assessed omics ‘layers.’ In simulation studies, we show that DRAGON adapts to edge density and feature size differences between omics layers, improving model inference and edge recovery compared to state-of-the-art methods. We further demonstrate in an analysis of joint transcriptome - methylome data from TCGA breast cancer specimens that DRAGON can identify key molecular mechanisms such as gene regulation via promoter methylation. In particular, we identify Transcription Factor AP-2 Beta (TFAP2B) as a potential multi-omic biomarker for basal-type breast cancer. DRAGON is available as open-source code in Python through the Network Zoo package (netZooPy v0.8; netzoo.github.io).

### Implementation

[netZooPy](https://github.com/netZoo/netZooPy), [netZooR](https://github.com/netZoo/netZooR)

### Netbook tutorials

The following [netbooks](http://netbooks.networkmedicine.org/) use DRAGON:

- netZooPy:

	- Investigating potential regulatory relationships between TFs in breast cancer using DRAGON

	- Multiomic CCLE analysis using the Network Zoo




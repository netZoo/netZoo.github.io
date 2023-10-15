---
title: "PANDA"
date: 2019-07-02T08:50:52-04:00
draft: false
hidden: false
description: true
---

{{< rawhtml >}}
<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>
{{< /rawhtml >}}
{{< rawhtml >}}
<div data-badge-popover="right" data-badge-type="donut" data-doi="10.1371/journal.pone.0064832" data-hide-no-mentions="true" class="altmetric-embed"></div>
{{< /rawhtml >}}
### Reference

Passing Messages between Biological Networks to Refine Predicted Interactions. 

Kimberly Glass, Curtis Huttenhower, John Quackenbush, Guo-Cheng Yuan.

Plos One

[doi.org/10.1371/journal.pone.0064832](https://www.ncbi.nlm.nih.gov/pubmed/23741402).

### Abstract

Regulatory network reconstruction is a fundamental problem in computational biology. There are significant limitations to such reconstruction using individual datasets, and increasingly people attempt to construct networks using multiple, independent datasets obtained from complementary sources, but methods for this integration are lacking. We developed PANDA (Passing Attributes between Networks for Data Assimilation), a message-passing model using multiple sources of information to predict regulatory relationships, and used it to integrate protein-protein interaction, gene expression, and sequence motif data to reconstruct genome-wide, condition-specific regulatory networks in yeast as a model. The resulting networks were not only more accurate than those produced using individual data sets and other existing methods, but they also captured information regarding specific biological mechanisms and pathways that were missed using other methodologies. PANDA is scalable to higher eukaryotes, applicable to specific tissue or cell type data and conceptually generalizable to include a variety of regulatory, interaction, expression, and other genome-scale data. An implementation of the PANDA algorithm is available at www.sourceforge.net/projects/panda-net.

### Implementation

[netZooR](https://github.com/netZoo/netZooR), [netZooPy](https://github.com/netZoo/netZooPy), [netZooM](https://github.com/netZoo/netZooM), [netZooC](https://github.com/netZoo/netZooC)

### Netbook tutorials

The following [netbooks](http://netbooks.networkmedicine.org) use PANDA:

- netZooR:

	- Building PANDA and LIONESS Regulatory Networks from GTEx Gene Expression Data in R

	- Building PANDA Regulatory Networks from GTEx Gene Expression Data in R

	- Finding drug candidates to reverse Lung Adenocarcinoma (LUAD)-induced gene regulation disruption using TCGA

	- Differential gene targeting of pancreatic cancer subtypes

	- Sex differences in lung adenocarcinoma

	- Generating 26 cancer gene regulatory network using TCGA datasets

	- Building and analyzing enhancer-driven TF-gene regulatory networks PANDA and LIONESS

- netZooPy:

	- Controlling the variance of PANDA networks

	- Benchmarking motif networks for the reconstruction of kidney cancer regulatory network



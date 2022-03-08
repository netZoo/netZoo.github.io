---
title: "ALPACA"
date: 2019-03-02T08:50:52-04:00
draft: false
---

{{< rawhtml >}}
<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>
{{< /rawhtml >}}
{{< rawhtml >}}
<div data-badge-popover="right" data-badge-type="donut" data-doi="10.1038/s41540-018-0052-5" data-hide-no-mentions="true" class="altmetric-embed"></div>
{{< /rawhtml >}}
### Reference

Detecting phenotype-driven transitions in regulatory network structure. 

Megha Padi and John Quackenbush.

npj Systems biology and applications

[doi:10.1038/s41540-018-0052-5](https://www.nature.com/articles/s41540-018-0052-5).

### Abstract

Complex traits and diseases like human height or cancer are often not caused by a single mutation or genetic variant, but instead arise from functional changes in the underlying molecular network. Biological networks are known to be highly modular and contain dense “communities” of genes that carry out cellular processes, but these structures change between tissues, during development, and in disease. While many methods exist for inferring networks and analyzing their topologies separately, there is a lack of robust methods for quantifying differences in network structure. Here, we describe ALPACA (ALtered Partitions Across Community Architectures), a method for comparing two genome-scale networks derived from different phenotypic states to identify condition-specific modules. In simulations, ALPACA leads to more nuanced, sensitive, and robust module discovery than currently available network comparison methods. As an application, we use ALPACA to compare transcriptional networks in three contexts: angiogenic and non-angiogenic subtypes of ovarian cancer, human fibroblasts expressing transforming viral oncogenes, and sexual dimorphism in human breast tissue. In each case, ALPACA identifies modules enriched for processes relevant to the phenotype. For example, modules specific to angiogenic ovarian tumors are enriched for genes associated with blood vessel development, and modules found in female breast tissue are enriched for genes involved in estrogen receptor and ERK signaling. The functional relevance of these new modules suggests that not only can ALPACA identify structural changes in complex networks, but also that these changes may be relevant for characterizing biological phenotypes.

### Implementation

[netZooR](https://github.com/netZoo/netZooR)

### Netbook tutorials

The following [netbooks](http://netbooks.networkmedicine.org) use ALPACA:

- netZooR:

    - Gene regulatory network analysis in Glioblastoma

	- Building and analyzing enhancer-driven TF-gene regulatory networks PANDA and LIONESS

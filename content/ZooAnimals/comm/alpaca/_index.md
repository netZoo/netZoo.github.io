---
title: "ALPACA"
date: 2019-03-02T08:50:52-04:00
draft: false
description: "ALPACA is a method for differential network analysis that is based on a novel approach to comparison of network community structures. Comparisons of community structure have typically been accomplished by assessing which nodes switch community membership between networks ("community comparison") or by computing the edge weight differences by subtracting the adjacency matrices of two networks and then performing community detection on the resulting differential network ("edge subtraction"). Both these approaches have important limitations. Community comparison is subject to a resolution limit and cannot detect differences smaller than the average community size in a network. Edge subtraction transfers noise from both of the original networks to the differential network, leading to an imprecise estimator. Moreover, positive and negative edge differences cannot be distinguished in the subsequent community detection performed on the differential network.
In contrast to community comparison and edge subtraction, ALPACA compares the community structure of two networks by optimizing a new metric: differential modularity. In the ALPACA algorithm, one network is defined as the reference network and the second is defined as the perturbed network. The differential modularity metric measures the extent to which edges in a community in the perturbed network differ from those that would be expected by random chance according to a null distribution based on the reference network. Community structure of the perturbed network is determined by maximizing this differential modularity. The resulting communities are differential modules that show how the perturbed network differs from the reference network at the community level."
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

---
title: "DRAGON"
date: 2018-07-02T08:50:52-04:00
draft: false
---

{{< rawhtml >}}
<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>
{{< /rawhtml >}}
{{< rawhtml >}}
<div data-badge-popover="right" data-badge-type="donut" data-arxiv-id="2104.01690" data-hide-no-mentions="true" class="altmetric-embed"></div>
{{< /rawhtml >}}
### Reference

DRAGON: Determining Regulatory Associations using Graphical models on multi-Omic Networks

Deborah Weighill, Rebekka Burkholz, Marouen Ben Guebila, Helena U. Zacharias, John Quackenbush, and Michael Altenbuchinger

arXiv

[arXiv:2104.01690](https://arxiv.org/abs/2104.01690)

### Abstract

The increasing quantity of multi-omics data, such as methylomic and transcriptomic profiles,
collected on the same specimen, or even on the same cell, provide a unique opportunity to explore
the complex interactions that define cell phenotype and govern cellular responses to perturbations.
We propose a network approach based on Gaussian Graphical Models (GGMs) that facilitates the
joint analysis of paired omics data. This method, called DRAGON (Determining Regulatory
Associations using Graphical models on multi-Omic Networks), calibrates its parameters to achieve
an optimal trade-off between the network’s complexity and estimation accuracy, while explicitly
accounting for the characteristics of each of the assessed omics layers. In simulation studies, we
show that DRAGON adapts to edge-density and feature-size differences between the omics layers,
which improves model inference and the recovery of associations compared to state-of-the-art network
inference using GGMs. Next, we verified this performance gain on paired single-cell data, where the
transcriptome was assayed together with selected proteins. Finally, we used DRAGON to study joint
transcriptome–methylome data of breast cancer specimens. In this context, we provide examples of
how DRAGON can identify key molecular mechanisms. For instance, we show how co-expression
can be explained by co-methylation and how DRAGON gives hints about the spatial organization of
the genome. DRAGON is available as open-source code in python through the Network Zoo package
(netZooPy v0.8; netzoo.github.io)

### Implementation

[netZooPy](https://github.com/netZoo/netZooPy)

### Netbook tutorials

The following [netbooks](http://netbooks.networkmedicine.org/) use DRAGON:

- netZooPy:

	- Investigating potential regulatory relationships between TFs in breast cancer using DRAGON




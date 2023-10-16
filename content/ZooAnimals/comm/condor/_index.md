---
title: "CONDOR"
date: 2019-05-02T08:50:52-04:00
draft: false
description: "CONDOR is a tool for community detection in bipartite networks. Many community detection methods for unipartite networks are based on the concept of maximizing a modularity metric that compares the weight of edges within communities to the weight of edges between communities, prioritizing community assignments with higher values of the former relative to the latter. CONDOR extends this concept to bipartite networks by optimizing a bipartite version of modularity defined by Barber (2007). To enable bipartite community detection on large networks such gene regulatory networks, CONDOR uses a fast unipartite modularity maximization method on one of the two unipartite projections of the bipartite network. In Platig et al. (2016), CONDOR is applied to bipartite networks of single nucleotide polymorphisms (SNPs) and gene expression, where a network edge from a SNP node to a gene node is indicative of an association between the SNP and the gene expression level, commonly known as an expression quantitative trait locus (eQTL). Communities detected with CONDOR contained local hub nodes ("core SNPs") enriched for association with disease, suggesting that functional eQTL relationships are encoded at the community level."
---

{{< rawhtml >}}
<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>
{{< /rawhtml >}}
{{< rawhtml >}}
<div data-badge-popover="right" data-badge-type="donut" data-doi="10.1371/journal.pcbi.1005033" data-hide-no-mentions="true" class="altmetric-embed"></div>
{{< /rawhtml >}}
### Reference

Bipartite Community Structure of eQTLs. 

John Platig, Peter J. Castaldi, Dawn DeMeo, John Quackenbush.

Plos computational biology

[doi.org/10.1371/journal.pcbi.1005033](https://pubmed.ncbi.nlm.nih.gov/27618581/).

### Abstract

Genome Wide Association Studies (GWAS) and expression quantitative trait locus (eQTL) analyses have identified genetic associations with a wide range of human phenotypes. However, many of these variants have weak effects and understanding their combined effect remains a challenge. One hypothesis is that multiple SNPs interact in complex networks to influence functional processes that ultimately lead to complex phenotypes, including disease states. Here we present CONDOR, a method that represents both cis- and trans-acting SNPs and the genes with which they are associated as a bipartite graph and then uses the modular structure of that graph to place SNPs into a functional context. In applying CONDOR to eQTLs in chronic obstructive pulmonary disease (COPD), we found the global network "hub" SNPs were devoid of disease associations through GWAS. However, the network was organized into 52 communities of SNPs and genes, many of which were enriched for genes in specific functional classes. We identified local hubs within each community ("core SNPs") and these were enriched for GWAS SNPs for COPD and many other diseases. These results speak to our intuition: rather than single SNPs influencing single genes, we see groups of SNPs associated with the expression of families of functionally related genes and that disease SNPs are associated with the perturbation of those functions. These methods are not limited in their application to COPD and can be used in the analysis of a wide variety of disease processes and other phenotypic traits.

### Implementation

[netZooR](https://github.com/netZoo/netZooR), [netZooPy](https://github.com/netZoo/netZooPy)

### Netbook tutorials

The following [netbooks](http://netbooks.networkmedicine.org) use CONDOR:

- netZooR:

	- Exploring eQTL tissue regulation with CONDOR

	- Building and analyzing enhancer-driven TF-gene regulatory networks PANDA and LIONESS

- netZooPy:

	- Benchmarking motif networks for the reconstruction of kidney cancer regulatory network

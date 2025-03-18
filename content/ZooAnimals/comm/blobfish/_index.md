---
title: "BLOBFISH"
date: 2018-10-03T08:50:52-04:00
draft: false
description: "BLOBFISH is a method to obtain a subnetwork connecting nodes of interest across observation-specific biological networks. Many biological networks are bipartite, such as expression quantitative trait loci (eQTL) networks, gene regulatory networks, and multi-omic partial correlation networks. However, the size of omics-scale bipartite networks can make them difficult to interpret as a whole; motivating the development of tools that evaluate connectivity between a subset of nodes. In addition, observation-specific networks (i.e., sample-specific or subject-specific networks) introduce the possibility of subsetting robust edges that are consistent across observations. BLOBFISH evaluates connectivity between a subset of nodes in a set of observation-specific bipartite networks by first finding significant edges across observations in comparison to a null distribution, and then using a breadth-first-search to uncover paths between seed nodes limited to a prespecified number of hops."
---

{{< rawhtml >}}
<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>
{{< /rawhtml >}}
{{< rawhtml >}}
<div data-badge-popover="right" data-badge-type="donut" data-doi="doi.org/2025.03.11.642378" data-hide-no-mentions="true" class="altmetric-embed"></div>
{{< /rawhtml >}}
### Reference

BLOBFISH: Bipartite Limited Subnetworks from Multiple Observations using Breadth-First Search with Constrained Hops

Tara Eicher, Marouen Ben Guebila, John Quackenbush

bioRxiv

[doi.org/10.1101/2025.03.11.642378](https://www.biorxiv.org/content/10.1101/2025.03.11.642378v1.abstract)

### Abstract

In analyzing gene regulatory network models, a common question is how members of a particular set of genes are connected. For example, one might want to explore network relationship between a set of differentially expressed genes, a gene set previously reported in the literature, or elements of one or more pathways. BLOBFISH uses a breadth-first search algorithm adapted to bipartite graphs to identify a compact subnetwork connecting the members of a pre-specified set of genes, providing a regulatory context that can shed light on specific mechanisms involved in a phenotype and its development. We demonstrate the use of BLOBFISH to extract gene regulatory subnetworks reflecting tissue specificity using publicly available data from the Genotype Tissue Expression (GTEx) project.

### Implementation

[netZooR](https://github.com/netZoo/netZooR)

---
title: "CRANE"
date: 2018-10-02T08:50:52-04:00
draft: false
---

{{< rawhtml >}}
<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>
{{< /rawhtml >}}
{{< rawhtml >}}
<div data-badge-popover="right" data-badge-type="donut" data-doi="doi.org/10.3389/fgene.2020.603264" data-hide-no-mentions="true" class="altmetric-embed"></div>
{{< /rawhtml >}}
### Reference

Generating Ensembles of Gene Regulatory Networks to Assess Robustness of Disease Modules. 

James T. Lim, Chen Chen, Adam D. Grant, Megha Padi.

Frontiers in Genetics

[doi.org/10.3389/fgene.2020.603264](https://www.frontiersin.org/articles/10.3389/fgene.2020.603264/full).

### Abstract

The use of biological networks such as protein-protein interaction and transcriptional regulatory networks is becoming an integral part of biological research in the genomics era. However, these networks are not static, and during phenotypic transitions like disease onset, they can acquire new “communities” of genes that carry out key cellular processes. Changes in community structure can be detected by maximizing a modularity-based score, but because biological systems and network inference algorithms are inherently noisy, it remains a challenge to determine whether these changes represent real cellular responses or whether they appeared by random chance. Here, we introduce Constrained Random Alteration of Network Edges (CRANE), a computational method that samples networks with fixed node strengths to identify a null distribution and assess the robustness of observed changes in network structure. In contrast with other approaches, such as consensus clustering or established network generative models, CRANE produces more biologically realistic results and performs better in simulations. When applied to breast and ovarian cancer networks, CRANE improves the recovery of cancer-relevant GO terms while reducing the signal from non-specific housekeeping processes. CRANE is a general tool that can be applied in tandem with a variety of stochastic community detection methods to evaluate the veracity of their results.

### Implementation

[netZooR](https://github.com/netZoo/netZooR)

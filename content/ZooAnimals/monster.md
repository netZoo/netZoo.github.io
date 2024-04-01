---
title: "MONSTER"
date: 2019-04-02T08:50:52-04:00
draft: false
---

{{< rawhtml >}}
<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>
{{< /rawhtml >}}
{{< rawhtml >}}
<div data-badge-popover="right" data-badge-type="donut" data-doi="10.1186/s12918-017-0517-y" data-hide-no-mentions="true" class="altmetric-embed"></div>
{{< /rawhtml >}}
### Reference

Estimating drivers of cell state transitions using gene regulatory network models. 

Daniel Schlauch, Kimberly Glass, Craig P Hersh, Edwin K Silverman, John Quackenbush.

BMC Systems Biology

[doi.org/10.1186/s12918-017-0517-y](https://pubmed.ncbi.nlm.nih.gov/29237467/)

### Abstract

Background: Specific cellular states are often associated with distinct gene expression patterns. These states are plastic, changing during development, or in the transition from health to disease. One relatively simple extension of this concept is to recognize that we can classify different cell-types by their active gene regulatory networks and that, consequently, transitions between cellular states can be modeled by changes in these underlying regulatory networks.

Results: Here we describe MONSTER, MOdeling Network State Transitions from Expression and Regulatory data, a regression-based method for inferring transcription factor drivers of cell state conditions at the gene regulatory network level. As a demonstration, we apply MONSTER to four different studies of chronic obstructive pulmonary disease to identify transcription factors that alter the network structure as the cell state progresses toward the disease-state.

Conclusions: We demonstrate that MONSTER can find strong regulatory signals that persist across studies and tissues of the same disease and that are not detectable using conventional analysis methods based on differential expression. An R package implementing MONSTER is available at github.com/QuackenbushLab/MONSTER.

Keywords: Chronic obstructive pulmonary disease; Gene regulatory network inference; Genomics.

### Implementation

[netZooR](https://github.com/netZoo/netZooR)

### Netbook tutorials

The following [netbooks](http://netbooks.networkmedicine.org) use MONSTER:

- netZooR:

	- Estimating state transition in yeast cell cycle using MONSTER

	- Finding drug candidates to reverse Lung Adenocarcinoma (LUAD)-induced gene regulation disruption using TCGA

	- Multiomic CCLE analysis using the Network Zoo (part of netZooPy examples but written in R)



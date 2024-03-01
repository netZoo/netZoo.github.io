---
title: "SPIDER"
date: 2018-10-02T08:49:52-04:00
draft: false
hidden: false
description: SPIDER extends the PANDA framework by incorporating DNase-Seq data to account for chromatin state for the prediction of TF binding sites. The method consists of processing DNase-Seq data to find open chromatin regions and build a “mask” matrix that is then overlaid on the TF-gene motif network to select binding sites that are available fro TF binding. This method can be applied for various biological contexts such as cell lines and tissues. Sonawane and colleagues have employed their method to model cell- type specific GRNs using DNase-Seq data from ENCODE and showed that integrating epigenetic data in SPIDER networks allows building more accurate networks.
---

{{< rawhtml >}}
<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>
{{< /rawhtml >}}
{{< rawhtml >}}
<div data-badge-popover="right" data-badge-type="donut" data-doi="doi.org/10.1101/2020.10.19.345827" data-hide-no-mentions="true" class="altmetric-embed"></div>
{{< /rawhtml >}}
### Reference

Constructing Gene Regulatory Networks using Epigenetic Data

Abhijeet Rajendra Sonawane, Dawn L. DeMeo, John Quackenbush, Kimberly Glass.

bioRxiv

[doi.org/10.1101/2020.10.19.345827](https://www.biorxiv.org/content/10.1101/2020.10.19.345827v1.abstract)

### Abstract

The biological processes that drive cellular function can be represented by a complex network of interactions between regulators (transcription factors) and their targets (genes). A cell’s epigenetic state plays an important role in mediating these interactions, primarily by influencing chromatin accessibility. However, effectively leveraging epigenetic information when constructing regulatory networks remains a challenge. We developed SPIDER, which incorporates epigenetic information (DNase-Seq) into a message passing framework in order to estimate gene regulatory networks. We validated SPIDER’s predictions using ChlP-Seq data from ENCODE and found that SPIDER networks were more accurate than other publicly available, epigenetically informed regulatory networks as well as networks based on methods that leverage epigenetic data to predict transcription factor binding sites. SPIDER was also able to improve the detection of cell line specific regulatory interactions. Notably, SPIDER can recover ChlP-seq verified transcription factor binding events in the regulatory regions of genes that do not have a corresponding sequence motif. Constructing biologically interpretable, epigenetically informed networks using SPIDER will allow us to better understand gene regulation as well as aid in the identification of cell-specific drivers and biomarkers of cellular phenotypes.

### Implementation

[netZooM](https://github.com/netZoo/netZooM), [netZooR](https://github.com/netZoo/netZooR)

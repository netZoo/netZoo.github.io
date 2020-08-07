---
title: "OTTER"
date: 2018-11-02T08:50:52-04:00
draft: false
---

{{< rawhtml >}}
<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>
{{< /rawhtml >}}
{{< rawhtml >}}
<div data-badge-popover="right" data-badge-type="donut" data-doi="10.1101/2020.06.23.167999" data-hide-no-mentions="true" class="altmetric-embed"></div>
{{< /rawhtml >}}

### Reference

Gene Regulatory Network Inference as Relaxed Graph Matching. [link](https://www.biorxiv.org/content/10.1101/2020.06.23.167999v2).

### Abstract

Gene regulatory network inference is instrumental to the discovery of genetic mechanisms driving diverse diseases, including cancer. Here, we present a theoretical framework for PANDA, an established method for gene regulatory network inference. PANDA is based on iterative message passing updates that resemble the gradient descent of an optimization problem, OTTER, which can be interpreted as relaxed inexact graph matching between a gene-gene co-expression and a protein-protein interaction matrix. The solutions of OTTER can be derived explicitly and inspire an alternative spectral algorithm, for which we can provide network recovery guarantees. We compare different solution approaches of OTTER to other inference methods using three biological data sets, which we make publicly available to offer a new application venue for relaxed graph matching in gene regulatory network inference. We find that using modern gradient descent methods with superior convergence properties solving OTTER outperforms state-of-the-art gene regulatory network inference methods in predicting binding of transcription factors to regulatory regions.

### Implementation

netZooR, netZooPy, netZooM

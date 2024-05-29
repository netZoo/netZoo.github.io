---
title: "TIGER"
date: 2018-05-02T08:50:52-04:00
draft: false
---

{{< rawhtml >}}
<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>
{{< /rawhtml >}}
{{< rawhtml >}}
<div data-badge-popover="right" data-badge-type="donut" data-doi="10.1038/s41540-024-00386-w" data-hide-no-mentions="true" class="altmetric-embed"></div>
{{< /rawhtml >}}
### Reference

Flexible modeling of regulatory networksimproves transcription factor activity estimation

Chen Chen, Megha Padi

npj Systems Biology and Applications

[doi.org/10.1038/s41540-024-00386-w](https://www.nature.com/articles/s41540-024-00386-w)

### Abstract

Transcriptional regulation plays a crucial role in determining cell fate and disease, yet inferring the key regulators from gene expression data remains a significant challenge. Existing methods for estimating transcription factor (TF) activity often rely on static TF-gene interaction databases and cannot adapt to changes in regulatory mechanisms across different cell types and disease conditions. Here, we present a new algorithm - Transcriptional Inference using Gene Expression and Regulatory data (TIGER) - that overcomes these limitations by flexibly modeling activation and inhibition events, up-weighting essential edges, shrinking irrelevant edges towards zero through a sparse Bayesian prior, and simultaneously estimating both TF activity levels and changes in the underlying regulatory network. When applied to yeast and cancer TF knock-out datasets, TIGER outperforms comparable methods in terms of prediction accuracy. Moreover, our application of TIGER to tissue- and cell-type-specific RNA-seq data demonstrates its ability to uncover differences in regulatory mechanisms. Collectively, our findings highlight the utility of modeling context-specific regulation when inferring transcription factor activities.

### Implementation

[netZooR](https://github.com/netZoo/netZooR)





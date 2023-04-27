---
title: "TIGER"
date: 2018-05-02T08:50:52-04:00
draft: true
---

{{< rawhtml >}}
<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>
{{< /rawhtml >}}
{{< rawhtml >}}
<div data-badge-popover="right" data-badge-type="donut" data-doi="10.1101/2022.12.12.520141" data-hide-no-mentions="true" class="altmetric-embed"></div>
{{< /rawhtml >}}
### Reference

Joint inference of transcription factor activity and context-specific regulatory networks

Chen Chen, Megha Padi

bioRxiv

[doi.org/10.1101/2022.12.12.520141](https://www.biorxiv.org/content/10.1101/2022.12.12.520141v1)

### Abstract


Transcriptional regulation is a critical process that determines cell fate and disease. One of the challenges in understanding transcriptional regulation is that there is no easy way to infer the main regulators from gene expression data. Many existing methods focus on estimating the activity of individual transcription factors (TFs) using static TF-gene interaction databases, but regulomes are often altered in different cell types and disease conditions. To address this problem, we developed a new algorithm – Transcriptional Inference using Gene Expression and Regulatory data (TIGER) – that leverages Bayesian matrix factorization to simultaneously infer TF regulomes and transcription factor (TF) activities from RNA-seq data. We show that, when applied to yeast, A375, and MCF7 TF knock-out datasets, TIGER can provide more accurate predictions than comparable methods. The application to single-cell RNA-seq data reveals TIGER’s potential for uncovering cell differentiation mechanisms. Our results reinforce the importance of incorporating context-specific regulation when studying the mechanisms driving disease in different cell types.

### Implementation

[netZooR](https://github.com/netZoo/netZooR)





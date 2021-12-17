---
title: "EGRET"
date: 2018-08-02T08:50:52-04:00
draft: false
---

{{< rawhtml >}}
<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>
{{< /rawhtml >}}
{{< rawhtml >}}
<div data-badge-popover="right" data-badge-type="donut" data-doi="10.1101/2021.01.18.427134" data-hide-no-mentions="true" class="altmetric-embed"></div>
{{< /rawhtml >}}
### Reference

Predicting genotype-specific gene regulatory networks

Deborah Weighill, Marouen Ben Guebila, Kimberly Glass, John Quackenbush, John Platig

bioRxiv

[doi.org/10.1101/2021.01.18.427134](https://www.biorxiv.org/content/10.1101/2021.01.18.427134v1.abstract)

### Abstract

The majority of disease-associated genetic variants are thought to have regulatory effects, including the disruption of transcription factor (TF) binding and the alteration of downstream gene expression. Identifying how a person’s genotype affects their individual gene regulatory network has the potential to provide important insights into disease etiology and to enable improved genotype-specific disease risk assessments and treatments. However, the impact of genetic variants is generally not considered when constructing gene regulatory networks. To address this unmet need, we developed EGRET (Estimating the Genetic Regulatory Effect on TFs), which infers a genotype-specific gene regulatory network (GRN) for each individual in a study population by using message passing to integrate genotype-informed TF motif predictions - derived from individual genotype data, the predicted effects of variants on TF binding and gene expression, and TF motif predictions - with TF protein-protein interactions and gene expression. Comparing EGRET networks for two blood-derived cell lines identified genotype-associated cell-line specific regulatory differences which were subsequently validated using allele-specific expression, chromatin accessibility QTLs, and differential TF binding from ChIP-seq. In addition, EGRET GRNs for three cell types across 119 individuals captured regulatory differences associated with disease in a cell-type-specific manner. Our analyses demonstrate that EGRET networks can capture the impact of genetic variants on complex phenotypes, supporting a novel fine-scale stratification of individuals based on their genetic background. EGRET is available through the Network Zoo R package (netZooR v0.9; netzoo.github.io).

### Implementation

[netZooR](https://github.com/netZoo/netZooR)

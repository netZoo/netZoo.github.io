+++
title: "EGRET"
date: 2018-08-02T08:50:52-04:00
draft: false
hidden: true
+++

{{< rawhtml >}}
<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>
{{< /rawhtml >}}
{{< rawhtml >}}
<div data-badge-popover="right" data-badge-type="donut" data-doi="10.1101/gr.275107.120" data-hide-no-mentions="true" class="altmetric-embed"></div>
{{< /rawhtml >}}
### Reference

Predicting genotype-specific gene regulatory networks

Deborah Weighill, Marouen Ben Guebila, Kimberly Glass, John Quackenbush, John Platig

Genome Research

[doi.org/10.1101/gr.275107.120](https://genome.cshlp.org/content/early/2022/02/21/gr.275107.120)

### Abstract

Understanding how each person's unique genotype influences their individual patterns of gene regulation has the potential to improve our understanding of human health and development, and to refine genotype-specific disease risk assessments and treatments. However, the effects of genetic variants are not typically considered when constructing gene regulatory networks, despite the fact that many disease-associated genetic variants are thought to have regulatory effects, including the disruption of transcription factor (TF) binding. We developed EGRET (Estimating the Genetic Regulatory Effect on TFs), which infers a genotype-specific gene regulatory network for each individual in a study population. EGRET begins by constructing a genotype-informed TF-gene prior network derived using TF motif predictions, expression quantitative trait locus (eQTL) data, individual genotypes, and the predicted effects of genetic variants on TF binding. It then uses a technique known as message passing to integrate this prior network with gene expression and TF protein–protein interaction data to produce a refined, genotype-specific regulatory network. We used EGRET to infer gene regulatory networks for two blood-derived cell lines and identified genotype-associated, cell line–specific regulatory differences that we subsequently validated using allele-specific expression, chromatin accessibility QTLs, and differential ChIP-seq TF binding. We also inferred EGRET networks for three cell types from each of 119 individuals and identified cell type–specific regulatory differences associated with diseases related to those cell types. EGRET is, to our knowledge, the first method that infers networks reflective of individual genetic variation in a way that provides insight into the genetic regulatory associations driving complex phenotypes.

### Implementation

[netZooR](https://github.com/netZoo/netZooR)

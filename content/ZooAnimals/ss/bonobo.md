---
title: "BONOBO"
date: 2019-06-01T08:50:52-04:00
draft: false
description: "BONOBO is a scalable Bayesian model for deriving individual sample-specific co-expression networks by recognizing variations in molecular interactions across individuals. For every sample, BONOBO assumes a Gaussian distribution on the log-transformed centered gene expression and a conjugate prior distribution on the sample-specific co-expression matrix constructed from all other samples in the data. Combining the sample-specific gene expression with the prior distribution, BONOBO yields a closed-form solution for the posterior distribution of the sample-specific co-expression matrices."
---

{{< rawhtml >}}
<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>
{{< /rawhtml >}}
{{< rawhtml >}}
<div data-badge-popover="right" data-badge-type="donut" data-doi="10.1101/gr.279117.124" data-hide-no-mentions="true" class="altmetric-embed"></div>
{{< /rawhtml >}}
### Reference

Bayesian inference of sample-specific coexpression networks

Enakshi Saha, Viola Fanfani, Panagiotis Mandros, Marouen Ben Guebila, Jonas Fischer, Katherine Hoff-Shutta, Dawn Lisa DeMeo, Camila Lopes-Ramos, John Quackenbush

Genome Research

[doi.org/10.1101/gr.279117.124](https://genome.cshlp.org/content/early/2024/08/10/gr.279117.124.abstract)

### Abstract

Gene regulatory networks (GRNs) are effective tools for inferring complex interactions between molecules that regulate biological processes and hence can provide insights into drivers of biological systems. Inferring coexpression networks is a critical element of GRN inference, as the correlation between expression patterns may indicate that genes are coregulated by common factors. However, methods that estimate coexpression networks generally derive an aggregate network representing the mean regulatory properties of the population and so fail to fully capture population heterogeneity. BONOBO (Bayesian Optimized Networks Obtained By assimilating Omics data) is a scalable Bayesian model for deriving individual sample-specific coexpression matrices that recognizes variations in molecular interactions across individuals. For each sample, BONOBO assumes a Gaussian distribution on the log-transformed centered gene expression and a conjugate prior distribution on the sample-specific coexpression matrix constructed from all other samples in the data. Combining the sample-specific gene coexpression with the prior distribution, BONOBO yields a closed-form solution for the posterior distribution of the sample-specific coexpression matrices, thus allowing the analysis of large datasets. We demonstrate BONOBO's utility in several contexts, including analyzing gene regulation in yeast transcription factor knockout studies, the prognostic significance of miRNA-mRNA interaction in human breast cancer subtypes, and sex differences in gene regulation within human thyroid tissue. We find that BONOBO outperforms other methods that have been used for sample-specific coexpression network inference and provides insight into individual differences in the drivers of biological processes.

### Implementation

[netZooPy](https://github.com/netZoo/netZooPy)

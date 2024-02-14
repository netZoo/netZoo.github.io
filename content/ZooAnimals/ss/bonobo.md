---
title: "BONOBO"
date: 2019-06-01T08:50:52-04:00
draft: false
---

{{< rawhtml >}}
<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>
{{< /rawhtml >}}
{{< rawhtml >}}
<div data-badge-popover="right" data-badge-type="donut" data-doi="10.1101/2023.11.16.567119" data-hide-no-mentions="true" class="altmetric-embed"></div>
{{< /rawhtml >}}
### Reference

Bayesian Optimized sample-specific Networks Obtained By Omics data (BONOBO)

Enakshi Saha, Viola Fanfani, Panagiotis Mandros, Marouen Ben-Guebila, Jonas Fischer, Katherine Hoff-Shutta, Kimberly Glass, Dawn Lisa DeMeo, Camila Lopes-Ramos, John Quackenbush

bioRxiv

[doi.org/10.1101/2023.11.16.567119](https://www.biorxiv.org/content/10.1101/2023.11.16.567119v1.abstract).

### Abstract

Gene regulatory networks (GRNs) are effective tools for inferring complex interactions between molecules that regulate biological processes and hence can provide insights into drivers of biological systems. Inferring co-expression networks is a critical element of GRN inference as the correlation between expression patterns may indicate that genes are coregulated by common factors. However, methods that estimate co-expression networks generally derive an aggregate network representing the mean regulatory properties of the population and so fail to fully capture population heterogeneity. To address these concerns, we introduce BONOBO (Bayesian Optimized Networks Obtained By assimilating Omics data), a scalable Bayesian model for deriving individual sample-specific co-expression networks by recognizing variations in molecular interactions across individuals. For every sample, BONOBO assumes a Gaussian distribution on the log-transformed centered gene expression and a conjugate prior distribution on the sample-specific co-expression matrix constructed from all other samples in the data. Combining the sample-specific gene expression with the prior distribution, BONOBO yields a closed-form solution for the posterior distribution of the sample-specific co-expression matrices, thus making the method extremely scalable. We demonstrate the utility of BONOBO in several contexts, including analyzing gene regulation in yeast transcription factor knockout studies, prognostic significance of miRNA-mRNA interaction in human breast cancer subtypes, and sex differences in gene regulation within human thyroid tissue. We find that BONOBO outperforms other sample-specific co-expression network inference methods and provides insight into individual differences in the drivers of biological processes.

### Implementation

[netZooR](https://github.com/netZoo/netZooR)

### Netbook tutorials

The following [netbooks](http://netbooks.networkmedicine.org) use BONOBO:

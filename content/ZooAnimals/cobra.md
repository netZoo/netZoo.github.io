---
title: "COBRA"
date: 2018-04-02T08:50:52-04:00
draft: false
---

{{< rawhtml >}}
<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>
{{< /rawhtml >}}
{{< rawhtml >}}
<div data-badge-popover="right" data-badge-type="donut" data-doi="10.1101/2023.12.28.573533" data-hide-no-mentions="true" class="altmetric-embed"></div>
{{< /rawhtml >}}
### Reference

Higher-order correction of persistent batch effects in correlation networks

Soel Micheletti, Daniel Schlauch, John Quackenbush, Marouen Ben Guebila

bioRxiv

[doi.org/10.1101/2023.12.28.573533](https://www.biorxiv.org/content/10.1101/2023.12.28.573533v1.abstract)

### Abstract

Systems biology methods often rely on correlations in gene expression profiles to infer co-expression networks, commonly used as input for gene regulatory network inference or to identify functional modules of co-expressed or co-regulated genes. While systematic biases, including batch effects, are known to induce spurious associations and confound differential gene expression analyses (DE), the impact of batch effects on gene co-expression has not been fully explored. Methods have been developed to adjust expression values, ensuring conditional independence of mean and variance from batch or other covariates for each gene. These adjustments have been shown to improve the fidelity of DE analysis. However, these methods do not address the potential for spurious differential co-expression (DC) between groups. Consequently, uncorrected, artifactual DC can skew the correlation structure, leading network inference methods that use gene co-expression to identify false, nonbiological associations, even when the input data is corrected using standard batch correction.

In this work, we demonstrate the persistence of confounders in covariance after standard batch correction using synthetic and real-world gene expression data examples. Subsequently, we introduce Co-expression Batch Reduction Adjustment (COBRA), a method for computing a batch-corrected gene co-expression matrix based on estimating a conditional covariance matrix. COBRA estimates a reduced set of parameters expressing the co-expression matrix as a function of the sample covariates, allowing control for continuous and categorical covariates. COBRA is computationally efficient, leveraging the inherently modular structure of genomic data to estimate accurate gene regulatory associations and facilitate functional analysis for high-dimensional genomic data.

### Implementation

[netZooR](https://github.com/netZoo/netZooR), [netZooPy](https://github.com/netZoo/netZooPy)





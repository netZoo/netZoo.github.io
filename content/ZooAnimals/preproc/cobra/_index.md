---
title: "COBRA"
date: 2018-04-02T08:50:52-04:00
draft: false
description: COBRA is method for correction of high-order batch effects such as those that persist in co-expression networks. Batch effects and other covariates are known to induce spurious associations in co-expression networks and confound differential gene expression analyses. These effects are corrected for using various methods prior to downstream analyses such as the inference of co-expression networks and computing differences between them. In differential co-expression analysis, the pairwise joint distribution of genes is considered rather than independently analyzing the distribution of expression levels for each individual gene. Computing co-expression matrices after standard batch correction on gene expression data is not sufficient to account for the possibility of batch-induced changes in the correlation between genes as existing batch correction methods act solely on the marginal distribution of each gene. Consequently, uncorrected, artifactual differential co-expression can skew the correlation structure such that network-based methods that use gene co-expression can produce false, nonbiological associations even using data corrected using standard batch correction. Co-expression Batch Reduction Adjustment (COBRA) addresses this question by computing a batch-corrected gene co-expression matrix based on estimating a conditional covariance matrix. COBRA estimates a reduced set of parameters that express the co-expression matrix as a function of the sample covariates and can be used to control for continuous and categorical covariates. The method is computationally fast and makes use of the inherently modular structure of genomic data to estimate accurate gene regulatory associations and enable functional analysis for high-dimensional genomic data.
---

{{< rawhtml >}}
<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>
{{< /rawhtml >}}
{{< rawhtml >}}
<div data-badge-popover="right" data-badge-type="donut" data-doi="10.1093/bioinformatics/btae531" data-hide-no-mentions="true" class="altmetric-embed"></div>
{{< /rawhtml >}}
### Reference

Higher-order correction of persistent batch effects in correlation networks

Soel Micheletti, Daniel Schlauch, John Quackenbush, Marouen Ben Guebila

OUP Bioinformatics

[doi.org/10.1093/bioinformatics/btae531](https://academic.oup.com/bioinformatics/advance-article/doi/10.1093/bioinformatics/btae531/7748404?login=false)

### Abstract

Motivation: Systems biology analyses often use correlations in gene expression profiles to infer co-expression networks that are then used as input for gene regulatory network inference or to identify functional modules of co-expressed or putatively co-regulated genes. While systematic biases, including batch effects, are known to induce spurious associations and confound differential gene expression analyses (DE), the impact of batch effects on gene co-expression has not been fully explored. Methods have been developed to adjust expression values, ensuring conditional independence of mean and variance from batch or other covariates for each gene, resulting in improved fidelity of DE analysis. However, such adjustments do not address the potential for spurious differential co-expression (DC) between groups. Consequently, uncorrected, artifactual DC can skew the correlation structure, leading to the identification of false, non-biological associations, even when the input data is corrected using standard batch correction.

Results: In this work, we demonstrate the persistence of confounders in covariance after standard batch correction using synthetic and real-world gene expression data examples. We then introduce Co-expression Batch Reduction Adjustment (COBRA), a method for computing a batch-corrected gene co-expression matrix based on estimating a conditional covariance matrix. COBRA estimates a reduced set of parameters expressing the co-expression matrix as a function of the sample covariates, allowing control for continuous and categorical covariates. COBRA is computationally efficient, leveraging the inherently modular structure of genomic data to estimate accurate gene regulatory associations and facilitate functional analysis for high-dimensional genomic data.

Availability and Implementation: COBRA is available under the GLP3 open source license in R and Python in netZoo (https://netzoo.github.io)

### Implementation

[netZooR](https://github.com/netZoo/netZooR), [netZooPy](https://github.com/netZoo/netZooPy)





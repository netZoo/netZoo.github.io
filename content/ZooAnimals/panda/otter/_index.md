---
title: "OTTER"
date: 2018-11-02T08:50:52-04:00
draft: false
description: 'OTTER is a GRN inference method based on the idea that observed biological data (PPI data and gene co-expression data) are projections of a bipartite GRN between TFs and genes. Specifically, PPI data represent the projection of the GRN onto the TF-TF space and gene co-expression data represent the projection of the GRN onto the gene-gene space. OTTER reframes the problem of GRN inference as a problem of relaxed graph matching and finds a GRN that has optimal agreement with the observed PPI and coexpression data. The OTTER objective function is tunable in two ways: first, one can prioritize matching the PPI data or the coexpression data more heavily depending on one's confidence in the data source; second, there is a regularization parameter that can be applied to induce sparsity on the estimated GRN. The OTTER objective function can be solved using spectral decomposition techniques and gradient descent; the latter is shown to be closely related to the PANDA message-passing approach (Glass et al. 2013).'
---

{{< rawhtml >}}
<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>
{{< /rawhtml >}}
{{< rawhtml >}}
<div data-badge-popover="right" data-badge-type="donut" data-doi="10.1101/2020.06.23.167999" data-hide-no-mentions="true" class="altmetric-embed"></div>
{{< /rawhtml >}}

### Reference

Gene Regulatory Network Inference as Relaxed Graph Matching. 

Deborah Weighill, Marouen Ben Guebila, Camila Lopes-Ramos, Kimberly Glass, John Quackenbush, John Platig, Rebekka Burkholz.

Proceedings of the AAAI Conference on Artificial Intelligence

[doi.org/10.1101/2020.06.23.167999](https://ojs.aaai.org/index.php/AAAI/article/view/17230).

### Abstract

Gene regulatory network inference is instrumental to the discovery of genetic mechanisms driving diverse diseases, including cancer. Here, we present a theoretical framework for PANDA, an established method for gene regulatory network inference. PANDA is based on iterative message passing updates that resemble the gradient descent of an optimization problem, OTTER, which can be interpreted as relaxed inexact graph matching between a gene-gene co-expression and a protein-protein interaction matrix. The solutions of OTTER can be derived explicitly and inspire an alternative spectral algorithm, for which we can provide network recovery guarantees. We compare different solution approaches of OTTER to other inference methods using three biological data sets, which we make publicly available to offer a new application venue for relaxed graph matching in gene regulatory network inference. We find that using modern gradient descent methods with superior convergence properties solving OTTER outperforms state-of-the-art gene regulatory network inference methods in predicting binding of transcription factors to regulatory regions.

### Supplementary data

Several OTTER networks are available in [GRAND](https://grand.networkmedicine.org/cancers/) database. In addition, the raw data for reconstruction and benchmarking of the networks are provided below.

| File name                 | Description | Link |
|---------------------------|-------------|-------|
| expressed_genes_tissue.txt | Column (gene) names of the gene regulatory matrix W or the initial guess W0. They are also the node names of the correlation matrix C. | [breast](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/DataS1_Breast/expressed_genes_breast.txt), [cervix](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/DataS2_Cervix/expressed_genes_cervix.txt), [liver](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/DataS3_Liver/expressed_genes_liver.txt), [liver_tcga_gtex](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/expressed_genes_liver_TCGA_and_GTEx.txt) |
| expressed_tf_names_tissue.txt | Row (TF) names of the gene regulatory matrix W or the initial guess W0. They are also the node names of the protein-protein interaction matrix P. | [breast](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/DataS1_Breast/expressed_tf_names_breast.txt), [cervix](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/DataS2_Cervix/expressed_tf_names_cervix.txt), [liver](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/DataS3_Liver/expressed_tf_names_liver.txt), [liver_tcga_gtex](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/expressed_tf_names_liver_TCGA_and_GTEx.txt) |
| motif_prior_matrix_tissue_otter.txt | Initial gene regulatory network W0, which was constructed based on TF binding motifs in the human reference genome. Row names: TF names in order of file expressed_tf_names_tissue.txt Column names: Gene names in order of file expressed_genes_tissue.txt | [breast](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/DataS1_Breast/motif_prior_matrix_breast.txt), [cervix](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/DataS2_Cervix/motif_prior_matrix_cervix.txt), [liver](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/DataS3_Liver/motif_prior_matrix_liver.txt), [liver_tcga_gtex](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/motif_prior_matrix_liver_TCGA_and_GTEx.txt) |
| PPI_matrix_tissue.txt | Protein-protein interaction matrix P. The node names are provided in the file expressed_tf_names_tissue.txt | [breast](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/PPI_matrix_breast.txt), [cervix](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/PPI_matrix_cervix.txt), [liver](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/PPI_matrix_bliver.txt), [liver_tcga_gtex](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/PPI_matrix_liver_TCGA_and_GTEx.txt) |
| tcga_tissue_TPM_otter.txt | Gene expression data. Columns refer two samples (i.e. people) and rows to genes. The gene names are defined in expressed_genes_tissue.txt. This data is used to compute the correlation matrix C. | [breast](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/DataS1_Breast/tcga_breast_TPM_otter.txt), [cervix](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/DataS2_Cervix/tcga_cervix_TPM_otter.txt), [tcga_liver](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/DataS3_Liver/tcga_liver_TPM_otter.txt)|
| corTissue.csv | Correlation matrix C. Rows and columns refer to genes with names defined in expressed_genes_tissue.txt |[breast](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/corBreast.csv), [cervix](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/corCervix.csv), [liver](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/corLiver.csv) |
| chipseq_postive_edges_tissue.txt | Validation set. Existing edges between TFs and genes. All TFs in the first column are tested with all genes. Thus, if an edge between any TFs in the first column and any other gene is not listed, it was not measured and counts as non-existent in the validation. | [breast](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/DataS1_Breast/chipseq_postive_edges_breast.txt), [cervix](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/DataS2_Cervix/chipseq_postive_edges_cervix.txt), [liver](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/DataS3_Liver/chipseq_postive_edges_liver.txt) |
| otterTissue.txt | Inferred gene regulatory network by optimizing OTTER with gradient descent. | [breast](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/otterBreast.csv), [cervix](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/otterCervix.csv), [liver](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/otterLiver.csv) |
| otterLiverTCGA.csv | Inferred gene regulatory network by optimizing OTTER with gradient descent. Liver cancer tissue. For comparison with the normal tissue network (otterLiverGTEX.csv), it has the same set of nodes. |  [liver_tcga](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/otterLiverTCGA.csv) |
| otterLiverGTEX.csv | Inferred gene regulatory network by optimizing OTTER with gradient descent. Normal liver tissue. For comparison with the liver cancer tissue network (otterLiverTCGA.csv), it has the same set of nodes. |  [liver_gtex](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/otterLiverGTEX.csv) |
| Supplementary_Figures.zip | Result figures of GO term enrichment analysis comparing TCGA and GTEx OTTER networks | [Supplementary figures](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/Supplementary_Figures.zip)
| Supplementary_Tables.zip  | Result tables of GO term enrichment analysis comparing TCGA and GTEx OTTER networks | [Supplementary tables](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/Supplementary_Tables.zip)
| Otter_AAAI2021-12.pdf | Supplementary material file | [Supplementary material](https://netzoo.s3.us-east-2.amazonaws.com/supData/otter/Otter_AAAI2021-12.pdf)

### Implementation

[netZooR](https://github.com/netZoo/netZooR), [netZooPy](https://github.com/netZoo/netZooPy), [netZooM](https://github.com/netZoo/netZooM)

### Netbook tutorials

The following [netbooks](http://netbooks.networkmedicine.org) use OTTER:

- netZooR:

	- Inferring Gene Regulatory Networks from GTEx Gene Expression Data in R with OTTER

---
title: "gpuZoo"
date: 2018-09-02T08:50:52-04:00
draft: false
---

{{< rawhtml >}}
<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>
{{< /rawhtml >}}
{{< rawhtml >}}
<div data-badge-popover="right" data-badge-type="donut" data-doi="10.1101/2021.07.13.452214" data-hide-no-mentions="true" class="altmetric-embed"></div>
{{< /rawhtml >}}
### Reference

gpuZoo: Cost-effective estimation of gene regulatory networks using the Graphics Processing Unit.

Marouen Ben Guebila, Daniel C Morgan, Kimberly Glass, Marieke L. Kuijjer, Dawn L. DeMeo, John Quackenbush.

bioRxiv

[doi.org/10.1101/2021.07.13.452214](https://www.biorxiv.org/content/10.1101/2021.07.13.452214v1).

### Abstract

Gene regulatory network inference allows for the study of transcriptional control to identify the alteration of cellular processes in human diseases. Our group has developed several tools to model a variety of regulatory processes, including transcriptional (PANDA, SPIDER) and post-transcriptional (PUMA) gene regulation, and gene regulation in individual samples (LIONESS). These methods work by performing repeated operations on data matrices in order to integrate information across multiple lines of biological evidence. This limits their use for large-scale genomic studies due to the associated high computational burden. To address this limitation, we developed gpuZoo, which includes GPU-accelerated implementations of these algorithms. The runtime of the gpuZoo implementation in MATLAB and Python is up to 61 times faster and 28 times less expensive than the multi-core CPU implementation of the same methods. gpuZoo takes advantage of the modern multi-GPU device architecture to build a population of sample-specific gene regulatory networks with similar runtime and cost improvements by combining GPU acceleration with an efficient on-line derivation. Taken together, gpuZoo allows parallel and on-line gene regulatory network inference in large-scale genomic studies with cost-effective performance. gpuZoo is available in MATLAB through the netZooM package https://github.com/netZoo/netZooM and in Python through the netZooPy package https://github.com/netZoo/netZooPy.

### Supplementary data

This is the data used for the benchmarks of gpuZoo. 

|Model                        | Motif | PPI  | Expression   | Mode | TFs | Genes |
|-----------------------------|-------|------|--------------|------|-----|-------|
|Small network                | [download](https://granddb.s3.amazonaws.com/gpuPANDA/Hugo_motifCellLine_reduced.txt) | [download](https://granddb.s3.amazonaws.com/gpuPANDA/ppi2015_freezeCellLine.txt) | [download](https://granddb.s3.amazonaws.com/optPANDA/expression/Hugo_exp1_lcl.txt) | Intersection | 652  | 1000  |
|Protein-coding genes network | [download](https://granddb.s3.amazonaws.com/optPANDA/motifs/Hugo_motifCellLine.txt)  | [download](https://granddb.s3.amazonaws.com/gpuPANDA/ppi2015_freezeCellLine.txt) | [download](https://granddb.s3.amazonaws.com/optPANDA/expression/Hugo_exp1_lcl.txt) | Union        | 652  | 27149 |
|Transcript network           | [download](https://granddb.s3.amazonaws.com/gpuPANDA/motif_complete_reduced.txt)     | [download](https://granddb.s3.amazonaws.com/optPANDA/ppi/ppi_complete.txt) | [download](https://granddb.s3.amazonaws.com/optPANDA/expression/THP-1.tsv) | Union        | 1603 | 43698 |

### Implementation

[netZooPy](https://github.com/netZoo/netZooPy), [netZooM](https://github.com/netZoo/netZooM)

### GitHub repository

To reproduce the benchmarks, check the [github repository gpuZoo](https://github.com/QuackenbushLab/gpuzoo).

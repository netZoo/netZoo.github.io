---
title: "gpuZoo"
date: 2018-09-02T08:50:52-04:00
draft: false
---

{{< rawhtml >}}
<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>
{{< /rawhtml >}}
{{< rawhtml >}}
<div data-badge-popover="right" data-badge-type="donut" data-doi="10.1093/nargab/lqac002" data-hide-no-mentions="true" class="altmetric-embed"></div>
{{< /rawhtml >}}
### Reference

gpuZoo: Cost-effective estimation of gene regulatory networks using the Graphics Processing Unit.

Marouen Ben Guebila, Daniel C Morgan, Kimberly Glass, Marieke L. Kuijjer, Dawn L. DeMeo, John Quackenbush.

NAR Genomics and Biofinformatics

[doi.org/10.1093/nargab/lqac002](https://academic.oup.com/nargab/article/4/1/lqac002/6524305?login=false).

### Abstract

Gene regulatory network inference allows for the modeling of genome-scale regulatory processes that are altered during development, in disease, and in response to perturbations. Our group has developed a collection of tools to model various regulatory processes, including transcriptional (PANDA, SPIDER) and post-transcriptional (PUMA) gene regulation, as well as gene regulation in individual samples (LIONESS). These methods work by postulating a network structure and then optimizing that structure to be consistent with multiple lines of biological evidence through repeated operations on data matrices. Although our methods are widely used, the corresponding computational complexity, and the associated costs and run times, do limit some applications. To improve the cost/time performance of these algorithms, we developed gpuZoo which implements GPU-accelerated calculations, dramatically improving the performance of these algorithms. The runtime of the gpuZoo implementation in MATLAB and Python is up to 61 times faster and 28 times less expensive than multi-core CPU implementation of the same methods. gpuZoo is available in MATLAB through the netZooM package https://github.com/netZoo/netZooM and in Python through the netZooPy package https://github.com/netZoo/netZooPy.

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

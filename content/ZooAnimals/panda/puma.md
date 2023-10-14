---
title: "PUMA"
date: 2019-02-02T08:50:52-04:00
draft: false
hidden: true
---

{{< rawhtml >}}
<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>
{{< /rawhtml >}}
{{< rawhtml >}}
<div data-badge-popover="right" data-badge-type="donut" data-doi="10.1093/bioinformatics/btaa571" data-hide-no-mentions="true" class="altmetric-embed"></div>
{{< /rawhtml >}}
### Reference

PUMA: PANDA Using MicroRNA Associations. 

Marieke L Kuijjer, Maud Fagny, Alessandro Marin, John Quackenbush, Kimberly Glass.

OUP Bioinformatics

[doi.org/10.1093/bioinformatics/btaa571](https://academic.oup.com/bioinformatics/article/doi/10.1093/bioinformatics/btaa571/5858977).

### Abstract

Conventional methods to analyze genomic data do not make use of the interplay between multiple factors, such as between microRNAs (miRNAs) and the mRNA transcripts they regulate, and thereby often fail to identify the cellular processes that are unique to specific tissues. We developed PUMA (PANDA Using MicroRNA Associations), a computational tool that uses message passing to integrate a prior network of miRNA target predictions with target gene co-expression information to model genome-wide gene regulation by miRNAs. We applied PUMA to 38 tissues from the Genotype-Tissue Expression (GTEx) project, integrating RNA-Seq data with two different miRNA target predictions priors, built on predictions from TargetScan and miRanda, respectively. We found that while target predictions obtained from these two different resources are considerably different, PUMA captures similar tissue-specific miRNA-target regulatory interactions in the different network models. Furthermore, the tissue-specific functions of miRNAs we identified based on regulatory profiles (available at: https://kuijjer.shinyapps.io/puma_gtex/) are highly similar between networks modeled on the two target prediction resources. This indicates that PUMA consistently captures important tissue-specific miRNA regulatory processes. In addition, using PUMA we identified miRNAs regulating important tissue-specific processes that, when mutated, may result in disease development in the same tissue. PUMA is available in C ++, MATLAB, and Python on GitHub (https://github.com/kuijjerlab and https://netzoo.github.io/).

### Implementation

[netZooPy](https://github.com/netZoo/netZooPy), [netZooM](https://github.com/netZoo/netZooM), [netZooC](https://github.com/netZoo/netZooC), [netZooR](https://github.com/netZoo/netZooR)

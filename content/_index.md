
+++
title = "The network zoo"
+++

# The network zoo

{{< rawhtml >}}

<div align="center">
<!-- Place this tag where you want the button to render. -->
<a class="github-button" href="https://github.com/netZoo/netZooR" data-color-scheme="no-preference: light; light: light; dark: light;" data-icon="octicon-star" data-size="large" data-show-count="true" aria-label="Star netZoo/netZooR on GitHub">netZooR</a>
<a class="github-button" href="https://github.com/netZoo/netZooPy" data-color-scheme="no-preference: light; light: light; dark: light;" data-icon="octicon-star" data-size="large" data-show-count="true" aria-label="Star netZoo/netZooPy on GitHub">netZooPy</a>
<a class="github-button" href="https://github.com/netZoo/netZooM" data-color-scheme="no-preference: light; light: light; dark: light;" data-icon="octicon-star" data-size="large" data-show-count="true" aria-label="Star netZoo/netZooM on GitHub">netZooM</a>
<a class="github-button" href="https://github.com/netZoo/netZooC" data-color-scheme="no-preference: light; light: light; dark: light;" data-icon="octicon-star" data-size="large" data-show-count="true" aria-label="Star netZoo/netZooC on GitHub">netZooC</a>
<a class="github-button" href="https://github.com/netZoo/netbooks" data-color-scheme="no-preference: light; light: light; dark: light;" data-icon="octicon-star" data-size="large" data-show-count="true" aria-label="Star netZoo/netZooC on GitHub">Netbooks</a>
</div>
{{< /rawhtml >}}

netZoo{R,Py,M,C} is a menagerie of network biology methods for the inference and analysis of gene regulatory networks. Implementation details and use cases in 

> The Network Zoo: a multilingual package for the inference and analysis of gene regulatory networks. Ben Guebila et al, 2023. Genome Biology. [doi:10.1186/s13059-023-02877-1](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-023-02877-1)

If you use netZoo, please cite us using the following format:

> We used DRAGON (Shutta, Weighill et al, 2023) as implemented in netZooPy v 1.5 (Ben Guebila et al, 2023) and Python v 3.9.

See the following citation [example](https://www.sciencedirect.com/science/article/pii/S2211124720307762) for reference.

A collection of tutorials hosted on the cloud is available without the need to install any depedency on [Netbooks](https://netbooks.networkmedicine.org/). It is possible to  run these tutorials on a local computer using [R markdown](https://netzoo.github.io/netZooR/), [Jupyter notebooks](https://netzoopy.readthedocs.io/en/latest/tutos/index.html), and [LiveScript](https://netzoom.readthedocs.io/en/latest/tutos/index.html).

### netZoo ecosystem

- The software tools are developed in [netZoo](https://github.com/netZoo). [Publication](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-023-02877-1)

- Continuous integration is enabled through [ZooKeeper](https://github.com/netZoo/netZooR/actions) (Travis-CI and GitHub actions). 

- A set of networks generated using netZoo tools are hosted in [GRAND](https://grand.networkmedicine.org) database. [Publication](https://academic.oup.com/nar/advance-article/doi/10.1093/nar/gkab778/6368528) 

- netZoo tutorials are distributed through bundled hardware and software environments using [Netbooks](https://netbooks.networkmedicine.org). [Publication](https://www.nature.com/articles/s41592-022-01479-2)

- Methods are also available through a web interface through [netzoocloud](https://netzoocloud.networkmedicine.org/) (beta)

- To ask questions or to provide feedback or ideas, please use our community channel for [discussions](https://github.com/netZoo/netZooR/discussions).

### Packages

R: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; {{% button href="https://github.com/netZoo/netZooR" icon="fab fa-github" %}}netZooR{{% /button %}}

Python: &nbsp; &nbsp; {{% button href="https://github.com/netZoo/netZooPy" icon="fab fa-github" %}}netZooPy{{% /button %}}

MATLAB: &nbsp; {{% button href="https://github.com/netZoo/netZooM" icon="fab fa-github" %}}netZooM{{% /button %}}

C: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; {{% button href="https://github.com/netZoo/netZooC" icon="fab fa-github" %}}netZooC{{% /button %}}

{{% notice note %}}
Following the update of python-igraph package from 0.7.1.post6 to newer versions, the assignemnt of communities in condor as implemented in netZooPy [has changed](https://github.com/netZoo/netZooPy/issues/82).
netZooPy >= 0.7.2 imports newer versions of python-igraph > 0.7.1.post6, therefore the results of condor in netZooPy < 0.7.2 and netZooPy >= 0.7.2 could be different.
{{% /notice  %}}

{{% notice note %}}
Starting from netZooM 0.4.1, netZooPy 0.5.1, and netZooR 0.6.1 (which includes pandaR 1.19.4), the default data processing step in PANDA has changed. Data processing was modified in
all platforms to give the same output as PANDA in netZooC, which adds rows of zeros if a gene/TF is missing in at least one prior (expression, motif, ppi). The previous behavior
can be accessed through the 'legacy' option in the variable mode. The option 'intersection' of the variable mode removes missing TFs/genes if they are absent from at least one
prior.
{{% /notice %}}

### Live status

Continuous integration (ZooKeeper) is enabled for netZoo using [Travis](https://travis-ci.com/github/netZoo) for netZooC and netZooM,  and [GitHub actions](https://github.com/netZoo/netZooR/actions) for netZooR and netZooPy.

R &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - [build status](http://zookeeper.networkmedicine.org/job/netZooR_Ubuntu18.04/lastBuild/) ([Ubuntu](https://github.com/netZoo/netZooR/actions), [Macos](https://github.com/netZoo/netZooR/actions)) - [coverage](https://codecov.io/gh/netZoo/netZooR)

Python &nbsp; - [build status](https://github.com/netZoo/netZooPy/actions) ([Ubuntu](https://github.com/netZoo/netZooPy/actions), [Macos](https://github.com/netZoo/netZooPy/actions)) - [coverage](https://codecov.io/gh/netZoo/netZooPy)

MATLAB - [build status](https://github.com/netZoo/netZooM/actions) ([Ubuntu](https://github.com/netZoo/netZooM/actions)) - [coverage](https://codecov.io/gh/netZoo/netZooM)

C &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - [build status](https://travis-ci.com/netZoo/netZooC) ([Ubuntu](https://travis-ci.com/netZoo/netZooC/jobs/553452530), [Macos](https://travis-ci.com/netZoo/netZooC/jobs/553452531)) - [coverage](https://codecov.io/gh/netZoo/netZooC)

{{% notice info %}}
netZoo{R,Py,M,C} is a community maintained package licensed under [GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).
{{% /notice %}}

### Labs

![labs](https://github.com/netZoo/netZoo.github.io/blob/master/docs/images/labs-01.png?raw=true "Labs")

{{< rawhtml >}}
<!-- Place this tag in your head or just before your close body tag. -->
<script async defer src="https://buttons.github.io/buttons.js"></script>
{{< /rawhtml >}}

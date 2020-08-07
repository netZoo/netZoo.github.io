
+++
title = "The network zoo"
+++

# The network zoo

netZoo{R,Py,M,C} is a network biology package for the reconstruction and analysis of gene regulatory networks.

If you use the netZoo, please cite us using the following format.

> We used ALPACA (Padi and Quackenbush 2018) as implemented in netZooR (v 0.7.2; netzoo.github.io) using R (v 4.0.2).

See the following [example](https://www.sciencedirect.com/science/article/pii/S2211124720307762) for reference.

A collection of networks generated using the netZoo is available in [GRAND](https://grand.networkmedicine.org) database.
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

Continuous integration is enabled for netZoo using [Travis](https://travis-ci.com/github/netZoo) and [ZooKeeper](http://zookeeper.networkmedicine.org/).

R &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - [build status](http://zookeeper.networkmedicine.org/job/netZooR_Ubuntu18.04/lastBuild/) ([Ubuntu](http://zookeeper.networkmedicine.org/job/netZooR_Ubuntu18.04/)) - [coverage](https://codecov.io/gh/netZoo/netZooR)

Python &nbsp; - [build status](https://travis-ci.com/netZoo/netZooPy) ([Ubuntu](https://travis-ci.com/netZoo/netZooPy), [Macos](https://travis-ci.com/github/netZoo/netZooPy)) - [coverage](https://codecov.io/gh/netZoo/netZooPy)

MATLAB - [build status](https://travis-ci.com/netZoo/netZooM) ([Ubuntu](https://travis-ci.com/netZoo/netZooM/jobs/212762427), [Macos](https://travis-ci.com/netZoo/netZooM/jobs/212762428)) - [coverage](https://codecov.io/gh/netZoo/netZooM)

C &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - [build status](https://travis-ci.com/netZoo/netZooC) ([Ubuntu](https://travis-ci.com/netZoo/netZooC/jobs/553452530), [Macos](https://travis-ci.com/netZoo/netZooC/jobs/553452531)) - [coverage](https://codecov.io/gh/netZoo/netZooC)

{{% notice info %}}
netZoo{R,Py,M,C} is a community maintained package licensed under [GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).
{{% /notice %}}

![labs](images/labs-01.png "Labs")

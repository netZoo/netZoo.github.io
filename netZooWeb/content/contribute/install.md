---
title: "How to install"
date: 2019-07-02T08:50:52-04:00
draft: false
---

### Installation guide

To install netZoo{Py, M, C}, all you have to do is `git clone https://github.com/netZoo/netZoo{Py,M,C}.git` then to get the latest changes in your repository you need to `git pull origin master`.

You can work on the devel branch by `git checkout devel`. To update the devel branch type `git pull origin devel`.

In Python, an additional step is required to install netZooPy through `pip3 install -e .` in the either the root of devel or master branch and after each change to the source code.

In R, the installation does not require `git clone`, the `devtools` library allow to install netZooR directly from github and from either devel or master.

Please refer to the specific installation guide for each package for more details.

### Quick developer guide

If you are a developer, you will need to clone to your own fork to be able to create pull requests to netZoo. Please refer to the [contribution guide](https://netzoo.github.io/contribute/contribute/).

Make sure to have the latest changes in your local repo through `git fetch upstream` then `git merge upstream/master`.

To update the devel branch `git checkout devel` and `git fetch upstream` and `git merge upstream/devel`.

{{% notice tip %}}
Make sure to update your repository before creating a pull request or creating an issue.
{{% /notice %}}

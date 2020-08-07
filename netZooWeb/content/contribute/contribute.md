---
title: "How to contribute"
date: 2019-07-02T08:50:52-04:00
draft: false
---

## Contribution guide

The netZoo is an open-source software suite of network biology methods in R, Python, MATLAB, and C. Contributions to the netZoo can be in the form of 1) bug fixing, 2) performance 
improvment, and 3) new functions.

Each language repository has a master and a devel branch. The master branch contains the stable code of the netZoo, and the devel branch contains the code with the new features
that gets periodically merged into the master branch. New contributions of type 1) and 2) have to go through automatic tests before being integrated into the package. Contributions of 
type 3) have to be submitted with unit tests and tutorials to explain how the new function works.

### Preparing the contribution

To increase the chances of including a contribution to netZoo, please follow the instructions below.

#### New functions

New functions have to include a header that will server as documentation. Headers include a general description, description of inputs, ouputs, any notes, the authors list, the date, and 
a reference to the publication. Please follow this [example](https://github.com/netZoo/netZooM/blob/master/netZooM/panda/panda_run.m).

To add a unit test, please include all the edge cases and the expected behavior of the function and ground truth dataset to test against. The tests should run ideally on several small examples to test several edge cases in a limited 
runtime. If a function is submitted in more than one language or if the function is a new implementation of a function that already exists in another language, there should be only one ground truth 
dataset across platform. This will ensure that the behavior of the function is the same across platforms. For example, if you're contirbuting a MATLAB implementation of PANDA, and there is an R implementation 
of PANDA, you should use the ground truth from netZooR for your test. Please check the [tests](https://github.com/netZoo/netZooPy/tree/master/tests) folder of each repo for examples.

{{% notice tip %}}
Please update your repo and make sure the tests pass locally before creating a PR. In R, please refer to the netZooR [contribution guide](https://github.com/netZoo/netZooR#contribution-and-development). 
In Python, please run `pytest` in the root of netZooPy. In Matlab, you can run the tests in the [tests](https://github.com/netZoo/netZooM/tree/master/tests) folder manually. 
{{% /notice %}}

#### Bug fixes

To fix a bug in a function, please create a new pull request with a description of the fix, and a new ground truth dataset if this relevant for the unit test.

#### Performance improvement

To improve the speed/memory usage of a function, please create a new pull request with a description of the addition and its impact on memory/speed.

### Pull requests to netZoo

The contribution model follows the standard fork-branch model on the devel branch. Contributions are submitted as pull requests (PRs).

1. fork the netZoo repo to your github

2. clone the forked repo to your computer

	`git clone https://github.com/<your_github_name>/netZoo{R,Py,M,C}.git`

3. access netZoo local folder `cd netZoo{R,Py,M,C}`

4. add a new remote typically called 'upstream' that points to the source of netZoo

	`git remote add upstream https://github.com/netZoo/netZoo{R,Py,M,C}.git`

5. switch to the devel branch, because your PR will target the devel branch

	`git checkout devel`

6. create a new branch called new-feature off of the devel branch

	`git checkout -b new-feature`

7. make the changes/additions to netZoo

8. add your changes

	`git add .`

9. commit your changes

	`git commit -m 'commit message'`

10. push your PR

	`git push origin new-feature`

11. go the netZoo website https://github.com/netZoo/netZoo{R, Py, M, C}

12. create a pull request through the pop-up

13. make sure to change the target to devel branch not the master branch

14. the PR will go through automatic tests and it will be accepted by the moderators if it passes the tests

15. if the PR does not pass the test, further changes need to be made (step 8-10)

16. once the PR integrated in the devel branch, you can delete new-feature, switch back to devel branch and update it with the new branch through

	`git checkout devel`

	`git fetch upstream`

	`git merge upstream/devel`

17. you can do the same for the master branch to update it .

{{% notice tip %}}
Delete the merged feature branch both locally and remotely.
{{% /notice %}}

## Contribution guide

The netZoo is an open-source software suite of network biology methods in R, Python, MATLAB, and C. Contributions to the netZoo can be in the form of 1) bug fixing, 2) performance 
improvment, and 3) new functions.

Each language repository has a master and a devel branch. The master branch contains the stable code of the netZoo, and the devel branch contains the code with the new features
that gets periodically merged into the master branch. New contributions of type 1) and 2) have to go through automatic tests before being integrated into the package. Contributions of 
type 3) have to be submitted with unit tests.

The contribution model follows the standard fork-branch model on the devel branch. Contributions are submitted as pull requets (PRs).

1. fork the netZoo repo to your github

2. clone the forked repo to your computer

3. add a new remote typically called 'upstream' that points to the source of netZoo

	`git remote add upstream https://github.com/netZoo/netZoo{R,Py,M,C}.git`

4. switch to the devel branch, because your PR will target the devel branch

	`git checkout devel`

5. create a new branch called new-feature off of the devel branch

	`git checkout -b new-feature`

6. make the changes/additions to netZoo

7. add your changess

	`git add .`

8. commit your changes

	`git commit -m 'commit message'`

9. push your PR

	`git push origin new-feature`

10. go the netZoo website https://github.com/netZoo/netZoo{R, Py, M, C}

11. create a pull request through the pop-up

12. make sure to change the target to devel branch not the master branch

13. the PR will go through automatic tests and it will be accepted by the moderators if it passes the tests

14. if the PR does not pass the test, further changes need to be made (step 7-9)

15. once the PR integrated in the devel branch, you can delete new-feature, switch back to devel branch and update it with the new branch through

	`git checkout devel`

	`git fetch upstream`

	`git merge usptream/devel`

16. you can do the same for the master branch to update it .

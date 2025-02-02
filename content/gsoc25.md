# Ideas List, Google Summer of Code 2025 


Welcome to the Ideas Page for the GSoC 2025, here you will find a list of possible GSoC projects for the netZoo
organization. 

**What is the netZoo project?**

The Network Zoo (netZoo) is a project spearheaded by the team of Prof. John Quackenbush at the Harvard T. Chan School of
Public Health.  The lab focuses on computational methods and analyses of how transcription factors (TFs) and genes
interact to regulate homeostasis and are disrupted in complex diseases, such as cancer or COPD. The netZoo is a
collection of open-source methods to infer gene regulatory network, conduct differential network analyses, estimate
community structure, and explore the transitions between biological states. The methods hosted in the netZoo have been
developed by the lab or close collaborators during the years and have been used in dozens of scientific publications.
The software is mostly written in R (netZooR) and Python  (netZooPy), with some exceptions in C++ and Matlab, and 
it is maintained by the lab with the goal of allowing dissemination, reproducibility, and educational purposes.

To have an idea of what is in the netZoo you can check the main paper: 
> The Network Zoo: a multilingual package for the inference and analysis of gene regulatory networks. Ben Guebila et al, 2023. Genome Biology. [doi:10.1186/s13059-023-02877-1](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-023-02877-1)

To look into the code you can refer to the main GitHub [netZoo page](https://github.com/netZoo), and navigate into the
[netZooR](https://github.com/netZoo/netZooR) and [netZooPy](https://github.com/netZoo/netZooPy) repos.

**Who should apply to be a contributor?**

We welcome all types of contributors, with a preference for students who want to dive into the computational biology
field with a hands on approach. Working on the netZoo software requires 
at least a basic level of interest and curiosity for biological questions, such that all methods are still relevant 
and helpful for anyone who wants to run graph analysis on patient molecular biology data.

**Who is gonna mentor the project?**

Each project will be mentored by one of the maintainers of the netZoo packages and supervised by Prof. Quackenbush.
On top of direct mentoring, the contributor will have access to a cutting-edge learning environment at the Harvard 
Biostatistics department. The Quackenbush lab is a highly collaborative environment that has hosted multiple highschool, undergraduate, and
graduate students during the years. We hold weekly lab meetings where you will hear from all students and postdocs and
will be able to ask questions and give updates on your progress.

**How have we chosen these projects?**

We have looked into issues and enhancement features that have come up while developing the software. 
The network zoo has started as a harmonization project, where many individual computational methods have been 
grouped under R or Python packages. Hence, project #1 and #2 will focus on refactoring and reorganizing code 
to make it more efficient and less redundant. Secondly, we recognize that scientific software, while addressing novel
and important questions, is often lacking of the robustness of properly developed packages. With project #3 we 
encourage contributors who are interested in writing unit tests and CI scripts. 
Finally, to those who are more interested in working on graph inference and visualization, we suggest to look into 
project #4. Indeed, we would like to expand and improve the used experience, with more meaningful and helpful 
visualization methods, more appropriate IO interfaces, and animal-to-animal interfaces that allow seamless integration
of the various analysis steps.

## Idea #1: Refactor code 

We need a programmer who would clean all I/O functions of netZooPy and/or netZooR, 
reconciling the different input formats and 

**Time allocation**: ~90 hour, ~175 hours or ~350 
**Prerequisites**: ~90 hour, ~175 hours or ~350
**Programming skills**: ~90 hour, ~175 hours or ~350 
**Difficulty**: easy medium hard

## Idea #2: Unit tests

Description

**Time allocation**: ~90 hour, ~175 hours or ~350 
**Prerequisites**: ~90 hour, ~175 hours or ~350
**Programming skills**: ~90 hour, ~175 hours or ~350 
**Difficulty**: easy medium hard

## Idea #3: Unit tests

Both netZooR and netZooPy include unit tests in their CI, however in both cases the tests do not include all 
functions and should be expanded and refined. For this project you could do one or multiple of the following
(depending on time committment and skill set of the contributor):
- Write tests for all animals' IO
- Write tests for all internal functions, which are the animals' engines
- Write both R and Python tests, also cross-language, when the animals are present in both repos

Also, we would also like to include testing for stochastic functions, which is, for instance, the case of this
igraph-related [active issue]()https://github.com/netZoo/netZooPy/issues/320.

Description

**Time allocation**: ~90 hour, ~175 hours or ~350 
**Prerequisites**: Python and/or R, unit tests
**Programming skills**: easy
**Difficulty**: easy
**Mentors**: 


## Idea #4: Implement graph visualization strategies for inferred networks

Description

**Time allocation**: ~90 hour, ~175 hours or ~350 
**Prerequisites**: ~90 hour, ~175 hours or ~350
**Programming skills**: ~90 hour, ~175 hours or ~350 
**Difficulty**: easy medium hard

<!-- 
Brief descriptions of projects that can be completed in ~90 hour, ~175 hours or ~350 hours of your GSoC contributor’s time (and labeled appropriately).
For each project, a list of prerequisites, description of programming skills needed and estimation of difficulty level (easy, medium, hard).
If your organization plans to focus on mostly student level potential GSoC contributors for all projects that is fine, but please state it explicitly on your Ideas Page. Or if a given project idea is geared more toward a student level or a more advanced developer please state it clearly in the project idea so there is no confusion for applicants.
A list of potential mentors.
It must NOT be a link to your bug tracker. -->
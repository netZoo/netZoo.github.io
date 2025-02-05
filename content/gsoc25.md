# Ideas List, Google Summer of Code 2025 

- [Ideas List, Google Summer of Code 2025](#ideas-list-google-summer-of-code-2025)
  - [FAQ](#faq)
    - [What is the netZoo project?](#what-is-the-netzoo-project)
    - [Who should apply to be a contributor?](#who-should-apply-to-be-a-contributor)
    - [Who is gonna mentor the project?](#who-is-gonna-mentor-the-project)
    - [How have we chosen these projects?](#how-have-we-chosen-these-projects)
  - [Ideas](#ideas)
    - [Idea #1: Standardization of interfaces, inputs and outputs](#idea-1-standardization-of-interfaces-inputs-and-outputs)
    - [Idea #2: Unit tests](#idea-2-unit-tests)
    - [Idea #3: Migrate GRAND database to secure and updated technology stacks.](#idea-3-migrate-grand-database-to-secure-and-updated-technology-stacks)
    - [Idea #4: Implement graph visualization strategies for inferred networks](#idea-4-implement-graph-visualization-strategies-for-inferred-networks)


Welcome to the Ideas Page for the GSoC 2025, here you will find a list of possible GSoC projects for the netZoo project.

## FAQ

### What is the netZoo project?

The **Network Zoo (netZoo)** is a project spearheaded by the team of **Prof. John Quackenbush** at the **Harvard T. Chan School of
Public Health**.  The lab focuses on computational methods and analyses of how transcription factors (TFs) and genes
interact to regulate homeostasis and are disrupted in complex diseases, such as cancer or COPD. The netZoo is a
collection of open-source methods to infer gene regulatory network, conduct differential network analyses, estimate
community structure, and explore the transitions between biological states. The methods hosted in the netZoo have been
developed by the lab or close collaborators during the years and have been used in dozens of scientific publications.
The software is mostly written in R (netZooR) and Python  (netZooPy), with some exceptions in C++ and Matlab, and 
it is maintained by the lab with the goal of allowing dissemination, reproducibility, and educational purposes.

To have an idea of what is in the netZoo you can check the **main paper**: 
> The Network Zoo: a multilingual package for the inference and analysis of gene regulatory networks. Ben Guebila et al, 2023. Genome Biology. [doi:10.1186/s13059-023-02877-1](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-023-02877-1)

To look into the **code** you can refer to the main GitHub [netZoo page](https://github.com/netZoo), and navigate into the
[netZooR](https://github.com/netZoo/netZooR) and [netZooPy](https://github.com/netZoo/netZooPy) repos.

### Who should apply to be a contributor?

**We welcome all types of contributors, with a preference for students who want to dive into the computational biology
field** with a hands on approach. Working on the netZoo software requires 
at least a basic level of interest and curiosity for biological questions, such that all methods are still relevant 
and helpful for anyone who wants to run graph analysis on patient molecular biology data.


### Who is gonna mentor the project?

Each project will be mentored by one of the maintainers of the netZoo packages and supervised by Prof. Quackenbush.
On top of direct mentoring, the contributor will have access to a cutting-edge learning environment at the Harvard 
Biostatistics department. The Quackenbush lab is a highly collaborative environment that has hosted multiple highschool, undergraduate, and
graduate students during the years. We hold weekly lab meetings where you will hear from all students and postdocs and
will be able to ask questions and give updates on your progress.

### How have we chosen these projects?

We have looked into issues and enhancement features that have come up while developing the software. For instance, with
Idea #1 and Idea #2 (refactoring and testing)
we focus on refactoring, reorganizing, and appropriately testing code 
to make it more efficient and less redundant. Similarly, we also need to upgrade the backend of the database we use to
share our networks, which is the focus of Idea #3.
Finally, to those who are more interested in working on graph inference and visualization, we suggest to look into 
project #4. 

Indeed, we would like to expand and improve the user experience, with more meaningful and helpful 
visualization methods, more appropriate IO interfaces, and animal-to-animal interfaces that allow seamless integration
of the various analysis steps.

While we already have a plan on how to carry out each of these projects, we welcome any expertise that could
help and enable us to improve the code and platform. 

## Ideas

### Idea #1: Standardization of interfaces, inputs and outputs

The network zoo has started as a harmonization project, where many individual computational methods have been 
collected under the same R or Python packages. 
NetZoo's fragmented history has resulted in a diverse range of file formats for both input data and output networks. Not
only different methods require the same dataset in different format styles, but also they generate output files that
cannot be readily fed to another method in multistep analysis. Similarly, all interfaces are not standardized creating problems for usability, interoperability, and documentation.

For this reason, we need a programmer who would clean all I/O functions of netZooPy and/or netZooR, reconciling the
different input/output formats and all interfaces. This way we not only lower the risk for errors, but we also simplify
the user experience and the ability to extend and improve methods in the future.

- **Time allocation**: 175 (~90 hour, ~175 hours or ~350)
- **Prerequisites**: R/
- **Programming skills**: R and/or Python
- **Difficulty**: easy
- **Mentors**: Viola Fanfani, Tara Eicher, Derrick DeConti, Marouen Ben Guebila


### Idea #2: Unit tests

Both netZooR and netZooPy are packages originally built by harmonizing and reorganizing previously published software
and computational methods. Currently, we require all new methods to include unit tests, and we have CI steps in place
for testing. However, not all 
functions and methods have consistent and complete tests and should be expanded and refined. 

For this project you could do one or multiple of the following
(depending on time committment and skill set of the contributor):
- Write tests for all animals' IO
- Write tests for all internal functions, which are the animals' engines
- Write both R and Python tests, also cross-language, when the animals are present in both repos

Also, we would also like to include testing for stochastic functions, which is, for instance, the case of this
igraph-related [active issue]()https://github.com/netZoo/netZooPy/issues/320.

Description

- **Time allocation**: 175 hours
- **Prerequisites**: unit tests
- **Programming skills**: Python and/or R
- **Difficulty**: easy
- **Mentors**: Viola Fanfani, Tara Eicher, Derrick DeConti, Marouen Ben Guebila

### Idea #3: Migrate GRAND database to secure and updated technology stacks.

The Quackenbush Lab has dedicated a lot of effort and resources to reproducible science. While hosting, sharing, and maintaining
code online is relatively easy and inexpensive, sharing large datasets and networks requires an appropriate space and
infrastructure. For this reason, we created
[GRAND](https://grand.networkmedicine.org/), a collection of gene regulatory networks derived from human tissues,
cancer, cell lines, and small molecule drugs that was originally intended to share
networks generated with the netZoo tools. GRAND has now grown into a vast repository containing over 200,000 networks
and associated sample metadata and since the server infrastructure was originally built for a smaller scale, it has now become
overburdened. 

We
plan to redesign the GRAND webserver and we would need help implementing a newer and more secure version of the
database. We would like to move this SQLite locally developed database to a more robust managed relational database, allowing us to increase security, encryption, backups, and uptime reliability.



- **Time allocation**: 350
- **Prerequisites**: Databases, 
- **Programming skills**: Python, SQL
- **Difficulty**: hard
- **Mentors**: Derrick DeConti, Marouen Ben Guebila, Viola Fanfani


### Idea #4: Implement graph visualization strategies for inferred networks

Each netZoo method deals with gene regulatory networks, hence they use, manipulate, or infer weighted graphs with more than 10,000
nodes. In many occasions, visually representing these networks could be beneficical to understand their
general structure, to investigate specific links, or to show differences between graphs. The effective visualization of
large graphs is often challenging and so far the netZoo doesn't have a dedicated interface, but it is relying on ad-hoc
scripts and functions. 

We would like to build an appropriate interface to interrogate and visualize the output of the netZoo methods. First,
one would need to refactor and standardize the outputs of all animals. Then we would like to have programmatic access to
graph visualization, that would include sub-setting the nodes/edge and appropriately group or color entities.

- **Time allocation**: 350 
- **Prerequisites**: Data viz
- **Programming skills**: R and/or Python
- **Difficulty**: medium
- **Mentors**: Viola Fanfani, Tara Eicher, Derrick DeConti

<!-- 
Brief descriptions of projects that can be completed in ~90 hour, ~175 hours or ~350 hours of your GSoC contributor’s time (and labeled appropriately).
For each project, a list of prerequisites, description of programming skills needed and estimation of difficulty level (easy, medium, hard).
If your organization plans to focus on mostly student level potential GSoC contributors for all projects that is fine, but please state it explicitly on your Ideas Page. Or if a given project idea is geared more toward a student level or a more advanced developer please state it clearly in the project idea so there is no confusion for applicants.
A list of potential mentors.
It must NOT be a link to your bug tracker. -->
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
help and enable us to improve the code and platform. So, if you have some ideas on how to do this, we welcome your input
and would love to hear more about it!

## Ideas

### Idea #1: Standardization of interfaces, inputs and outputs

The network zoo has started as a harmonization project to bring together tools that were developed around a common
conceptual framework, but were written and maintained by different individuals. These methods can use
different file formats for both input data and output networks. As a result, not only this increases the risk of errors
for the users, but also serial analyses are hampered in some cases because output files from one method cannot be readily fed to
another. Similarly, the interfaces are not standardized and minor inconsistencies can lead to problems with usability,
interoperability, and documentation.

For this reason, we need a programmer who would clean all I/O functions of netZooPy and/or netZooR, reconciling the
different input/output formats and all interfaces. This way we not only lower the risk for errors, but we also simplify
the user experience and the ability to extend and improve methods in the future.

- **Time allocation**: 175 
- **Prerequisites**: OOP and functional programming
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

Our research team is dedicated to reproducible science. While hosting, sharing, and maintaining code online is
relatively easy and inexpensive, sharing large datasets and networks requires an appropriate space and infrastructure.
Much of our work involves creating large-scale networks for modeling the process of gene regulation, but there are no
national databases for storing such networks, rendering much of our work potentially difficult to reproduce. To overcome
the limitations of public databases, we created [GRAND](https://grand.networkmedicine.org/), an online repository of
gene regulatory networks that have been derived from human tissues, cancer, and cell lines, as well as networks that
capture cellular response to small molecule drugs. GRAND has grown into a vast repository containing over 200,000
networks and associated sample metadata, operating on a server infrastructure originally built for a much smaller scale.
As we continue to grow our analyses and expand the data we make available to other researchers, there is a critical need
to refactor the code and improve our the architecture supporting this important project.

We plan to redesign the GRAND webserver and resource and we would need help implementing a newer and more secure version of the database. We would like to move this locally developed SQLite database to a more robust managed relational database, allowing us to increase security, encryption, backups, and uptime reliability.

- **Time allocation**: 350
- **Prerequisites**: databases, cloud storage, managed relational databases`*`
- **Programming skills**: Python, SQL, MongoDB`*`
- **Difficulty**: hard
- **Mentors**: Derrick DeConti, Marouen Ben Guebila, Viola Fanfani

`*`Preferred but not required.


### Idea #4: Implement graph visualization strategies for inferred networks

The netZoo methods infer or analyze gene regulatory networks that are represented by weighted graphs with more than 20,000 nodes and many more edges. For many analyses, visually representing these networks (and color-coding the nodes based on the properties of the genes) can provide new insights into the processes driving health and disease and comparing graphs between conditions or over time can lead to a deeper understanding of how diseases develop and progress.  Effective visualization of such large graphs can be challenging and netZoo does not yet have a dedicated interface or tools for creating robust, scalable visualizations. 

We would like to build an appropriate interface to interrogate and visualize the output of the netZoo methods. First, one would need to refactor and standardize the outputs of all the individual methods (see Idea #1). Then one would have to develop graph visualization that address key questions, including sub-setting the nodes/edge and appropriately grouping or coloingr entities.

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


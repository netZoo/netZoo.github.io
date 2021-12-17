---
title: "How to contribute to netbooks"
date: 2019-07-02T08:50:52-04:00
draft: false
---

## Contribution guide

[netbooks](http://netbooks.networkmedicine.org) is a Jupyter notebook tutorial server that hosts several uses case of the Network Zoo tools.


## Preparing the contribution

Please prepare your tutorial as an Python/R [Jupyter notebook](https://jupyter.org/).

Make sure to:

- Avoid saving files on disk

- Avoid making systems calls to create folders or call  other programs such as `os.system( someBashCommand )`

- Include substantial documentation of the code and illustrate the use cases with biological/theoretical motivation in the introduction and main takeaway in the conclusion

- Always include the package loading call in the beginning of each tutorial and the references at the end

- Avoid setting working directories using `setwd()/os.chdir()` and instead refer to files by their relative paths

## Submit the contribution

Please open a new pull request at the [netbooks GitHub repo](https://github.com/netZoo/netbooks) and push the `.ipynb` file.

Then, the server will fetch the new changes periodically and the tutorial will be displayed in the server.

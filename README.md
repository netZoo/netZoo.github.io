## Installation
netZoo.github.io website uses [HUGO](https://gohugo.io) and follows a standard structure. The web pages are written in [markdown](https://www.markdownguide.org/) and are stored in `content` folder.

## Modifiying the content
You can modify the content and push the changes through `deploy.sh` script after checking that  you like the modification through `hugo server -D`.

You can change the paramters of the website, including the themes, in the `config.toml` file.

## Updating list of publications
Please run the `fetchPubs.py` script that will automatically fetch the list of publications that use the netZoo from
Google Scholar. The script will build an updated `papers.md` page. Finally, `deploy.sh`.




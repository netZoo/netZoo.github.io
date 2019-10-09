import scholarly
import re
import time

## 1. PANDA
panda = re.compile("[Pp]assing messages between biological networks to refine")

# Retrieve the author's data, fill-in, and print
search_query = scholarly.search_author('Kimberley Glass')
author = next(search_query).fill()
print(author)

# Print the titles of the author's publications
for pub in author.publications:
	if panda.search(pub.bib['title']):
		break;

# Take a closer look at the first publication
pub = pub.fill()
print(pub)

# Which papers cited that publication?
pubs = "--- \ntitle: \"List\" \ndate: 2019-07-02T08:50:52-04:00 \ndraft: false \n--- \n## Publications \n \n"

for citation in pub.get_citedby():
        print(citation.bib['title'])
        try:
                pubs = pubs + '>'+citation.bib['title']+'. '+citation.bib['author']+'. \n \n'+citation.bib['url'] + '. \n \n'
        except:
                print("Paper has no url")

time.sleep(30)
## 2. LIONESS
lioness = re.compile("[Ee]stimating sample-specific regulatory networks")

# Retrieve the author's data, fill-in, and print
search_query = scholarly.search_author('Marieke kuijjer')
author = next(search_query).fill()
print(author)

# Print the titles of the author's publications
for pub in author.publications:
        if lioness.search(pub.bib['title']):
                break;

# Take a closer look at the first publication
pub = pub.fill()
print(pub)

# Fetch citations
for citation in pub.get_citedby():
	print(citation.bib['title'])
	try:
		pubs = pubs + '>'+citation.bib['title']+'. '+citation.bib['author']+'. \n \n'+citation.bib['url'] + '. \n \n'
	except:
		print("Paper has no url")

time.sleep(30)
## 3. CONDOR
condor = re.compile("[Bb]ipartite community structure of e[qQ][tT][lL]s")

# Retrieve the author's data, fill-in, and print
search_query = scholarly.search_author('John platig')
author = next(search_query).fill()
print(author)

# Print the titles of the author's publications
for pub in author.publications:
        if condor.search(pub.bib['title']):
                break;

# Take a closer look at the first publication
pub = pub.fill()
print(pub)

# Fetch citations
for citation in pub.get_citedby():
        print(citation.bib['title'])
        try:
                pubs = pubs + '>'+citation.bib['title']+'. '+citation.bib['author']+'. \n \n'+citation.bib['url'] + '. \n \n'
        except:
                print("Paper has no url")

time.sleep(30)
## 4. ALPACA
alpaca = re.compile("[Dd]etecting phenotype-driven transitions in regulatory network structure")

# Retrieve the author's data, fill-in, and print
search_query = scholarly.search_author('John Quackenbush')
author = next(search_query).fill()
print(author)

# Print the titles of the author's publications
for pub in author.publications:
        if alpaca.search(pub.bib['title']):
                break;

# Take a closer look at the first publication
pub = pub.fill()
print(pub)

# Fetch citations
for citation in pub.get_citedby():
        print(citation.bib['title'])
        try:
                pubs = pubs + '>'+citation.bib['title']+'. '+citation.bib['author']+'. \n \n'+citation.bib['url'] + '. \n \n'
        except:
                print("Paper has no url")

# save to markdown
text_file = open("netZooWeb/content/papers/papers.md","w")
text_file.write(pubs)
text_file.close()

# shortsweet
# Text summarization app with flexibility and enhanced accuracy
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

wiki_url = 'https://en.wikipedia.org/wiki/Genome'
wiki_data = urlopen(wiki_url) # open the wiki url to read it

wiki_html = wiki_data.read() # read the data from the wiki url
wiki_data.close() # close the connection

page_soup = soup(wiki_html, 'html.parser')

# Create a list to store the pure text from the page
genome_text = []

# Find all the paragraphs and add their text to the list
for div in page_soup.findAll('p'):
    genome_text.append(div.text)

print(genome_text)

# Isolate sentences with 6 words.
for i in range(genome_text.index()):
    six_word = genome_text.pop()

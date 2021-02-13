from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import csv

# This program scrapes paragraph text from wikipedia files
# and adds them sentence by sentence to a .csv file.

# Find the position of the nth space in the list
def parse_sentences(text_str):
    # Define list to hold the individual strings
    split_text_strings = []
    for i in text_str:
        split_i = i.split('.')
        for j in split_i:
            last = len(split_i) - 1
            if split_i[last] == '':
                split_i.pop(last)
            split_text_strings.append(j)

    return split_text_strings

wiki_url = 'https://en.wikipedia.org/wiki/Giant_panda'
wiki_data = urlopen(wiki_url) # open the wiki url to read it

wiki_html = wiki_data.read() # read the data from the wiki url
wiki_data.close() # close the connection

page_soup = soup(wiki_html, 'html.parser')

# Create a list to store the pure text from the page
page_text = []

# Create a .csv to store the text from the wiki page.
csv_file = open('wiki_scraps.csv','w')
writer = csv.writer(csv_file)

# Write the headers for the .csv file
writer.writerow(['Six Words', 'Important Words'])

# Find all the paragraphs in the wiki page text
# add their text to the list of six words
for div in page_soup.findAll('p'):
    page_text.append(div.text)

# Remove utf-8 characters in a separate loop to
# avoid O(n^2) algorithm
# utf_scrubbed_chars = [char for char in page_text if ord(char) < 128]

# Convert the utf_scrubbed_chars list of chars back into a list of sentences
# scrubbed_page_text = ""
# for char in utf_scrubbed_chars:
    # scrubbed_page_text.append(char)

# split the page_text into individual sentences
page_text = parse_sentences(page_text)

for text_line in range(len(page_text)):
    writer.writerow([page_text[text_line],])


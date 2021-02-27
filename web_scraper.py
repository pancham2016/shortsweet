from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import urllib.error
import csv

class WebScraper:
    """
    A Webpage Scraper class that extracts the contents and headers
    of a webpage.
    Assumptions:
    1. 'Content' (non-headers) is the most occurring type of text (in number of
    characters).
    2. Headers and content text are only differentiated by text size, can
    possibly use bold or font name in the future
    """

    def __init(self, url):
        # Define the url attribute
        self.url = url

    def read_web_page(self, url):
        # Open and read the url of a webpage
        """
        :param: url: the url of the webpage
        :return: soup_object: the raw data soup of the webpage
        """
        # Open the url, read the data and stop retrieving data
        # from the source
        raw_web_soup = urlopen(url)
        read_page = raw_web_soup.read()
        raw_web_soup.close()

        # Create instance of soup object
        soup_object = soup(read_page, 'html.parser')

        return soup_object

    def site_forbidden(self, url):
        """
        # Checks if webpage is accessible or forbidden.
        # Will be useful for future webcrawling. Maybe?
        :param url: the url of the website being scraped
        :return: success: True if webpage read was successful
                          False if webpage is forbidden
        """
        try:
            # Try to read the page and return True if there are no issues
            sr.read_web_page(url)
            success = True
        except urllib.error.HTTPError:
            # Return false if the website is forbidden to access
            success = False

        return success

    def parse_sentences(self, text_list):
        # Parses through a list containing all the sentences in a Wiki webpage
        # and splits their sentences.
        """
        :param text_list: the list of websoup data
        :return: a list of the sentences from the webpage
        """
        # Define list to hold the individual strings
        split_text_list = []
        for i in text_list:
            split_i = i.split('.')
            for j in split_i:
                last = len(split_i) - 1
                if split_i[last] == '':
                    split_i.pop(last)
                split_text_list.append(j)

        return split_text_list


    def filter_paragraphs(self, web_soup):
        # This method loops through data and removes
        # as many tags as given
        # param: web_soup - the raw data from the web page
        #
        # return: new_soup: a new data set from the web page with those tags
        #         sanitized.
        paragraph_soup = web_soup.findAll('p')

        return paragraph_soup

    def filter_headers(self, web_soup):
        # Grabs the headers from the web page
        """
        :param web_soup: the raw web soup from the webpage
        :return: header_soup: soup of just the headers
        TO DO: Work in progress. Method keeps printing out unnecessary headers
        """
        for span in web_soup("span"):
            span.decompose()

        header_soup = web_soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

        return header_soup


# Create a website csv
csv_file = open('websites.csv','w')
writer = csv.writer(csv_file)

# TO DO: Find a way to parse sentence by sentence

if __name__=='__main__':
    sr = WebScraper()
    url = 'https://en.wikipedia.org/wiki/Genome'
    read_page_soup = sr.read_web_page(url)
    # just_pars = sr.filter_paragraphs(read_page_soup)
    # print(just_pars)

    # # print(read_page_soup.get_text())
    # parse_list = []
    # for div in just_pars:
    #     parse_list.append(div.text)
    #
    # parse_list = sr.parse_sentences(parse_list)
    # for div in parse_list:
    #     print(div)







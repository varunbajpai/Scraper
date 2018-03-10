import requests
from html.parser import HTMLParser
import sys
import ast
scrape_check=''

#Stopwords, specialwords and Bad_words from configuration file
with open('configuration.json') as config_file:
    config_dict = ast.literal_eval(config_file.read())

special_tags = config_dict['special_tags']
stop_tags = config_dict['stop_tags']
bad_data = config_dict['bad_data']

def write_to_file(data):
    with open('output.txt', 'a') as output:
        output.write(data)

# create a subclass and override the handler methods
class MyHtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global scrape_check
        scrape_check = tag

    def handle_data(self,data):
        global scrape_check
        if scrape_check in special_tags:
            write_to_file(data)
            return
        if scrape_check in stop_tags or data in bad_data:
            scrape_check = ''
            return
        if len(data.split(' '))>10:
            write_to_file(data)

# instantiate the parser and fed it HTML
def scraper(url):
    try:
        page = requests.get(url)
        parser = MyHtmlParser()
        parser.feed(str(page.content))
    except:                                 #fires up in case of invalid URL
        print('INVALID URL')
scraper(sys.argv[1])

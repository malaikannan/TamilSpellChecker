import requests
from bs4 import BeautifulSoup
import tamil
import os
import traceback

class ProjectMaduraiCrawler:

    def __init__(self,base_url,sub_url,tamil_word_list_path):
        self.base_url = base_url
        self.home_page = base_url + sub_url
        res = requests.get(self.home_page)
        self.html_page = res.content
        self.tamil_word_list_path = tamil_word_list_path

    
    def FetchHTMLLinks(self):
        try:

            soup = BeautifulSoup(self.html_page)
            links = [a['href'] for a in soup.select('a[href]')]
            self.html_links = []

            #link in 
            for link in links:
                if ".html" in link:
                    if "pm_etext" in link:
                        self.html_links.append(link)
        except Exception as e:
            track = traceback.format_exc()
            print(track)
    
    def FetchUniqueWords(self):
        ta_words = []
        for link in self.html_links:
            res = requests.get(self.base_url+link)
            print("fetching content for : " + self.base_url + link)
            html_page = res.content 
            soup = BeautifulSoup(html_page, 'html.parser')
            text = soup.find_all(text=True)

            output = ''
            blacklist = [
                '[document]',
                'noscript',
                'header',
                'html',
                'meta',
                'head', 
                'input',
                'script',
                # there may be more elements you don't want, such as "style", etc.
            ]

            for t in text:
                if t.parent.name not in blacklist:
                    output += '{} '.format(t)

            
            taletters = tamil.utf8.get_letters(output)
            ta_words_page = tamil.utf8.get_tamil_words(taletters)
            ta_words = ta_words + ta_words_page
            

        self.ta_words_unique = list(set(ta_words))
    
    def create_tamil_unique_word_list_file(self):

        outfile = open(self.tamil_word_list_path, 'w') # open a file in write mode
        for item in self.ta_words_unique:    # iterate over the list items
            outfile.write(str(item) + '\n') # write to the file
        outfile.close() 

if __name__ == "__main__":
    
    base_url = "https://www.projectmadurai.org"
    sub_url = "/pmworks.html"
    wordlist_file_name = "tamilwordlist_text.txt"


    crawler  = ProjectMaduraiCrawler(base_url,sub_url,wordlist_file_name)
    crawler.FetchHTMLLinks()
    crawler.FetchUniqueWords()
    crawler.create_tamil_unique_word_list_file()
    


    


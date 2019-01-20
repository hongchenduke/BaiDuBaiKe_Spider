#conding :ctf-8
from bs4 import BeautifulSoup
class HtmlParser(object):
    def _get_new_urls(page_url,soup):
       new_urls = set()
    def _get_new_data(page_url,soup):


    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls =self._get_new_urls(page_url,soup)
        new_data =self._get_new_data(page_url,soup)
        return new_urls,new_data

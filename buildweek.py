from time import sleep
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep

base_url = 'https://www.goodreads.com/list/show/1.Best_Books_Ever?page=1'


def scrape_classes(url, tag, class_to_find):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        sleep(0.5)
        return soup.find_all(tag, class_=class_to_find)

# 
# def create_page_url(items_list, str1, str2):
#         urls =[]
#         for el in items_list:
#                 url = str1 + el.a['href'] + str2
#                 urls.append(url)
#         return urls

book_titles = scrape_classes(base_url, 'a', 'bookTitle')
print(book_titles)
print(len(book_titles))

# book_authors = scrape_classes(base_url, 'a', 'authorName')
# print(book_authors)
# #print(len(book_authors))

# book_urls = scrape_classes(base_url, 'a', 'authorName')
# print(book_urls)
# print(len(book_urls))



def url_getter(url):
    page_all = requests.get(url)
    soup = BeautifulSoup(page_all.content, "html.parser")
    return soup

page1 = url_getter(url_links)

def award(soup):
    award1000 = soup.find_all('span', itemprop='numberOfPages')
    book_award =[]
    for award in award1000:
        sleep(0.5)
        bo_award= award.text
        bo_award = bo_award.replace('\n', '')
        book_award.append(bo_award)
    return book_award

first100_book_award =award(page1)
print(first100_book_award)
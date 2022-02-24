from time import sleep
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep

url1 = 'https://www.goodreads.com/list/show/1.Best_Books_Ever'
url2 = 'https://www.goodreads.com/list/show/1.Best_Books_Ever?page=2'
url3 = 'https://www.goodreads.com/list/show/1.Best_Books_Ever?page=3'
url4 = 'https://www.goodreads.com/list/show/1.Best_Books_Ever?page=4'
url5 = 'https://www.goodreads.com/list/show/1.Best_Books_Ever?page=5'
url6 = 'https://www.goodreads.com/list/show/1.Best_Books_Ever?page=6'
url7 = 'https://www.goodreads.com/list/show/1.Best_Books_Ever?page=7'
url8 = 'https://www.goodreads.com/list/show/1.Best_Books_Ever?page=8'
url9 = 'https://www.goodreads.com/list/show/1.Best_Books_Ever?page=9'
url10 = 'https://www.goodreads.com/list/show/1.Best_Books_Ever?page=10'


def url_getter(url):
    page_all = requests.get(url)
    soup = BeautifulSoup(page_all.content, "html.parser")
    return soup

page1 = url_getter(url1)
page2 = url_getter(url2)
page3 = url_getter(url3)
page4 = url_getter(url4)
page5 = url_getter(url5)
page6 = url_getter(url6)
page7 = url_getter(url7)
page8 = url_getter(url8)
page9 = url_getter(url9)
page10 = url_getter(url10)


def title(soup):
    title1000 = soup.find_all('a', class_="bookTitle")
    book_title =[]
    for i in title1000:
        sleep(0.5)
        bo_title= i.text
        bo_title = bo_title.replace('\n', '')
        book_title.append(bo_title)
    return book_title

first100_book_title = title(page1)
second100_book_title = title(page2)
third100_book_title = title(page3)
forth100_book_title = title(page4)
fifth100_book_title = title(page5)
sixth100_book_title = title(page6)
seventh100_book_title = title(page7)
eight100_book_title = title(page8)
ninth100_book_title = title(page9)
tenth100_book_title = title(page10)

# all_book_titles = first100_book_title + second100_book_title + third100_book_title + forth100_book_title + fifth100_book_title + sixth100_book_title + seventh100_book_title + eight100_book_title + ninth100_book_title + tenth100_book_title
# print(all_book_titles)
#print(len(all_book_titles))


def author(soup):
    author1000 = soup.find_all('a', class_="authorName")
    book_author =[]
    for i in author1000:
        sleep(0.5)
        bo_author = i.text
        bo_author = bo_author.replace('\n', '')
        book_author.append(bo_author)
    return book_author


first100_book_author = author(page1)
second100_book_author = author(page2)
third100_book_author = author(page3)
forth100_book_author = author(page4)
fifth100_book_author = author(page5)
sixth100_book_author = author(page6)
seventh100_book_author = author(page7)
eight100_book_author = author(page8)
ninth100_book_author = author(page9)
tenth100_book_author = author(page10)

# all_book_author = first100_book_author + second100_book_author + third100_book_author + forth100_book_author + fifth100_book_author + sixth100_book_author + seventh100_book_author + eight100_book_author + ninth100_book_author + tenth100_book_author
# print(all_book_author)
# print(len(all_book_author))


def book_address(soup):

    #website = requests.get(website_links)
    #soup = BeautifulSoup(website.content, 'html.parser')
    book_pages = soup.find_all('div', class_='js-tooltipTrigger tooltipTrigger')

    book_Awards = []
    for book_page in book_pages:   
        sleep(0.5)
        address = book_page.a['href']
        address = 'https://www.goodreads.com' + address 
        book_Awards.append(address)
    return book_Awards
first100_book_Awards = author(page1)
print(first100_book_Awards)




# def book_url(soup):
#     url1000 = soup.find_all('a', class_="bookTitle")
#     book_url =[]
#     for i in url1000:       #'https://www.goodreads.com/book/show/'
#         sleep(0.5)
#         url_100 =  url1000[i]
#         book_url.append(url_100)
#     return book_url

# url_f100 = book_url(page1)

# print(url_f100)
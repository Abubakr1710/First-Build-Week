import requests
from bs4 import BeautifulSoup
from time import sleep

url_1 =  'https://www.goodreads.com/list/show/1.Best_Books_Ever'
url_2 =  'https://www.goodreads.com/list/show/1.Best_Books_Ever?page=2'
url_3 =  'https://www.goodreads.com/list/show/1.Best_Books_Ever?page=3'
url_4 =  'https://www.goodreads.com/list/show/1.Best_Books_Ever?page=4'
url_5 =  'https://www.goodreads.com/list/show/1.Best_Books_Ever?page=5'
url_6 =  'https://www.goodreads.com/list/show/1.Best_Books_Ever?page=6'
url_7 =  'https://www.goodreads.com/list/show/1.Best_Books_Ever?page=7'
url_8 =  'https://www.goodreads.com/list/show/1.Best_Books_Ever?page=8'
url_9 =  'https://www.goodreads.com/list/show/1.Best_Books_Ever?page=9'
url_10 = 'https://www.goodreads.com/list/show/1.Best_Books_Ever?page=10'

websites = [url_1, url_2, url_3, url_4, url_5, url_6, url_7, url_8, url_9, url_10]

#########################################################################################################################
#   AWARDS  
#########################################################################################################################

def bookAward(website_links):

    website = requests.get(website_links)
    soup = BeautifulSoup(website.content, 'html.parser')
    book_pages = soup.find_all('div', class_='js-tooltipTrigger tooltipTrigger')

    book_Awards = []
    for book_page in book_pages:   
        sleep(0.5)
        address = book_page.a['href']
        address = 'https://www.goodreads.com' + address 
        book_Awards.append(address)

    bookAward = [] 
    for book_Award in book_Awards:
        sleep(0.5)
        page = requests.get(book_Award)
        soup = BeautifulSoup(page.content, 'html.parser')

        book_awards = soup.find_all('a', class_='award')
        for book_award in book_awards:
            sleep(0.5)
            book_award = book_award.text 
            book_award = book_award.strip()
            bookAward.append(book_award)

    return book_Award
        
# --------------------------------------------------------------------------------------------------------------------

# book_AWARDS = []
# for website in websites:
#     review = bookAward(website)
#     book_AWARDS = book_AWARDS + review

# print(len(book_AWARDS))
# print(book_AWARDS)

#########################################################################################################################

websites = [url_1, url_2, url_3, url_4, url_5, url_6, url_7, url_8, url_9, url_10]

review = bookAward(url_1)

print(review)





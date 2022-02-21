import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://www.goodreads.com/list/show/1.Best_Books_Ever')
soup = BeautifulSoup(page.content, 'html.parser')

ori = []
ser = []
gen = []

#----------------------------------------------------------------------#
#Original publish year


#----------------------------------------------------------------------#
#Series



#----------------------------------------------------------------------#
#Genres



#----------------------------------------------------------------------#


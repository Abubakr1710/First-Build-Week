from email import header
from lib2to3.pgen2.pgen import DFAState
from os import sep
from pickle import TRUE
from matplotlib.pyplot import xlabel, ylabel
import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import plotly_express as px

header = st.container()
sidebar = st.sidebar

with sidebar:
    st.image('data//img1.jpg')
    st.header('Team members:')
    st.markdown('* **Peter**')
    st.markdown('* **Busayo**')
    st.markdown('* **Islom**')
    st.markdown('* **Abubakr**')

    st.header('Data analyze')
    st.markdown('* **1:** Group the books by original_publish_year and get the mean of the minmax_norm_ratings of the groups.')
    st.markdown('* **2:** Create a function that given an author as input it returns her/his book with the highest minmax_norm_ratings.')
    st.markdown('* **3:** Which 50 books should i stock up as a bookstore and should it be part of a series or no series?')
    st.markdown('* **4:** Do the number of ratings affect the actual rating provided? Can this be used to make the decision to read a book or not?')
    st.markdown('* **5:** Do the number of awards actually mean that the book got a higher rating? Do it on author by author basis as well!')


with header:
    st.title('Welcome to our project')
    df = pd.read_csv('C:/Users/Abubakr/Documents/GitHub/First-Build-Week/new_data.csv')
    st.write(df)

def p1(df):
    data =  df.groupby(['original_publish_year'])['minmax_norm_ratings'].mean().round(2)
    fig = px.bar(data)
    return fig
test2 = p1(df)
st.write(test2)

def p2(df):
    st.markdown('* **Here must be something**')
    fig = px.scatter(df, x = 'original_publish_year', y = 'minmax_norm_ratings', color ='minmax_norm_ratings' ,size='num_ratings')
    return fig
test = p2(df)
st.header('Here must be something')
st.write(test)

def p3(df):
    author_name  = df['author'].unique().tolist()
    author = st.selectbox('Choose author', author_name, 0)
    df= df[df['author'] == author]
    return df[df['author']==author].sort_values('minmax_norm_ratings', ascending=False)['title'].head(1).item(), df[df['author']==author].sort_values('minmax_norm_ratings', ascending=False)['minmax_norm_ratings'].head(1).item() 
test3 = p3(df)
st.write("Author's best book is:",test3[0])
st.write('The Rating of the book is:',test3[1])
    
    
    
    
    #st.write("Author's best book is:", name_book)
    #st.write('The Rating of the book is:',rat_book)

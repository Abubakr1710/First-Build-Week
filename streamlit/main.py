from email import header
from pickle import TRUE
from matplotlib.pyplot import xlabel, ylabel
import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import plotly_express as px


sidebar = st.sidebar
header = st.container()
dataset = st.container()
plots =st.container()
firstone = st.container()
bestbook_author = st.container()
bestbook = st.container()


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



with dataset:
    st.header('Data section')
    
    df = pd.read_csv('C:/Users/Abubakr/Documents/GitHub/First-Build-Week/new_data.csv')
    st.write(df)

with plots:
    st.header('Welcome to plots')
    st.markdown('* **Headache section 🤪**')

    graph = df['minmax_norm_ratings'].sort_values(ascending=True).head(20)
    st.bar_chart(graph)

    graph1 = df['num_ratings'].head(21)
    st.bar_chart(graph1)

with firstone:
    st.title('Data analyze')
    st.write(df)
    data = df.groupby(['original_publish_year'])['minmax_norm_ratings'].mean().round(2)
    st.write(data)
    fig = px.bar(data)
    st.write(fig)
    #----------------------------------------------------------#
    fig = px.scatter(df, x="original_publish_year", y="minmax_norm_ratings", animation_frame=df['original_publish_year'].sort_values(ascending=True),
        color="minmax_norm_ratings",log_x=True, log_y=True)
    st.write(fig)
    #----------------------------------------------------------#
    fig = px.scatter(df, x = 'original_publish_year', y = 'minmax_norm_ratings', color ='minmax_norm_ratings' ,size='num_ratings')
    st.write(fig)
    #----------------------------------------------------------#   
with bestbook_author:
    

    st.markdown('* **This is answer for 2**')
    st.header('Best book of any Authors')

    author_name  = df['author'].unique().tolist()
    author = st.selectbox('Choose author', author_name, 0)
    df= df[df['author'] == author]
    name_book = df[df['author']==author].sort_values('minmax_norm_ratings', ascending=False)['title'].head(1).item()
    rat_book = df[df['author']==author].sort_values('minmax_norm_ratings', ascending=False)['minmax_norm_ratings'].head(1).item() 
    st.write("Author's best book is:", name_book)
    st.write('The Rating of the book is:',rat_book)
    

    #2
    df1 = pd.read_csv('C:/Users/Abubakr/Documents/GitHub/First-Build-Week/new_data.csv')
    withminmax = df1['minmax_norm_ratings'].unique().tolist()
    chminmax = st.selectbox('Choose rating(Rating is between 1 and 10)', withminmax,0)
    df1=df1[df1['minmax_norm_ratings'] == chminmax]
    name_book1 = df1[df1['minmax_norm_ratings']==chminmax].sort_values('mean_norm_ratings', ascending=False)['title'].head(1).item()
    auth_book1 = df1[df1['minmax_norm_ratings']==chminmax].sort_values('mean_norm_ratings', ascending=False)['author'].head(1).item()
    st.write("Book kname is:", name_book1)
    st.write('Name of author:',auth_book1)






with bestbook:
    st.markdown('* **This is answer for 4**')
    st.header('Here you can find the best books to read by rating')
    data = pd.read_csv('C:/Users/Abubakr/Documents/GitHub/First-Build-Week/new_data.csv')


    ratingbook = data['minmax_norm_ratings'].sort_values(ascending=True)
    rating = st.select_slider('Choose rating', ratingbook,1.0)
    data = data[data['minmax_norm_ratings'] == rating]
    nbook = data[data['minmax_norm_ratings']==rating].sort_values('minmax_norm_ratings', ascending=True)['title'].head(1).item()
    nwriter = data[data['minmax_norm_ratings']==rating].sort_values('minmax_norm_ratings', ascending=True)['author'].head(1).item()
    nrating = data[data['minmax_norm_ratings']==rating].sort_values('minmax_norm_ratings', ascending=True)['num_ratings'].head(1).item()
    st.write(nrating,'ratings')
    st.write('writer:',nwriter)
    st.write('This is a best book in your match:', nbook)




    





    










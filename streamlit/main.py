from email import header
from matplotlib.pyplot import xlabel, ylabel
import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import matplotlib.pyplot as plt



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

    graph1 = df['num_rating'].head(21)
    st.bar_chart(graph1)

with firstone:
    st.title('Data analyze')
    st.write(df)
    data = df.groupby(['author'])['minmax_norm_ratings'].mean().round(2)
    st.write(data)
    fig = data.head(70)
    st.bar_chart(fig)


    #fig = px.scatter(df, x = 'Weight', y = 'Height', size='Index',color='Index', hover_name='Index')
    #st.write(fig)

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



with bestbook:
    st.markdown('* **This is answer for 4**')
    st.header('Here you can find the best books to read by rating')
    data = pd.read_csv('C:/Users/Abubakr/Documents/GitHub/First-Build-Week/new_data.csv')


    ratingbook = data['minmax_norm_ratings'].sort_values(ascending=True)
    rating = st.select_slider('Choose rating', ratingbook,1.0)
    data = data[data['minmax_norm_ratings'] == rating]
    nbook = data[data['minmax_norm_ratings']==rating].sort_values('minmax_norm_ratings', ascending=True)['title'].head(1).item()
    nwriter = data[data['minmax_norm_ratings']==rating].sort_values('minmax_norm_ratings', ascending=True)['author'].head(1).item()
    nrating = data[data['minmax_norm_ratings']==rating].sort_values('minmax_norm_ratings', ascending=True)['num_rating'].head(1).item()
    st.write(nrating,'ratings')
    st.write('writer:',nwriter)
    st.write('This is a best book in your match:', nbook)




    





    










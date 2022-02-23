from email import header
from matplotlib.pyplot import xlabel
import streamlit as st
import pandas as pd
import plotly.figure_factory as ff



sidebar = st.sidebar
header = st.container()
dataset = st.container()
plots =st.container()
bestbook_author = st.container()
bestbook = st.container()

with sidebar:
    st.image('data//img1.jpg')
    st.header('Team members:')
    st.markdown('* **Peter**')
    st.markdown('* **Busayo**')
    st.markdown('* **Islom**')
    st.markdown('* **Abubakr**')


    add_selectbox = st.sidebar.selectbox(
    "Do you want to contact with us?",
    ("Peter","Busayo","Islom","Abubakr"))
    


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

with bestbook_author:
    
    st.header('Best book of any Authors')

    author_name  = df['author'].unique().tolist()
    author = st.selectbox('Choose author', author_name, 0)
    df= df[df['author'] == author]
    name_book = df[df['author']==author].sort_values('minmax_norm_ratings', ascending=False)['title'].head(1).item()
    rat_book = df[df['author']==author].sort_values('minmax_norm_ratings', ascending=False)['minmax_norm_ratings'].head(1).item() 
    st.write("Author's best book is:", name_book)
    st.write('The Rating of the book is:',rat_book)



with bestbook:
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




    





    










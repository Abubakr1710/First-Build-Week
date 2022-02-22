from email import header
from matplotlib.pyplot import xlabel
import streamlit as st
import pandas as pd
import plotly.figure_factory as ff



sidebar = st.sidebar
header = st.container()
dataset = st.container()
plots =st.container()

with sidebar:
    st.title('🐉 SLYTHERIN 🐉')
    st.header('Team members:')
    st.markdown('* **Peter**')
    st.markdown('* **Busayo**')
    st.markdown('* **Abubakr**')

    add_selectbox = st.sidebar.selectbox(
    "Do you want to contact with us?",
    ("Peter", "Busayo", "Abubakr"))

with header:
    st.title('Welcome to our project')



with dataset:
    st.header('Data section')
    
    df = pd.read_csv('C:/Users/Abubakr/Documents/GitHub/First-Build-Week/streamlit/data/new_data.csv')
    st.write(df)

with plots:
    st.header('Welcome to plots')
    st.markdown('* **Headache section 🤪**')

    graph = df['minmax_norm_ratings'].head(21)
    st.bar_chart(graph)



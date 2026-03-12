import streamlit as st
import pickle
import os

st.set_page_config(page_title="Layouts", layout='wide')
st.title('Streamlit Layout')  # display title format
# sidebar
sidebar = st.sidebar
sidebar.write('This is my sidebar')
sidebar.header('Header in sidebar')
# columns
col1, col2, col3 = st.columns(3)
with col1:
    st.write('This is column -1 :smirk_cat:')
    st.image('./media/cat.jpg')
    
with col2:
    st.write('This is column -2 :dog2:')
    st.image('./media/dog.jpg')
    
with col3:
    st.write('This is column -3 :owl:')
    st.image('./media/owl.jpg')
# tabs
st.header('Display in Tabs')
tab1, tab2, tab3 = st.tabs(['Cat', 'Dog', 'Owl'])

with tab1:
    st.write('You are in Cat Tab :smirk_cat:')
    st.image('./media/cat.jpg')
with tab2:
    st.write('You are in Dog Tab :dog2:')
    st.image('./media/dog.jpg')
with tab3:
    st.write('You are in Owl Tab :owl:')
    st.image('./media/owl.jpg')

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = 'layout_app.pkl'
data_to_save = {"test": "It works!"} 
with open('layout_app.pkl', 'rb') as f:
    data = pickle.load(f)
st.write("Data loaded successfully!", data)

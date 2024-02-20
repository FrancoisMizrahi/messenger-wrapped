import streamlit as st

from utils import upload_file

st.title('Messenger Wrapped')

data = upload_file()

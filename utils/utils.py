import streamlit as st

from config import *
from .upload_utils import load_json


def upload_file():
    uploaded_file = st.file_uploader("Choose a JSON file", type="json")
    if uploaded_file is not None:
        data = load_json(uploaded_file)
        return data
    else:
        st.write("Please upload a JSON file.")
        
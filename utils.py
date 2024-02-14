import streamlit as st
import json
import re
from functools import partial



def load_json(file_name):
    escapes = partial(re.compile(rb'\\u00([\da-f]{2})').sub,lambda m: bytes.fromhex(m[1].decode()),)

    with open(file_name, 'rb') as binary_data:
        repaired = escapes(binary_data.read())
    parsed_json = json.loads(repaired)
    return parsed_json


def upload_file():
    uploaded_file = st.file_uploader("Choose a JSON file", type="json")
    if uploaded_file is not None:
        data = json.load(uploaded_file)
        st.json(data)
    else:
        st.write("Please upload a JSON file.")
        
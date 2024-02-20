import streamlit as st
import json
import re
from functools import partial


def temp_load(uploaded_file, file_name):
    data = json.load(uploaded_file)
    json_object = json.dumps(data, indent=4)
    with open(file_name, "w") as outfile:
        outfile.write(json_object)


def repair_json(file_name):
    escapes = partial(re.compile(rb'\\u00([\da-f]{2})').sub,lambda m: bytes.fromhex(m[1].decode()),)
    with open(file_name, 'rb') as binary_data:
        repaired = escapes(binary_data.read())
    parsed_json = json.loads(repaired)
    
    return parsed_json


def load_json(uploaded_file):
    file_name = "temp_storage/temp_load.json"
    temp_load(uploaded_file, file_name)
    parsed_json= repair_json(file_name)
    
    return parsed_json


def upload_file():
    uploaded_file = st.file_uploader("Choose a JSON file", type="json")
    if uploaded_file is not None:
        data = load_json(uploaded_file)
        return data
    else:
        st.write("Please upload a JSON file.")
        
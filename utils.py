import streamlit as st
import json
import re
import os

from functools import partial
from config import *



def temp_load(uploaded_file, file_name):
    data = json.load(uploaded_file)
    json_object = json.dumps(data, indent=4)
    with open(file_name, "w") as outfile:
        outfile.write(json_object)

def remove_temp_json(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        st.warning("The file does not exist", icon="⚠️")


def repair_json(file_name):
    escapes = partial(re.compile(rb'\\u00([\da-f]{2})').sub,lambda m: bytes.fromhex(m[1].decode()),)
    with open(file_name, 'rb') as binary_data:
        repaired = escapes(binary_data.read())
    parsed_json = json.loads(repaired)
    remove_temp_json(file_name)
    return parsed_json


def load_json(uploaded_file):
    temp_load(uploaded_file, temp_storage_file_name)
    parsed_json= repair_json(temp_storage_file_name)
    
    return parsed_json


def upload_file():
    uploaded_file = st.file_uploader("Choose a JSON file", type="json")
    if uploaded_file is not None:
        data = load_json(uploaded_file)
        return data
    else:
        st.write("Please upload a JSON file.")
        
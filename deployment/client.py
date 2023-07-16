import os

import streamlit as st

import httpx
# from utils import hf_ents_to_displacy_format, make_color_palette
from httpx import HTTPError
import random

# Modify these
API_URL = "http://127.0.0.1:7863/predictions/"
MODEL_NAME = "ner_model"
LOCAL = False

# from https://github.com/explosion/spacy-streamlit/util.py#L26
WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem; margin-bottom: 2.5rem">{}</div>"""

if not LOCAL:
    API_URL = "https://api-inference.huggingface.co/models/"
    MODEL_NAME = "dslim/bert-base-NER"
    
API_URL = st.sidebar.text_input("API URL", API_URL)
MODEL_NAME = st.sidebar.text_input("MODEL NAME", MODEL_NAME)
# st.write(f"API endpoint: {API_URL}{MODEL_NAME}")


def raise_on_not200(response):
    if response.status_code != 200:
        st.write("There was an error!")
        st.write(response)


client = httpx.Client(timeout=1000, event_hooks={"response": [raise_on_not200]})


def sanitize_input(input_):
    clean = str(input_)
    return clean


def predict(model, input_):
    res = client.post(API_URL + model, json=input_)
    return res.json()


def display(bert_ents):
    pass


st.header("Angio Classification")

# input_ = st.text_input("Input", "My name is Ceyda and I live in Seoul, Korea.")
# input_ = sanitize_input(input_)
# bert_ents = predict(MODEL_NAME, input_)


uploaded_files = st.file_uploader("Choose image file", accept_multiple_files=True)

for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)


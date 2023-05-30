import streamlit as st

import cloudscraper

from bs4 import BeautifulSoup

import time

def mdiskpro(url):

    client = cloudscraper.create_scraper(allow_brotli=False)

    DOMAIN = "https://mdisk.pro"

    ref = "https://m.meclipstudy.in/"

    h = {"referer": ref}

    resp = client.get(url, headers=h)

    soup = BeautifulSoup(resp.content, "html.parser")

    inputs = soup.find_all("input")

    data = {input.get('name'): input.get('value') for input in inputs}

    h = {"x-requested-with": "XMLHttpRequest"}

    time.sleep(8)

    r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)

    try:

        return r.json()['url']

    except:

        return "Something went wrong :("

# Streamlit app

st.title("Mdisk Pro Link Converter")

# Input URL

url = st.text_input("Enter the Mdisk Pro URL")

# Convert button

if st.button("Convert"):

    if url:

        converted_url = mdiskpro(url)

        st.success("Converted Link:")

        st.write(converted_url)

    else:

        st.warning("Please enter a URL")


import streamlit as st

import cloudscraper

from bs4 import BeautifulSoup

import time

import requests


def mdisk(url):
    header = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://mdisk.me/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    	 }
    
    inp = url 
    fxl = inp.split("/")
    cid = fxl[-1]

    URL = f'https://diskuploader.entertainvideo.com/v1/file/cdnurl?param={cid}'
    res = requests.get(url=URL, headers=header).json()
    return res['download'] + '\n\n' + res['source']


###################################################################


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

def shareus(url):

    token = url.split("=")[-1]

    bypassed_url = "https://us-central1-my-apps-server.cloudfunctions.net/r?shortid=" + token

    response = requests.get(bypassed_url).text

    return response

# Streamlit app

st.title("Link Converter")

# Select conversion method

conversion_method = st.selectbox("Select conversion method", ["Mdisk Pro", "Shareus", "URL Shortx", "Mdisk.me"])

# Input URL

url = st.text_input("Enter the URL")

# Convert button

if st.button("Convert"):

    if url:

        if conversion_method == "Mdisk Pro":

            converted_url = mdiskpro(url)

        elif conversion_method == "Shareus":

            converted_url = shareus(url)

        elif conversion_method == "Mdisk.me":
            converted_url = mdisk(url)

        st.success("Converted Link:")

        st.write(converted_url)

    else:

        st.warning("Please enter a URL")



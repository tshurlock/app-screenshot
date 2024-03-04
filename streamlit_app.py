import streamlit as st
import time
import psutil
import random
import os
import sys
from PIL import Image, ImageDraw, ImageOps
from PIL.Image import Resampling
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from os.path import exists

st.set_page_config(page_title="get selenium working", page_icon=':wave:')
st.title('get sleen wokring')
st.warning('An app for taking screenshot of a Streamlit app.')

#@st.cache_resource
def get_driver():
    options = webdriver.ChromeOptions()
    
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    #options.add_argument(f"--window-size={width}x{height}")
    
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    
    return webdriver.Chrome(service=service, options=options)

driver = get_driver()
runner = str(47595)
ParkrunURL = "https://www.parkrun.org.uk//parkrunner//" + runner + "//all//"
try:
    #table = driver.find_element(By.XPATH, "(//table)[0]")
    vegetable = driver.find_element(By.CLASS_NAME, "sortable")
    #table_element = driver.find_element_by_id("results")
    st.write('we got it')
except:
    st.write('this table was not found')  





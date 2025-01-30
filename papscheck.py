from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time
import sys
import streamlit as st
# from webdriver_manager.chrome import ChromeDriverManager

# import os
# from datetime import datetime
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# Set page configuration
st.set_page_config(
    page_title="prac Page",
    page_icon="🌟",
    layout="centered",  # Options: "centered", "wide"
    initial_sidebar_state="collapsed"
)

st.header('E-Manifest Tracker')


# Directory to save uploaded files


tab2, tab3= st.tabs(["PARS (ACI)", "PAPS (ACE)"])

with tab2:
    pars = st.text_input('Enter PARS# only last 6 digits', key='pars')
    search_pars = st.button('Search', key = 'search_pars')
    st.write('OR')
    truck = st.text_input('Enter Truck# ', key='truck')
    search_truck = st.button('Search', key = 'search_truck')

    if search_pars:
        st.write("Checking through pars#...")
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Headless mode
        chrome_options.add_argument("--disable-gpu")  # Required for Linux/macOS
        chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
        chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resources
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--remote-debugging-port=9222")
        chrome_options.add_argument("--disable-software-rasterizer")


        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        url = 'https://ace.avaal.com/manifest/profile/login.jsp'
        user = "dfh"
        passs = "dfh@12345"
        driver.get(url)

        # add user
        driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(user)
        time.sleep(1)
        # add password
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(passs)
        time.sleep(1)
        # click sigin button
        driver.find_element(By.XPATH, '//*[@id="btnLogin"]').click()
        time.sleep(1)
        #click aci trips
        driver.find_element(By.XPATH, '//*[@id="topnav"]/div/span[10]/span/a').click()
        time.sleep(1)
        #pars input
        driver.find_element(By.XPATH, '//*[@id="hidenSearchForm"]/td[1]/table/tbody/tr[1]/td[2]/input').send_keys(pars)
        time.sleep(1)
        #click search to look for pars
        driver.find_element(By.XPATH, '//*[@id="SearchButtonSection"]').click()
        time.sleep(1)
        #click on pars to open trip
        while True:
            try:
                driver.find_element(By.XPATH, '//*[@id="datatable"]/tbody/tr/td[2]/a').click()
                time.sleep(1)
                break
            except NoSuchElementException:
                st.write("PARS not found. Try contacting customs team")
                driver.quit()
                st.stop()
            
          
        # #click print button
        driver.find_element(By.XPATH, '//*[@id="printBtn"]').click()
        time.sleep(1)
        # click to send aci by email
        print('child html opened')

        #enter iframe for send email to driver 
        iframe=driver.find_element(By.XPATH,'//*[@id="windowSize"]/tbody/tr[2]/td[2]/div/div/table/tbody/tr/td/iframe')
        driver.switch_to.frame(iframe)
        time.sleep(1)

        #click send email to driver
        txt=driver.find_element(By.XPATH, '/html/body/div[1]/button[2]').click()
        time.sleep(1)

        #click send
        txt=driver.find_element(By.XPATH, '/html/body/div/button[1]').click()
        time.sleep(1)

        driver.quit()
        st.write('aci sent')
        
    
    if search_truck:
        st.write("Checking through truck#...")
        options = Options()
        options.add_argument('--headless')
        chromedrivepath = r"C:\Users\sarap\chromedriver-win64\chromedriver.exe"
        finalpath = chromedrivepath.replace('\\',"/")
        service = Service(executable_path = finalpath)
        driver = webdriver.Chrome(service = service)#, options=options)
        url = 'https://ace.avaal.com/manifest/profile/login.jsp'
        user = "dfh"
        passs = "dfh@12345"
        driver.get(url)

        # add user
        driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(user)
        time.sleep(1)
        # add password
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(passs)
        time.sleep(1)
        # click sigin button
        driver.find_element(By.XPATH, '//*[@id="btnLogin"]').click()
        time.sleep(1)
        #click aci trips
        driver.find_element(By.XPATH, '//*[@id="topnav"]/div/span[10]/span/a').click()
        time.sleep(1)
        #truck  input
        driver.find_element(By.XPATH, '//*[@id="hidenSearchForm"]/td[1]/table/tbody/tr[2]/td[2]/input').send_keys(truck)
        time.sleep(1)
        #click search to look for pars
        driver.find_element(By.XPATH, '//*[@id="SearchButtonSection"]').click()
        time.sleep(1)
        #click on pars to open trip
        driver.find_element(By.XPATH, '//*[@id="datatable"]/tbody/tr/td[2]/a').click()
        time.sleep(1)         
        # #click print button
        driver.find_element(By.XPATH, '//*[@id="printBtn"]').click()
        time.sleep(1)
        # click to send aci by email
        print('child html opened')

        #enter iframe for send email to driver 
        iframe=driver.find_element(By.XPATH,'//*[@id="windowSize"]/tbody/tr[2]/td[2]/div/div/table/tbody/tr/td/iframe')
        driver.switch_to.frame(iframe)
        time.sleep(1)

        #click send email to driver
        txt=driver.find_element(By.XPATH, '/html/body/div[1]/button[2]').click()
        time.sleep(1)

        #click send
        txt=driver.find_element(By.XPATH, '/html/body/div/button[1]').click()
        time.sleep(1)

        driver.quit()
        st.write('aci sent')

        






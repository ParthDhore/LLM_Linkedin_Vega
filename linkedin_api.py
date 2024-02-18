# Imports for Selenium WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

# Import pandas library and alias it as pd
import pandas as pd

# Import time module
import time

# Import os module
import os

url="https://in.indeed.com/"

ser=webdriver.ChromeService("C:/chromedriver.exe")
driver=webdriver.Chrome(service=ser)
driver.get(url)
driver.implicitly_wait(5)

def create_joblist(job_title: str, job_loc: str):
    # Find the input field element (assuming it has an ID attribute)
    job_input_field = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"text-input-what")))
    place_input_field = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"text-input-where")))

    # Type text into the input field
    job_input_field.send_keys(job_title)
    place_input_field.send_keys(job_loc)

    # Simulate pressing the "Enter" key
    place_input_field.send_keys(Keys.ENTER)

    filter_radius_btn=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"filter-radius")))
    filter_radius_btn.send_keys(Keys.ENTER)
    filter_radius_menu=driver.find_element(By.ID, "filter-radius-menu")
    radius_elements=filter_radius_menu.find_elements(By.TAG_NAME,"li")

    for li in radius_elements:
        anchor=li.find_element(By.TAG_NAME,"a")
        text=anchor.text
        if(text=="Within 100 kilometres"):
            href=anchor.get_attribute('href')
            driver.close()
            driver.get("https://in.indeed.com/"+href)
    
    time.sleep(1000)

create_joblist("datascience","bengaluru")
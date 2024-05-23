from selenium import webdriver
from selenium.webdriver.common.by import By

def get_images_url(driver,url):        
    driver.get(url)   
    images  = driver.find_elements(By.TAG_NAME,"img")
    return [img.get_attribute('src') for img in images]
    
    
def run_chrome(url):
   with webdriver.Chrome() as driver:
       return get_images_url(driver,url)

def run_firefox(url):
    with webdriver.Firefox() as driver:
       return get_images_url(driver,url)
        
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def get_images_url(driver,url):        
    driver.get(url)   
    images  = driver.find_elements(By.TAG_NAME,"img")
    return [img.get_attribute('src') for img in filter(lambda img: int(img.get_attribute('width'))>12,images)]
    
    
def run_chrome(url):
   with webdriver.Chrome() as driver:
       return get_images_url(driver,url)

def run_firefox(url):
    with webdriver.Firefox() as driver:
       return get_images_url(driver,url)
        
def run(url,browser_name):
    if browser_name == "chrome":
        return run_chrome(url)
    
    if browser_name == "firefox":
        return run_firefox(url)
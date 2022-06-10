import selenium
from selenium import webdriver

PATTH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATTH)

driver.get("https://www.youtube.com/")
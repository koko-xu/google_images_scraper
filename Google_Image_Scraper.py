""" Scrape Image URLs """

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import selenium
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui

df = pd.DataFrame(columns=["name", "link"])

driver = webdriver.Chrome(ChromeDriverManager().install())
# Cattail images link
driver.get("https://www.google.com/search?q=cattail&tbm=isch&chips=q:cattail,g_1:plant:dhttNngNpPY%3D&hl=en&sa=X&ved=2ahUKEwjqtK6yjf74AhU5rXIEHQhYCcQQ4lYoAnoECAEQJA&biw=1920&bih=1001#imgrc=xnnvCgWYaXhEkM")
# Not cattail images link
# driver.get("https://www.google.com/search?q=plants+and+flowers+in+nature&tbm=isch&ved=2ahUKEwiWt7DVpf74AhVOrnIEHQX7B2QQ2-cCegQIABAA&oq=plants+and+flowers+in+nature&gs_lcp=CgNpbWcQAzoECAAQQzoFCAAQgAQ6BggAEB4QBzoICAAQHhAHEAU6CAgAEB4QCBAHOgYIABAeEAhQ4x5Y5ydg9yhoAHAAeACAAT-IAeAEkgECMTKYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=viXTYpbgFs7cytMPhfafoAY&bih=1001&biw=1300&hl=en#imgrc=StfA5K6hJDgBqM")
driver.implicitly_wait(5)

for i in range(500):
    link_path = "//*[@id=\"Sva75c\"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img"
    link = driver.find_element(by=By.XPATH, value=link_path).get_attribute("src")

    if "https" in link:
        print(link)

    next_path = "//*[@id=\"Sva75c\"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[1]/a[3]"
    next = driver.find_element(by=By.XPATH, value=next_path)
    next.click()

    driver.implicitly_wait(5)

driver.close()

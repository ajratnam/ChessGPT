from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from config import *


def create_browser():
    options = Options()
    PROFILE_PATH and options.add_argument(f"--user-data-dir={PROFILE_PATH}")
    PROFILE_NAME and options.add_argument(f"--profile-directory={PROFILE_NAME}")
    options.add_experimental_option("detach", DETACH)
    return webdriver.Chrome(options=options)


def open_chess(driver: WebDriver):
    driver.get("https://www.chess.com/play/computer")
    if first_div := driver.find_elements(By.CLASS_NAME, "modal-first-time-button"):
        first_div[0].find_element(By.TAG_NAME, "button").click()

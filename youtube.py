from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.youtube.com/")


def youtube_list():
    youtube_see = driver.find_element(By.ID, 'search')
    youtube_see.send_keys("Tutorial of Github")

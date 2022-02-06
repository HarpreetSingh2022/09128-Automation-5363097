from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.google.com/")


def googlesee():
    google_searchbox = driver.find_element(By.ID, 'input')
    google_searchbox.send_keys("Google search Github")

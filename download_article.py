from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time
import time
import random

from generate_word import generate_word_doc



# Create the WebDriver with EdgeOptions
driver = webdriver.Edge()
driver.get("https://nce.koolearn.com/diercetingli/")

time.sleep(20)

with open("E:\\github\\downloadnoe\\book20.txt", "r") as f:
     url_lists = f.readlines()

for url in url_lists:
    # Navigate to a URL
    # driver.get(f'https://nce.koolearn.com/diercetingli/{page}.html')
    driver.get(url)

    # Wait for the page to load (you can adjust the sleep time as needed)
    time.sleep(random.randint(2, 15))

    # Find the <ul> element with class "xqy_entry_list"
    element = driver.find_element(By.CLASS_NAME,'xqy_core_tit')
    title = element.text.split(":")[1]

    # Find all child <li> elements of the <ul>
    content = element.find_elements(By.XPATH, "//p[text()='　　1.课文']").find_element_by_xpath("following-sibling::*").text

    generate_word_doc("E:\github\downloadnoe\bookII", title, content)

# Close the browser window
driver.quit()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import time
import random
import re
import base64

from generate_word import generate_word_doc

def clean_filename(filename):
    # Define a regex pattern to match invalid characters
    invalid_chars_pattern = re.compile(r'[\\/:"*?<>|]+')

    # Replace invalid characters with underscores
    cleaned_filename = re.sub(invalid_chars_pattern, '_', filename)

    return cleaned_filename

# Create the WebDriver with EdgeOptions
# driver = webdriver.Chrome()

chrome_options = Options()
# chrome_options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)

# Specify the path to your ChromeDriver executable
chrome_driver_path = 'C:\\apps\\chromedriver.exe'

# Create a Chrome WebDriver with the specified options
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

with open("E:\\github\\downloadnoe\\guzhi.txt", "r") as f:
     url_lists = f.readlines()
index = 1

for url in url_lists:
    # Navigate to a URL
    # driver.get(f'https://nce.koolearn.com/diercetingli/{page}.html')
    driver.get(url)

    # Wait for the page to load (you can adjust the sleep time as needed)
    time.sleep(random.uniform(2, 15))

     # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    body = driver.find_element_by_tag_name("body")

    # Get initial body height
    initial_body_height = driver.execute_script("return document.body.scrollHeight")

    # Set a threshold for the number of iterations with no change in body height
    threshold = 3  # You can adjust this value based on your requirements

    # Initialize a counter for consecutive iterations with no change
    no_change_counter = 0
    # scrolled_to_bottom = False
    is_body_bottom_displayed = False
    # Perform scrolling until the body height no longer changes
    while no_change_counter < threshold or not is_body_bottom_displayed:
        body.send_keys(Keys.PAGE_DOWN)
        # Wait for a short time to allow the content to load (you can adjust the sleep duration)
        time.sleep(random.uniform(1, 3))

        # scrolled_to_bottom = driver.execute_script("return window.innerHeight + window.scrollY >= document.body.scrollHeight;")

        # Get the current body height
        current_body_height = driver.execute_script("return document.body.scrollHeight")

        print (f"scrolling, initial_body_height:{initial_body_height}, current_body_height:{current_body_height}")
        # Check if the body height has changed
        if current_body_height == initial_body_height:
            no_change_counter += 1
        else:
            no_change_counter = 0  # Reset the counter if there is a change
        
        # Update the initial body height for the next iteration
        initial_body_height = current_body_height

        # Get the height of the viewport
        viewport_height = driver.execute_script("return window.innerHeight;")

        # Get the position of the bottom of the body element
        body_bottom_position = driver.execute_script("return document.body.getBoundingClientRect().bottom;")

        # Check if the bottom of the body element is displayed in the current window
        is_body_bottom_displayed = abs(body_bottom_position - viewport_height) < 2
        print(f"is_body_bottom_displayed:{is_body_bottom_displayed}, body_bottom_position:{body_bottom_position}, viewport_height:{viewport_height}")

    
    body.send_keys(Keys.END)

    time.sleep(random.uniform(1, 5))
    
    # Execute Chrome DevTools Protocol command to save the page as PDF
    result = driver.execute_cdp_cmd('Page.printToPDF', {'landscape': False, 'displayHeaderFooter': False})
    filename = 'E:\github\\downloadnoe\\guzhi\\' + "{:02d}".format(index) + clean_filename(driver.title) + '.pdf'
    index += 1
    # Specify the path where you want to save the PDF

    # Save the PDF content to a file
    with open(filename, 'wb') as pdf_file:
        pdf_file.write(base64.b64decode(result['data']))

# Close the browser window
driver.quit()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time
import random

# Create a new instance of the Edge WebDriver
driver = webdriver.Chrome()

all_urls = []
for page in range(1):
    # Navigate to a URL
    # driver.get(f'https://nce.koolearn.com/diercetingli/{page}.html')
    driver.get(f'https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI5NzA5MDEzNg==&action=getalbum&album_id=2737029876410662914&scene=21#wechat_redirect')

    # Wait for the page to load (you can adjust the sleep time as needed)
    time.sleep(2)

    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    body = driver.find_element_by_tag_name("body")

    scroll_times = 10

    '''while scroll_times > 0:
        body.send_keys(Keys.END)
        time.sleep(random.randint(1, 3))
        scroll_times -= 1
    '''
    #time.sleep(20)

    # Find the <ul> element with class "xqy_entry_list"
    #ul_element = driver.find_elements(By.CLASS_NAME,'album__list-item js_album_item js_wx_tap_highlight wx_tap_cell')

    # Find all child <li> elements of the <ul>
    li_elements = driver.find_elements(By.TAG_NAME, 'li')

    # Loop through each <li> element
    for li_element in li_elements:
        # Find the <h3> element within the <li>
        href_value = li_element.get_attribute('data-link')

        # Print or use the href value as needed
        all_urls.append(href_value)

# Remove None elements using list comprehension
filtered_list = [item for item in all_urls if item is not None]

with open("E:\\github\\downloadnoe\\2023.txt", "w") as f:
    f.writelines('\n'.join(filtered_list))
# Close the browser window
driver.quit()
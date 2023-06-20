from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import pandas as pd

start_time = time.time()
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)
driver.get("https://fifthwall.com/partners")

screen_width = driver.execute_script("return window.screen.width;")
screen_height = driver.execute_script("return window.screen.height;")

new_width = int(screen_width / 2)
new_height = screen_height
new_position_x = 0
new_position_y = 0

driver.set_window_size(new_width, new_height)
driver.set_window_position(new_position_x, new_position_y)

time.sleep(2)

driver.execute_script("window.scrollTo(0, 1600);")
time.sleep(2)

bio_links = driver.find_elements(
    "xpath", "//a[contains(@class, 'popup-opener js-popup-open card-link')]")
bio_links[0].click()
time.sleep(5)

data = []

# while True:
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

results = soup.find_all('div', class_='row')
for result in results:
    name_element = result.find('h1')
    name = name_element.text if name_element else ''

    web_element = result.find('a', class_='link')
    web = web_element['href'] if web_element else ''

    desc_element = result.find('div', class_='markdown-content')
    desc = desc_element.text if desc_element else ''

    data.append([name, web, desc])
    print(f'Scraped {name}')
    time.sleep(2)

    # next_popup = driver.find_elements("xpath", "//a[contains(@data-direction, 'next')]")
    # if not next_popup:
    #     break
    # next_popup[0].click()
    # time.sleep(5)

df = pd.DataFrame(data)
df.to_csv('scraped-csv/fifthwallpart.csv', index=False)
end_time = time.time()
print(f'Time taken: {end_time - start_time} seconds')
driver.quit()


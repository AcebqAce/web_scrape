from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import pandas as pd

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.eurazeo.com/en/investments")

screen_width = driver.execute_script("return window.screen.width;")
screen_height = driver.execute_script("return window.screen.height;")

new_width = int(screen_width / 2)
new_height = screen_height
new_position_x = 0
new_position_y = 0

driver.set_window_size(new_width, new_height)
driver.set_window_position(new_position_x, new_position_y)

time.sleep(2)
for i in range(37):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

driver.execute_script("window.scrollTo(0, 1600);")
time.sleep(2)

bio_links = driver.find_elements("xpath", "//div[contains(@class, 'bloc-portefeille-wrap')]")
bio_links[0].click()
time.sleep(5)

data = []

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

results = soup.find_all('div', class_='portefeille_quickview')
for result in results:
    name_element = result.find('h3')
    name = name_element.text.replace('\t', '').strip() if name_element else ''

    web_element = result.find('a', class_='link')
    web = web_element['href'] if web_element else ''

    data.append([name, web])
    print(f'Scraped {name}')

    time.sleep(2)

df = pd.DataFrame(data)
df.to_csv('scraped-csv/eurazeo.csv', index=False)

time.sleep(2)

driver.quit()


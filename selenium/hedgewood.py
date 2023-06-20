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
driver.get("https://hedgewood.com/")

screen_width = driver.execute_script("return window.screen.width;")
screen_height = driver.execute_script("return window.screen.height;")

new_width = int(screen_width / 2)
new_height = screen_height
new_position_x = 0
new_position_y = 0

driver.set_window_size(new_width, new_height)
driver.set_window_position(new_position_x, new_position_y)

time.sleep(2)

driver.execute_script("window.scrollTo(0, 2600);")
time.sleep(2)

bio_links = driver.find_elements(
    "xpath", "//a[contains(@class, 'expand-portfolio')]")
bio_links[0].click()
time.sleep(5)

data = []

while True:
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    
    results = soup.find_all('div', id='portfolio-ajax-single')
    for result in results:
        name_element = result.find('h2')
        name = name_element.text if name_element else ''

        web_element = result.find_all('a')
        web = web_element[-1]['href'] if web_element else ''

        data.append([name, web])
        print(f'Scraped {name}')
        time.sleep(2)

    next_popup = driver.find_elements("xpath", "//a[contains(@id, 'next-portfolio')]")
    if not next_popup:
        break
    next_popup[0].click()
    time.sleep(5)

df = pd.DataFrame(data)
df.to_csv('scraped-csv/hedgewood.csv', index=False)
end_time = time.time()
print(f'Time taken: {end_time - start_time} seconds')
driver.quit()


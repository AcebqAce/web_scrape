from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time

start_time = time.time()

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.nycfounderguide.com/investors")

screen_width = driver.execute_script("return window.screen.width;")
screen_height = driver.execute_script("return window.screen.height;")

new_width = int(screen_width / 2)
new_height = screen_height
new_position_x = 0
new_position_y = 0

driver.set_window_size(new_width, new_height)
driver.set_window_position(new_position_x, new_position_y)
time.sleep(5)

data = []

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

results2 = soup.find_all('a', class_='card investor-card w-inline-block')
for result2 in results2:
    name_element = result2.find('h5', class_='text-center')
    name = name_element.text if name_element else ''

    stage_element = result2.find('li', class_='card-list-item')
    stage = stage_element.text.replace('Average Check Size', '').strip() if stage_element else ''

    locat_element = result2.find_all('li', class_='card-list-item')
    locat = locat_element[1].text.replace('Stage', '').strip() if len(locat_element) > 1 else ''

    size_element = result2.find_all('li', class_='card-list-item')
    size = size_element[2].text.replace('SectorS', '').strip() if len(size_element) > 2 else ''

    sector_element = result2.find_all('li', class_='card-list-item')
    sector = sector_element[-1].text.replace('Sample Portfolio Companies', '').strip() if len(sector_element) > 0 else ''

    data.append([name, stage, locat, size, sector])
    print(f'Scraped {name}')    

df = pd.DataFrame(data)
df.to_csv('scraped-csv/nycfounderguideinvest2.csv', index=False)

end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
driver.quit()


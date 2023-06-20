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

info_links = driver.find_elements("xpath", "//a[contains(@class, 'card investor-card w-inline-block')]")
data = []

for link in info_links:
    if link is not None:
        link_url = link.get_attribute("href")

    driver.execute_script("window.open('" + link_url + "', '_blank');")
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(5)

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    results = soup.find_all('div', class_='content-width-medium')
    for result in results:
        name_element = result.find('h1')
        name = name_element.text if name_element else ''

        bio_element = result.find('p', class_='styles__investorBio_IRf7S')
        bio = bio_element.text if bio_element else ''

        web_element = result.find_all('a')
        web = web_element[-1]['href'] if len(web_element) > -1 else ''
  
    data.append([name, bio, web])
    print(f'Scraped {name}')

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    

df = pd.DataFrame(data)
df.to_csv('scraped-csv/nycfounderguideinvest.csv', index=False)

time.sleep(2)
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
driver.quit()


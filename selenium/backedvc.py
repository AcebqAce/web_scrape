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
driver.get("https://www.backed.vc/our-investments/")

screen_width = driver.execute_script("return window.screen.width;")
screen_height = driver.execute_script("return window.screen.height;")

new_width = int(screen_width / 2)
new_height = screen_height
new_position_x = 0
new_position_y = 0

driver.set_window_size(new_width, new_height)
driver.set_window_position(new_position_x, new_position_y)

time.sleep(2)
driver.execute_script("window.scrollTo(0, 1000);")

bio_links = driver.find_elements("xpath", "//div[contains(@class, 'elementor-button-wrapper')]")

data = []
num_popups = 0

for link in bio_links:
    link.click()

    time.sleep(5)

    page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'html.parser')

    results = soup.find_all('section', id='investment-popup')
    for result in results:
        name_element = result.find_all('h5', class_='elementor-heading-title elementor-size-default')
        name = name_element[6].text if len(name_element) > 6 else ''

        locat_element = result.find_all('h5', class_='elementor-heading-title elementor-size-default')
        locat = locat_element[3].text if len(locat_element) > 3 else ''

        web_element = result.find('a')
        web = web_element['href'] if web_element else ''

        data.append([name, locat, web])
        print(f'Scraped {name}')

    time.sleep(2)
    
    num_popups += 1
    if num_popups > 1:
        driver.execute_script("window.scrollBy(0, -500);")
    else:
        continue

    close_popup = driver.find_element("xpath", "//a[contains(@class, 'dialog-close-button dialog-lightbox-close-button')]")
    close_popup.click()

df = pd.DataFrame(data)
df.to_csv('backedvc.csv', index=False)

time.sleep(2)

driver.quit()


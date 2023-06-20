from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd
from bs4 import BeautifulSoup

start_time = time.time()
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://matterscale.com/portfolio/")

driver.set_window_size(int(driver.execute_script("return window.screen.width;")) // 2,
                       driver.execute_script("return window.screen.height;"))
driver.set_window_position(0, 0)
time.sleep(2)

driver.execute_script("window.scrollTo(0, 500);")
time.sleep(2)

data = []
bio_links = driver.find_elements("xpath", "//div[contains(@class, 'companies-loop-card h-100')]")
i = 0
while i < len(bio_links):
    link = bio_links[i]
    driver.execute_script("arguments[0].scrollIntoView(true);", link)
    time.sleep(2)
    link.click()
    time.sleep(5)

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    results = soup.find_all('div', class_='company-modal-box')
    for result in results:
        name_element = result.find('h1')
        name = name_element.text if name_element else ''

        locat_element = result.find('p', class_='mb-0 company-location')
        locat = locat_element.text if locat_element else ''

        web_element = result.find('a')
        web = web_element['href'] if web_element else ''

        data.append([name, locat, web])
        print(f'Scraped {name}')

        time.sleep(2)

    close_popup = driver.find_element(By.CSS_SELECTOR, "svg.modal-close-icon")
    close_popup.click()
    time.sleep(2)
    
    i += 1
    if i == len(bio_links):
        break
    else:
        bio_links = driver.find_elements("xpath", "//div[contains(@class, 'companies-loop-card h-100')]")

pd.DataFrame(data).to_csv('scraped-csv/matterscale.csv', index=False)
end_time = time.time()
print('\n' f'Scraping complete in {end_time - start_time} seconds')



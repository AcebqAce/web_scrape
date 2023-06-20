from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
from bs4 import BeautifulSoup

start_time = time.time()
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://leadedge.com/portfolio/")

driver.set_window_size(int(driver.execute_script("return window.screen.width;")) // 2, 
                       driver.execute_script("return window.screen.height;"))
driver.set_window_position(0, 0)
time.sleep(2)

bio_link = driver.find_element("xpath", "//a[contains(@class, 'portfolio')]")
bio_link.click()
time.sleep(2)

data = []

num_popups = 79
num_clicked = 0

while num_clicked < num_popups:
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    results = soup.find_all('div', class_='fancybox-inner')
    for result in results:
        name_element = result.find('h3')
        name = name_element.text if name_element else ''

        web_element = result.find('a')
        web = web_element['href'] if web_element else ''
        
        data.append([name, web])
        print(f'Scraped {name}')
        time.sleep(2)

    next_popup = driver.find_elements("xpath", "//button[contains(@class, 'fancybox-arrow fancybox-arrow--right')]")
    next_popup[0].click()
    num_clicked += 1

    if num_clicked == num_popups:
        break
    time.sleep(2)

df = pd.DataFrame(data)
df.to_csv('scraped-csv/leadedge.csv', index=False)

end_time = time.time()
print('\n' f'Scraping complete in {end_time - start_time} seconds')

driver.quit()

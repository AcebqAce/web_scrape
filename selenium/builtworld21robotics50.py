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
driver.get("https://builtworlds.com/insights/2021-robotics-50-list/")

screen_width = driver.execute_script("return window.screen.width;")
screen_height = driver.execute_script("return window.screen.height;")

new_width = int(screen_width / 2)
new_height = screen_height
new_position_x = 0
new_position_y = 0

driver.set_window_size(new_width, new_height)
driver.set_window_position(new_position_x, new_position_y)
time.sleep(2)

driver.execute_script("window.scrollTo(0, 1500);")
time.sleep(2)

info_links = driver.find_elements("xpath", "//div[contains(@class, 'fl-rich-text')]//h2//a")
data = []

for link in info_links:
    link_url = link.get_attribute("href")
    if link_url is not None:
        driver.execute_script("window.open('" + link_url + "', '_blank');")
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(5)

        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        results = soup.find_all('main', id='main')
        for result in results:
            name_element = result.find('h1', class_='entry-title')
            name = name_element.text.split('About ')[-1] if name_element else ''

            desc_element = result.find('div', class_='entry-content')
            desc = desc_element.text.replace('\n', '').replace('\t', '').strip() if desc_element else ''

            web_element = result.find('a', class_='external')
            web = web_element['href'] if web_element else ''

            date_element = result.find_all('dd')
            date = date_element[1].text.replace('\n', '').replace('\t', '').strip() if date_element else ''
            
            locat_element = result.find_all('dd')
            locat = locat_element[2].text.replace('\n', '').replace('\t', '').strip() if locat_element else ''

            data.append([name, web, desc, date, locat])
            print(f'Scraped {name}')

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)

df = pd.DataFrame(data)
df.to_csv('scraped-csv/builtworld21robotics50.csv', index=False)

time.sleep(2)
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
driver.quit()


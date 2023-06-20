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
driver.get("https://signal.nfx.com/investor-lists/top-real-estate-proptech-series-a-investors")

screen_width = driver.execute_script("return window.screen.width;")
screen_height = driver.execute_script("return window.screen.height;")

new_width = int(screen_width / 2)
new_height = screen_height
new_position_x = 0
new_position_y = 0

driver.set_window_size(new_width, new_height)
driver.set_window_position(new_position_x, new_position_y)
time.sleep(2)

while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(2)
    try:
        show_more = driver.find_element("xpath", "//button[contains(@class, 'btn-xs sn-light-greyblue-accent-button sn-center mt3 mb2 btn btn-default')]")
        show_more.click()
        time.sleep(5)
    except:
        break

data = []

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

results = soup.find_all('div', class_='pr3')
for result in results:
    name_element = result.find('a')
    name = name_element.text if name_element else ''

    com_element = result.find_all('a')
    com = com_element[1].text if len(com_element) > 1 else ''

    title_element = result.find_all('span')
    title = title_element[1].text if len(title_element) > 2 else ''

    spot_element = result.find('span', class_='vc-search-card-value')
    spot = spot_element.text if spot_element else ''

    rang_element = result.find_all('span', class_='vc-search-card-value')
    rang = rang_element[1].text if len(rang_element) > 1 else ''

    data.append([name, com, title, spot, rang])
    print(f'Scraped {name}')

df = pd.DataFrame(data)
df.to_csv('scraped-csv/signalnfxtoperprop2.csv', index=False)

time.sleep(2)
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
driver.quit()


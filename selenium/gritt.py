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
driver.get("https://angels.tryretool.com/embedded/public/a5debca4-cbb2-421f-ab2b-a8dab755d979?id=undefined")

screen_width = driver.execute_script("return window.screen.width;")
screen_height = driver.execute_script("return window.screen.height;")

new_width = int(screen_width / 2)
new_height = screen_height
new_position_x = 0
new_position_y = 0

driver.set_window_size(new_width, new_height)
driver.set_window_position(new_position_x, new_position_y)

time.sleep(17)

driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
time.sleep(1)

data = []

# while True:
#     page_source = driver.page_source
#     soup = BeautifulSoup(page_source, 'html.parser')
    
#     results = soup.find_all('div', class_='retool-grid with-padding')
#     for result in results:
#         name_element = result.find('div', {'data-testid': 'table1-ffirstname-0'})
#         name = name_element.text if name_element else ''

#         data.append([name])
#         print(f'Scraped {name}')
#         time.sleep(2)

next_popup = driver.find_elements("xpath", "//*[@id='table-table1']/div/div/div[2]/div/div[1]/div/div[2]")


next_popup[0].click()
time.sleep(10)

df = pd.DataFrame(data)
df.to_csv('scraped-csv/gritt.csv', index=False)
end_time = time.time()
print(f'Time taken: {end_time - start_time} seconds')
# driver.quit()


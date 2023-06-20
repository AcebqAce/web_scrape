from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time

start_time = time.time()

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.closedlooppartners.com/the-center/accelerating-the-circular-fashion-economy/")

screen_width = driver.execute_script("return window.screen.width;")
screen_height = driver.execute_script("return window.screen.height;")

new_width = int(screen_width / 2)
new_height = screen_height
new_position_x = 0
new_position_y = 0

driver.set_window_size(new_width, new_height)
driver.set_window_position(new_position_x, new_position_y)
time.sleep(2)

scroll_pos = 3600
scroll_increment = 900

for i in range(1):
    driver.execute_script(f"window,scrollTo(0, {scroll_pos});")
    show_more = driver.find_element("xpath", "//a[contains(@class, 'btn btn-outline-light btn-more')]")
    show_more.click()
    time.sleep(2)
    scroll_pos += scroll_increment

info_links = driver.find_elements("xpath", "//a[contains(@data-type, 'portfolio')]")
data = []
num_popups = 0

for link in info_links:
    link.click()
    time.sleep(5)

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    results = soup.find_all('div', class_='modal-body')
    for result in results:
        name_element = result.find('h2')
        name = name_element.text if name_element else ''

        web_element = result.find('a', class_='btn btn-outline-light btn-link')
        web = web_element['href'] if web_element else ''

        data.append([name, web])
        print(f'Scraped {name}')

        time.sleep(5)

    close_popup = driver.find_element(By.XPATH, '/html/body/div[5]/div/div[1]')
    close_popup.click()

    time.sleep(2)

df = pd.DataFrame(data)
df.to_csv('closedaccel.csv', index=False)

time.sleep(2)
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
driver.quit()


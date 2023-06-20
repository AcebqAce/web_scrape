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

info_links = driver.find_elements("xpath", "//a[contains(@class, 'vc-search-card-name')]")
data = []

for link in info_links:
    link_url = link.get_attribute("href")
    driver.execute_script("window.open('" + link_url + "', '_blank');")
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(5)

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    results = soup.find_all('main', class_='content-fluid')
    for result in results:
        name_element = result.find('h1', class_='f3 f1-ns mv1')
        name = name_element.text if name_element else ''

        web_element = result.find('a', class_='iconlink')
        web = web_element['href'] if web_element else ''

        linkedin_element = web_element.find_next_sibling('a', class_='iconlink')
        linkedin = linkedin_element['href'] if linkedin_element else ''

        data.append([name, web, linkedin])
        print(f'Scraped {name}')

        time.sleep(5)

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)

df = pd.DataFrame(data)
df.to_csv('signalnfxtoperprop.csv', index=False)

time.sleep(2)
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
driver.quit()


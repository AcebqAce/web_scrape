import time
import pandas as pd
from bs4 import BeautifulSoup

with open('downloaded-html/example.html') as file:

    # Parse the HTML content of the page
    soup = BeautifulSoup(file, 'html.parser')

# Find all elements with the specified attribute
results = soup.find_all('span', class_='_2PHJq public-DraftStyleDefault-ltr')

# Column names for the CSV file
columns = ['Name', 'Describe', 'Website']

# List to store the scraped data
data = []

# Start the timer
start_time = time.time()

# Loop through each result and extract the data
for i, result in enumerate(results):
    
    name_elements = result.find('h2')
    name = name_elements.text if name_elements else ''

    describe_elements = result.find('p')
    describe = describe_elements.text if name_elements else ''

    website_elements = soup.find_all('a', href=True)
    website = website_elements['href'] if website_elements else ''

    # Add the data to the list
    data.append([name, describe, website])

    # Print while scraping
    print('\n' f'\rScraping data from downloaded-html... {i+1}/{len(results)}', end='')

# Create a Pandas DataFrame from the list of data
df = pd.DataFrame(data, columns=columns)

# Replace empty space string with ''
df = df.replace(r'^\s*$', '', regex=True)

# Write the DataFrame to a CSV file
df.to_csv('scraped-csv/example.csv', index=False)

# End the timer
end_time = time.time()

# Calculate the elapased time
elapsed_time = end_time - start_time

# Print the elapsed time
print('\n' f'Scraping completed in {elapsed_time:.2f} seconds')
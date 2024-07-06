from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# Set up Chrome WebDriver using Service
chrome_driver_path = '/usr/bin/chromedriver'  # Replace with your actual path to chromedriver

# Create a Chrome service object
chrome_service = Service(chrome_driver_path)

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Optional: Run in headless mode

# Create a WebDriver instance
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Open the OPEC webpage
url = 'https://www.opec.org/opec_web/en/data_graphs/40.htm'
driver.get(url)

# Use explicit wait for the desired element to be clickable
try:
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'option4'))
    )
    element.click()
except Exception as e:
    print(f"Error clicking element: {e}")

time.sleep(2)  # Wait for the selection to update (adjust as needed)

# Extract data from the graph (example: get the data points)
data_points = []
try:
    for item in driver.find_elements(By.CSS_SELECTOR, '.highcharts-series-0 > rect'):
        data_points.append(item.get_attribute('aria-label'))
except Exception as e:
    print(f"Error extracting data points: {e}")

# Process the data points as needed (parse, clean, convert to DataFrame)
# Example: Convert data points to DataFrame
df_opec_data = pd.DataFrame(data_points, columns=['Data'])

# Save the extracted data to CSV
df_opec_data.to_csv('opec_data_from_graph.csv', index=False)

# Close the webdriver
driver.quit()

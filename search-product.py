# test script for search-product
from selenium import webdriver
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the local file
driver.get("enter the path")

# Find the search input field and enter a product name to search for
search_input = driver.find_element("id", "search_input")
search_input.send_keys("sdfghj")

# Find the search button and click it
search_button = driver.find_element("id", "search_button")
search_button.click()

# Wait for the search process to complete
time.sleep(5)

# Check if the search input field is empty
if search_input.get_attribute("value") == "":
    print("Product not found, empty field")
else:
    print("Product found")

# Close the browser
driver.quit()

# test script for checkout
from selenium import webdriver
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the local file
driver.get("file:///C:/Users/Aakarsh Roy/Pictures/selenium/test_page.html")

# Find the address, payment mode, and amount fields and enter values
address_field = driver.find_element("id", "address")
address_field.send_keys("mumbai 400101")

payment_mode_field = driver.find_element("id", "payment_mode")
payment_mode_field.send_keys("Debit Card")

amount_field = driver.find_element("id", "amount")
amount_field.send_keys("700")

# Find the checkout button and click it
checkout_button = driver.find_element("id", "checkout_button")
checkout_button.click()

# Wait for the checkout process to complete
time.sleep(3)

# Check if any of the fields are empty
if address_field.get_attribute("value") == "" or payment_mode_field.get_attribute("value") == "" or amount_field.get_attribute("value") == "":
    print("Checkout failed. One or more fields are empty.")
else:
    print("Checkout Successful!")
# Close the browser
driver.quit()

# test script for add-product
from selenium import webdriver
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the local file
driver.get("enter the path")

# Find the product name field and enter a value
product_name_field = driver.find_element("id", "product_name")
product_name_field.send_keys("apple")

# Find the add to cart button and click it
add_to_cart_button = driver.find_element("id", "add_to_cart_button")
add_to_cart_button.click()

# Wait for the add to cart process to complete
time.sleep(4)

# Check if the product was added to the cart
if product_name_field.get_attribute("value") == "":
    print("Failed to add product to cart. Product name field is empty.")
elif "Product Name" in driver.page_source:
    print("Product successfully added to cart")

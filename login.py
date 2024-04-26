# test script for login
from selenium import webdriver
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the local file
driver.get("enter the path")

# Find the username field and enter a value
username_field = driver.find_element("id", "username")
username_field.send_keys("zepto_user77")

# Find the password field and enter the same value as username
password_field = driver.find_element("id", "password")
password_field.send_keys("zepto_user77")  # Using the same value as username for simplicity

# Find the login button and click it
login_button = driver.find_element("id", "login_button")
login_button.click()

# Wait for the login process to complete
time.sleep(4)

# Check if the username and password are not empty and match
if username_field.get_attribute("value") != "" and username_field.get_attribute("value") == password_field.get_attribute("value"):
    print("Login successful")
elif username_field.get_attribute("value") == "" and password_field.get_attribute("value") == "":
    print("No credentials entered")
else:
    print("Invalid credentials!")

# Close the browser
driver.quit()

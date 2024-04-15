# test script for logout
from selenium import webdriver
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the local file
driver.get("file:///C:/Users/Aakarsh Roy/Pictures/selenium/test_page.html")

# Find the logout button and click it
logout_button = driver.find_element("id", "logout_button")
logout_button.click()

# Wait for the logout process to complete (you might need to adjust the wait time)
time.sleep(3)

try:
    logout_button = driver.find_element("id", "logout_button")
    print("Logout successful")
except:
    pass
# Close the browser
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Define BrowserStack desired capabilities
bs_capabilities = {
    "browser": "Chrome",
    "browser_version": "120.0",
    "os": "Windows",
    "os_version": "10",
    "name": "Test on Flipkart with Samsung Galaxy S10 search",
    "browserstack.use_w3c": True  # BrowserStack specific capability
}

# Authenticate with BrowserStack
bs_username = "kunjandutiya_RQwaeI"
bs_access_key = "rTb4ys4FZqsCK2trMi6E"

# Initialize Chrome options
chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")  # Example Chrome option, add more as needed

# Add BrowserStack capabilities directly to Chrome options
for key, value in bs_capabilities.items():
    chrome_options.add_experimental_option("w3c", {"desiredCapabilities": {key: value}})

# Initialize WebDriver with Chrome options
driver = webdriver.Chrome(options=chrome_options)

# Navigate to flipkart.com
driver.get("https://www.flipkart.com/")

# Perform search for Samsung Galaxy S10
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Samsung Galaxy S10" + Keys.RETURN)

# Click on Mobiles category
mobiles_category = driver.find_element(By.LINK_TEXT, "Mobiles")
mobiles_category.click()

# Apply filters
time.sleep(2)  # Wait for page to load

# Wait for the Samsung checkbox to be clickable
wait = WebDriverWait(driver, 5)
samsung_filter_checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label.tJjCVx._3DvUAf")))

# Scroll to the Samsung checkbox
driver.execute_script("arguments[0].scrollIntoView(true);", samsung_filter_checkbox)

# Click the Samsung checkbox using JavaScript
driver.execute_script("arguments[0].click();", samsung_filter_checkbox)

# Wait for filter to be applied
time.sleep(5)

# Wait for the "Select Flipkart assured" checkbox to be clickable
flipkart_assured_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[contains(@src, 'fa_62673a.png')]")))

# Scroll to the "Select Flipkart assured" checkbox
driver.execute_script("arguments[0].scrollIntoView(true);", flipkart_assured_checkbox)

# Click the "Select Flipkart assured" checkbox using JavaScript
driver.execute_script("arguments[0].click();", flipkart_assured_checkbox)

# Wait for filter to be applied
time.sleep(5)

# Click on the sorting dropdown to expand it
sorting_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Price -- High to Low')]")))
sorting_dropdown.click()

# Wait for the sorting to be applied
time.sleep(5)

# Read the set of results that show up on page 1
product_list = []

# Retrieve product details
products = driver.find_elements(By.XPATH, "//div[@data-id]")

for product in products:
    product_name_element = product.find_element(By.XPATH, ".//div[@class='KzDlHZ']")
    product_name = product_name_element.text

    product_link_element = product.find_element(By.XPATH, ".//a[@class='CGtC98']")
    product_link = product_link_element.get_attribute("href")

    product_price_element = product.find_element(By.XPATH, ".//div[@class='Nx9bqj _4b5DiR']")
    product_price = product_price_element.text

    product_list.append({
        "Product Name": product_name,
        "Display Price": product_price,
        "Link to Product Details Page": product_link
    })

# Close the browser window
driver.quit()

# Print the list of products on terminal
# for product in product_list:
#     print(product)

print("Process completed successfully.")

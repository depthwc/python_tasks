from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://www.demoblaze.com/")

# Click on Laptops category
laptops_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Laptops")))
laptops_link.click()
time.sleep(2)  # wait for laptops to load

laptops_data = []

# Scrape laptops on current page
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#tbodyid .col-lg-4.col-md-6.mb-4")))
cards = driver.find_elements(By.CSS_SELECTOR, "#tbodyid .col-lg-4.col-md-6.mb-4")

for card in cards:
    name = card.find_element(By.CSS_SELECTOR, ".card-title a").text.strip()
    price = card.find_element(By.CSS_SELECTOR, ".card-block h5").text.strip()
    
    detail_link = card.find_element(By.CSS_SELECTOR, ".card-title a").get_attribute("href")
    
    # Open detail link in new tab
    driver.execute_script("window.open(arguments[0]);", detail_link)
    driver.switch_to.window(driver.window_handles[1])

    try:
        desc_elem = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#more-information p")))
        description = desc_elem.text.strip()
    except:
        description = "No description available"

    laptops_data.append({
        "name": name,
        "price": price,
        "description": description
    })

    # Close detail tab and switch back
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

# Try to click Next button
try:
    next_button = driver.find_element(By.ID, "next2")
    if "disabled" not in next_button.get_attribute("class"):
        next_button.click()
        time.sleep(2)
        
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#tbodyid .col-lg-4.col-md-6.mb-4")))
        cards = driver.find_elements(By.CSS_SELECTOR, "#tbodyid .col-lg-4.col-md-6.mb-4")

        for card in cards:
            name = card.find_element(By.CSS_SELECTOR, ".card-title a").text.strip()
            price = card.find_element(By.CSS_SELECTOR, ".card-block h5").text.strip()

            detail_link = card.find_element(By.CSS_SELECTOR, ".card-title a").get_attribute("href")

            driver.execute_script("window.open(arguments[0]);", detail_link)
            driver.switch_to.window(driver.window_handles[1])

            try:
                desc_elem = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#more-information p")))
                description = desc_elem.text.strip()
            except:
                description = "No description available"

            laptops_data.append({
                "name": name,
                "price": price,
                "description": description
            })

            driver.close()
            driver.switch_to.window(driver.window_handles[0])
except Exception as e:
    print("No next page or error:", e)

driver.quit()

# Save to JSON
with open("laptops.json", "w", encoding="utf-8") as f:
    json.dump(laptops_data, f, ensure_ascii=False, indent=4)

print(f"Scraped {len(laptops_data)} laptops saved to laptops.json")

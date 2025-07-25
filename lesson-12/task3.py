import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("--headless")


driver = webdriver.Chrome(options=options)
driver.get("https://www.demoblaze.com/")

time.sleep(2)
laptops_button = driver.find_element(By.LINK_TEXT, "Laptops")
laptops_button.click()

time.sleep(2)

laptops = []


for _ in range(2): 
    time.sleep(2)
    items = driver.find_elements(By.CLASS_NAME, "col-lg-4")

    for item in items:
        name = item.find_element(By.TAG_NAME, "a").text
        price = item.find_element(By.CLASS_NAME, "price-container").text
        description = item.find_element(By.TAG_NAME, "p").text
        laptops.append({
            "name": name,
            "price": price.replace("Price: ", ""),
            "description": description
        })


    try:
        next_button = driver.find_element(By.ID, "next2")
        next_button.click()
    except:
        break


with open("laptops.json", "w", encoding="utf-8") as f:
    json.dump(laptops, f, indent=4, ensure_ascii=False)

print("✅ Done! Laptops saved to laptops.json")

driver.quit()

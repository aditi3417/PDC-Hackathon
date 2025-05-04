from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup browser
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Optional: comment this line to see the browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Load level 3 page
url = "https://hertie-scraping-website.vercel.app/level3"
driver.get(url)

# Click known buttons
for btn_id in ["flag-55", "flag-57", "flag-59"]:
    try:
        btn = driver.find_element(By.ID, btn_id)
        btn.click()
        time.sleep(2)  # allow any JS-rendered content to appear
    except Exception as e:
        print(f"Error clicking {btn_id}: {e}")

# 1. Extract flags visible in rendered text
visible_text = driver.find_element(By.TAG_NAME, "body").text

flags_dict = {}

# flag-54, 56, 58, 60 appear in rendered text
for i in [54, 56, 58, 60]:
    flag = f"flag-{i}"
    if flag in visible_text:
        flags_dict[flag] = flag

# 2. flag-55, 57, 59 are button IDs — check their presence
for i in [55, 57, 59]:
    try:
        if driver.find_element(By.ID, f"flag-{i}"):
            flags_dict[f"flag-{i}"] = f"flag-{i}"
    except:
        pass  # ignore if not found

# Show final result
print("Found flags:", flags_dict)

driver.quit()

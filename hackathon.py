import requests
from bs4 import BeautifulSoup

# Load the page
url = "https://hertie-scraping-website.vercel.app/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

flags_dict = {}

# 1. Flags from <p class="text-base">
for p in soup.find_all("p", class_="text-base"):
    text = p.text.strip()
    if text.startswith("flag-"):
        flags_dict[text] = text

# 2. Flags 8 and 9 by ID
for i in [8, 9]:
    if soup.find(attrs={"id": f"flag-{i}"}):
        flags_dict[f"flag-{i}"] = f"flag-{i}"

# 3. Even flags 10 to 40 by class
for i in range(10, 41, 2):
    class_name = f"flag-{i}"
    flag_element = soup.find("div", class_=lambda x: x and class_name in x.split())
    if flag_element:
        flags_dict[class_name] = class_name

# 4. Odd flags 11 to 39 by ID
for i in range(11, 40, 2):
    flag_id = f"flag-{i}"
    if soup.find("div", id=flag_id):
        flags_dict[flag_id] = flag_id


print(flags_dict)


import requests
from bs4 import BeautifulSoup

# Load level 2 page
url = "https://hertie-scraping-website.vercel.app/level2"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Dictionary to collect flags
flags_dict = {}

#flag 41
flag_41_element = soup.find("div", class_="text-center my-4")
if flag_41_element and "flag-41" in flag_41_element.text:
    flags_dict["flag-41"] = "flag-41"

# flag-42 from any <div> that contains it in text
flag_42_element = soup.find("div", string=lambda text: text and "flag-42" in text)
if flag_42_element:
    flags_dict["flag-42"] = "flag-42"
else:
    print("flag-42 not found")

# flag-43 from <p id="flag-43"> and manually check for flag-44 and flag-45
p_43 = soup.find("p", id="flag-43")
if p_43:
    flags_dict["flag-43"] = "flag-43"
    text_43 = p_43.text
    if "flag-44" in text_43:
        flags_dict["flag-44"] = "flag-44"
    if "flag-45" in text_43:
        flags_dict["flag-45"] = "flag-45"
else:
    print("flag-43 not found")

# flag-46 contains <p class="flag-47">
div_46 = soup.find("div", id="flag-46")
if div_46:
    flags_dict["flag-46"] = "flag-46"
    p_47 = div_46.find("p", class_="flag-47")
    if p_47:
        flags_dict["flag-47"] = "flag-47"
        text_47 = p_47.text
        if "flag-48" in text_47:
            flags_dict["flag-48"] = "flag-48"
        if "flag-49" in text_47:
            flags_dict["flag-49"] = "flag-49"
    else:
        print("flag-47 not found")
else:
    print("flag-46 not found")

# flag-50 contains <p id="flag-51"> which may contain flag-52 and flag-53
div_50 = soup.find("div", class_="flag-50")
if div_50:
    flags_dict["flag-50"] = "flag-50"
    p_51 = div_50.find("p", id="flag-51")
    if p_51:
        flags_dict["flag-51"] = "flag-51"
        text_51 = p_51.text
        if "flag-52" in text_51:
            flags_dict["flag-52"] = "flag-52"
        if "flag-53" in text_51:
            flags_dict["flag-53"] = "flag-53"
    else:
        print("flag-51 not found")
else:
    print("flag-50 not found")

# Print final flags dictionary
print(flags_dict)

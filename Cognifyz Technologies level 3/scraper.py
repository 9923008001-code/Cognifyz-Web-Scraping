import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Website URL
url = "https://quotes.toscrape.com"

# Step 2: Send request
response = requests.get(url)

# Step 3: Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Find quote blocks
quote_blocks = soup.find_all("div", class_="quote")

# Step 5: Create CSV file
with open("quotes.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])  # Header

    for quote in quote_blocks:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        writer.writerow([text, author])

print("✅ Quotes saved successfully to quotes.csv")

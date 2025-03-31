import requests
import os
import pandas as pd
from bs4 import BeautifulSoup

# Wikipedia page URL to scrape character names and links
url = "https://en.wikipedia.org/wiki/List_of_Adventure_Time_characters"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Store characters and links
characters = []
links = []

# Extract character names
for item in soup.select(".mw-heading3"):
    characters.append(item.text)

# Extract character links
for linkList in soup.select(".hatnote a"):
    link_href = linkList.get("href")
    if link_href.startswith("/wiki/"):  # Ensure it's a valid Wikipedia link
        full_url = "https://en.wikipedia.org" + link_href
        links.append(full_url)

# Ensure both lists are the same length
max_length = max(len(characters), len(links))
characters += [""] * (max_length - len(characters))
links += [""] * (max_length - len(links))

# Create DataFrame for character names and links
df = pd.DataFrame({"Character": characters, "Character_Link": links})

# Create a folder to store images
os.makedirs("character_images", exist_ok=True)

# Function to download and save the infobox image for each character
def download_infobox_image(url, character_name):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find the first image in the infobox
        img_tag = soup.select_one(".infobox img")
        
        if img_tag:
            img_url = "https:" + img_tag["src"]
            # Get the image content
            img_data = requests.get(img_url).content
            
            # Save the image to the 'character_images' folder
            img_filename = f"character_images/{character_name.replace(' ', '_')}.jpg"
            with open(img_filename, "wb") as img_file:
                img_file.write(img_data)
                
            return img_filename  # Return the saved file path
    except Exception as e:
        print(f"Failed to fetch image for {url}: {e}")
    
    return None

# Download images and store the filenames
df["Image_Path"] = df.apply(lambda row: download_infobox_image(row["Character_Link"], row["Character"]) if row["Character_Link"] else None, axis=1)

# Save the DataFrame
df.to_csv("adventure_time_characters_with_images.csv", index=False)
print(df)

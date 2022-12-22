# this is for to scrap images of easydrawingguides.com
import requests
import os
from bs4 import BeautifulSoup

# Replace `url` with the URL of the webpage that you want to download images from
url = "https://easydrawingguides.com/how-to-draw-a-crown"

# Set the directory path where you want to save the images
directory = "images/"

# Send an HTTP request to the URL and store the response
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, "html.parser")

# Find all `figure` tags on the page
figures = soup.find_all("div")

# Iterate through each `figure` tag
for i, figure in enumerate(figures):
  # Find the `img` tag within the `figure` tag
  img_tag = figure.find("img")

  # If there is an `img` tag, get the URL of the image
  if img_tag:
    img_url = img_tag["src"]
    # Download the image and save it to a file in the specified directory
    response = requests.get(img_url)
    file_path = os.path.join(directory, f"image_{i}.jpg")
    open(file_path, "wb").write(response.content)

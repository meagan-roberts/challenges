from bs4 import BeautifulSoup
import requests

import os
from dotenv import load_dotenv

load_dotenv() 
URL = os.getenv("SECRET_MESSAGE_URL")
print(URL)

def get_data(url):
     # Get the content of the google doc url
    response = requests.get(url)

    # Parse the response content using the beautifulSoup library
    soup = BeautifulSoup(response.text, "html.parser")
    data = soup.get_text("\n").strip().splitlines()

    # Remove text from coordinates
    coordinates = []
    right_data = False
    for d in data:
        if right_data == True:
            coordinates.append(d)
        else:
            if d == "y-coordinate":
                right_data = True

    return coordinates

def secret_message():
    # function call get_data
    coordinates = get_data(URL) 

    # Seperate coordinates into x, y, and img
    x_list = []
    y_list = []
    char_list = []

    for index, item in enumerate(coordinates):
        if index % 3 == 0:
            x_list.append(int(item.strip()))
        if index % 3 == 1:
            char_list.append(item)
        if index % 3 == 2:
            y_list.append(int(item.strip()))

    # Set the max x and y grid points
    max_x = max(x_list) + 1
    max_y = max(y_list) + 1

    grid = [[' ' for _ in range(max_x)] for _ in range(max_y)]

    # for each character set the x and y grid points
    for i, char in enumerate(char_list):
        grid[y_list[i]][x_list[i]] = char
    
    
    for y in range(max_y):
        print(''.join(grid[y]))

# main function call
secret_message()
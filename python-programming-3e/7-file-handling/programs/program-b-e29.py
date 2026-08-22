# EXAMPLE 7.29 : Write a program to download web pages through the web and write in a file.

import requests
from pathlib import Path

file_path = Path(__file__).parent / "example-files" / "google-file.html"

url = 'https://www.google.com/'
r = requests.get(url)

with open(file_path, 'wb') as file:
    file.write(r.content)
print(f'Content from "{url}" written in "{file_path.name}"')

import xml.etree.ElementTree as ET
from pathlib import Path

book = ET.Element("book")

name = ET.SubElement(book, "name")
name.text = "Python Programming Using Problem Solving Approach"

edition = ET.SubElement(book, "edition")
edition.text = "3"

author = ET.SubElement(book, "author")
author.text = "Reema Thareja"

publisher = ET.SubElement(book, "publisher")
publisher.text = "Oxford University Press"

price = ET.SubElement(book, "price")
price.text = "560.00"

book.set("chapters", "12")

tree = ET.ElementTree(book)
xml_file_path = Path(__file__).parent / "files" / "book.xml"
tree.write(xml_file_path)

print(f"XML file created. \"{xml_file_path}\"")

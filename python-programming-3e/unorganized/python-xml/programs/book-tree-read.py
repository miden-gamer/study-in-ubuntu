import xml.etree.ElementTree as ET
from pathlib import Path

xml_file_path = Path(__file__).parent / "files" / "book.xml"

tree = ET.parse(xml_file_path)
root = tree.getroot()

print(f"Root Tag = <{root.tag}>")

name = root.find("name")
print(f"Book name = \"{name.text}\"")

# Example 7.27 : To show use of os.path.exists(path) and os.path.isfile(path) and os.path.isdir(path) methods

import os

file_path = __file__
directory = os.path.dirname(__file__)

print(f"os.path.exists(\"{file_path}\") = {os.path.exists(file_path)}")
print(f"os.path.isfile(\"{file_path}\") = {os.path.isfile(file_path)}")
print(f"os.path.isdir(\"{directory}\") = {os.path.isdir(directory)}")
print(f"os.path.isfile(\"{directory}\") = {os.path.isfile(directory)}")
print(f"os.path.isdir(\"{file_path}\") = {os.path.isdir(file_path)}")
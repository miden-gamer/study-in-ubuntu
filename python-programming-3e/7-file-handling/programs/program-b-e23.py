# EXAMPLE 7.23 : Program to demonstrate use of os.path.relpath(path, start) method

import os

cwd = os.getcwd()
current_file_abspath = __file__
current_file_relpath = os.path.relpath(current_file_abspath, cwd)

print("CWD =", cwd)
print("Absolute path of this program file =", current_file_abspath)
print("Path of this program file relative to CWD =", current_file_relpath)
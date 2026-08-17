# PROGRAM 7.8 : Write a program to check if flash drive is connected to your 
# computer

import os
print("os.path.exists(\"G:\\\") =", os.path.exists("G:\\"))
# Works only if:
# USB Drive gets drive letter: G:
# Program is being run on Windows system.
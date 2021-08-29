# File xu_ly_tap_tin
import xu_ly_tap_tin as tv
import os
from os import path


def read_file(filename):
    dd = os.getcwd()+"\\bai_11\\"+filename
    if path.exists(dd):
        f = open(dd, "r", encoding="utf-8")
        content = f.read()
        f.close()
        return content
    else:
        return "no file found"


# Bai 11.1
f_name = input("File name:")
content = tv.read_file(f_name)
print("File content: \n")
print(content)

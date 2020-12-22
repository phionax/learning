import os

path = r'F:\files\test\1'
tr = '\\'

def  ren():
    os.rename(path + tr + file, path + tr + file[2:])

filelist = os.listdir(path)
for file in filelist:
    if file[:2] == "s_":
        ren()

from sys import path
from xml.dom import minidom
import os, shutil, glob
import requests
import gzip

xmls = os.listdir(r"E:\moaaz\elemnt14\New folder (11)")
f = open('E:\\moaaz\\elemnt14\\New folder (11)\\data11.txt', 'a')
for i in range(len(xmls)):
    print(xmls[i])
    mydoc = minidom.parse("E:\\moaaz\\elemnt14\\New folder (11)\\"+xmls[i])
    items = mydoc.getElementsByTagName('xhtml:link')
    for iter2 in range(len(items)):
        if "https://sg.element14.com" in items[iter2].attributes['href'].value+"\n":
            print(iter2+1, "=", items[iter2].attributes['href'].value+"\n")
            f.writelines(items[iter2].attributes['href'].value+"\n")
f.close()

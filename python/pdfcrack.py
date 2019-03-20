#! /usr/bin/python
import os

#os.system("pwd")
userfile = input("Input the full name of the file and extension: ")
type(userfile)
#print(userfile)
#crackPath = os.system("locate " + userfile)
#print(crackPath)
os.system("pdfcrack -f " + userfile + " -w /usr/share/wordlists/rockyou.txt")
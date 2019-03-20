#! /usr/bin/python
import os
import subprocess

################################################################
#HOW TO RUN IN KALI LINUX
# Make sure to change the directory (cd) to the directory holding the pdfcrack.py file
#Enter "python3 pdfcrack.py" to run the program (python3 filename.extension)
#################################################################


#HAVE PROGRAM DECIDE WHICH CRACK IT IS DOING



#os.system("pwd") #test that this command works
userfile = input("Input the full name of the file: ")  #prompts user for inpupt
type(userfile)
#print(userfile) #test to see user input was saved into variable
userfile = userfile + ".pdf" #adds .pdf to the end of the user input
#print(userfile) #test to make sure .pdf was added
#os.system("pdfcrack -f " + userfile + " -w /usr/share/wordlists/rockyou.txt") #original command
#proc=subprocess.Popen('readlink -f ' + userfile, shell=True, stdout=subprocess.PIPE, ) #original saving output
proc=subprocess.Popen('find ~ -name ' + userfile, shell=True, stdout=subprocess.PIPE, ) #does subprocess, first quotation is the command and subprocess is saved with stdout
output=proc.communicate()[0] #saves the terminal output
#print(output) #locate file
output2 = output.decode("utf-8") #converts the terminal output which is in bytes into a string
output2 = output2.rstrip() #strips the \n from the end of the string
#print(output2) #confirm that the path is saved correctly
#userfilePATH = output2 + " " + userfile
#print(userfilePATH)
os.system("pdfcrack -f " + output2 + " -w /usr/share/wordlists/rockyou.txt") #command that cracks the password, calls on pdfcrack
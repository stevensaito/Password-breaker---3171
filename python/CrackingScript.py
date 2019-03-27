#! /usr/bin/python
import os
import subprocess

#PROGRAM NEEDS USER TO INDICATE WHAT FILE THEY ARE CRACKING ATM
#FUTURE IS PROGRAM CAN DECIDE FROM BUTTON THEY CLICK OR DRAG AND DROP

################################################################
#HOW TO RUN IN KALI LINUX
# Make sure to change the directory (cd) to the directory holding the pdfcrack.py file
#Enter "python3 pdfcrack.py" to run the program (python3 filename.extension)
#################################################################


while True:
    typeoffile = input("What type of file are you cracking? (pdf or zip): ").lower()  #prompts user for input, converts the input into lowercase with .lower()
    if typeoffile == "pdf":
   	 #print(typeoffile) #confirm input
   	 break
    elif typeoffile == "zip":
   	 #print(typeoffile) #confirm input
   	 break
    else:
   	 print("Please select a valid option")
   	 continue

#os.system("pwd") #test that this command works
#os.system inputs command, ("pwd") is the command
userfile = input("Input the full name of the file: ")  #prompts user for input
type(userfile)
#print(userfile) #test to see user input was saved into variable

if typeoffile == "pdf":
    userfile = userfile + ".pdf" #adds .pdf to the end of the user input
elif typeoffile == "zip":
    userfile = userfile + ".zip" #adds .pdf to the end of the user input


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

if typeoffile == "pdf":
    os.system("pdfcrack -f " + output2 + " -w /usr/share/wordlists/rockyou.txt")#command that cracks the password, calls on pdfcrack
elif typeoffile == "zip":
    os.system("fcrackzip -u -D -p /usr/share/wordlists/rockyou.txt " + output2)#command that cracks the password, calls on fccrackzip




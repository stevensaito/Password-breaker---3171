#! /usr/bin/python
from tkinter import *
import tkinter as tk
import os
import subprocess
from tkinter import filedialog

#prints text field value into terminal
#def show_entry_fields():
	#print("First Name: %s\n" % (e1.get()))
	#print (master.filename)

def crack():
	if r"root/" not in e1.get():
		#print("potato") #Test if this if statement is used
		proc=subprocess.Popen('find ~ -name ' + e1.get(), shell=True, stdout=subprocess.PIPE, ) #does subprocess, first quotation is the command and subprocess is saved with stdout
		output=proc.communicate()[0] #saves the terminal output
		#print(output) #locate file
		output = output.decode("utf-8") #converts the terminal output which is in bytes into a string
		master.filename = output.rstrip()
		#print(master.filename) #see if correct path is found

#THIS IS THE CRACKING COMMAND
	if (master.filename).endswith('.pdf'):
		os.system("pdfcrack -f " + master.filename + " -w /usr/share/wordlists/rockyou.txt")#command that cracks the password, calls on pdfcrack
	elif (master.filename).endswith('.zip'):
		print("Beginning crack")
		os.system("fcrackzip -u -D -p /usr/share/wordlists/rockyou.txt " + master.filename)#command that cracks the password, calls on fccrackzip
	else:
		print("You did not select an appropiate file")
########THIS IS THE CRACKING COMMAND

def searchfile():
	master.filename =  filedialog.askopenfilename(initialdir = "/root",title = "Select file",filetypes = (("all files","*.zip AND *.pdf"),("pdf files","*.pdf"),("zip files","*.zip"))) #(("pdf files","*.pdf"),("all files","*.*")))
	#print (master.filename)
	e1.insert(0, master.filename) #inserts found file into entry field
	

master = Tk() #name of the window
Label(master, text="File Name: ").grid(row=0)

e1 = Entry(master)
#e2 = Entry(master)

e1.grid(row=0, column=1)
#e2.grid(row=0, column=2)

Button(master, text='Quit', command=master.quit).grid(row=4, column=0, sticky=W, pady=4)
Button(master, text='Search for File', command=searchfile).grid(row=4, column=1, sticky=W, pady=4)
Button(master, text='Crack Password', command=crack).grid(row=4, column=2, sticky=W, pady=4)

mainloop( )


#https://www.tecmint.com/create-password-protected-zip-file-in-linux/
#https://www.python-course.eu/tkinter_entry_widgets.php
#https://www.python-course.eu/tkinter_radiobuttons.php
#https://pythonspot.com/tk-file-dialogs/
#https://stackoverflow.com/questions/43759769/how-to-test-if-symbol-backslash-is-in-a-string
#https://stackoverflow.com/questions/5899497/checking-file-extension
from tkinter import *
fields = 'Last Name', 'First Name', 'Job', 'Country'
#import webbrowser    #import for internet browsers
import os   #import for command promt

#url='www.google.ca'   #url for browser
#chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'    #path for program

def commandprompt(): os.system("start cmd")


def fetch(entries):
   for entry in entries:
      field = entry[0]
      text  = entry[1].get()
      print('%s: "%s"' % (field, text))

def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries


#def openSecond(second):
    #exec(open("secondWin.py").read())


if __name__ == '__main__':
   root = Tk()
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))
   b1 = Button(root, text='Show',
          command=(lambda e=ents: fetch(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='Quit', command=root.quit)
   b2.pack(side=LEFT, padx=5, pady=5)
   b3 = Button(root, text='Open File',
               #command=exec(open("secondWin.py").read()))
               #command=webbrowser.get(chrome_path).open(url))    #open google chrome
               command=(os.system("start cmd"))) #open command prompt
   b3.pack(side=RIGHT, padx=5, pady=5)
   root.mainloop()


   #https://www.python-course.eu/tkinter_buttons.php
   #https://www.python-course.eu/tkinter_entry_widgets.php
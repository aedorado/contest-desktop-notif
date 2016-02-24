from Tkinter import *
from threading import *
import tkMessageBox
import webbrowser

class App():

    w = 400
    h = 200
    bgColor = '#77216F'

    def __init__(self, contestlist):
        self.contestlist = contestlist

        self.root = Tk()
        self.root.overrideredirect(1)
        self.root.configure(background=self.bgColor)

        # get screen width and height
        ws = self.root.winfo_screenwidth()  # width of the screen
        hs = self.root.winfo_screenheight() # height of the screen

        # set the dimensions of the screen and where it is placed
        self.root.geometry('%dx%d+%d+%d' % (self.w, self.h, ws - self.w, 0))

        self.clist = Listbox(self.root)
        self.clist.configure(foreground='#FFF', background=self.bgColor)

        for i in range(len(contestlist)):
            print i
            self.clist.insert(END, contestlist[i]['Platform'] + '\n' + contestlist[i]['url'])
            pass

        self.clist.bind('<<ListboxSelect>>', self.bopen)
        self.clist.place(x=10, y=10, height=180, width=350)

        self.scrollbar = Scrollbar(self.clist)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.clist.yview)
        # self.label.pack(pady=20)

        self.bQuit = Button(self.root, text="X", command=self.closeSelf)
        self.bQuit.place(x=375, y=0, height=25, width=25)
        self.bQuit.configure(background = '#77216F')

        # self.root.after(7500, lambda: self.root.destroy())
        self.root.mainloop()

    def closeSelf(self):
        self.root.destroy()

    def bopen(self, event):
        i = self.clist.curselection()[0]
        webbrowser.open(self.contestlist[i]['url'])
        
        pass

# app = App('hello').root.mainloop()
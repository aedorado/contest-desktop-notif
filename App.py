from Tkinter import *
from threading import *
import tkFont
import webbrowser

class App():

    w = 400
    h = 450
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
        self.root.geometry('%dx%d+%d+%d' % (self.w, self.h, ws - self.w - 20, hs - self.h - 50))

        self.clist = Listbox(self.root)
        self.clist.configure(foreground='#FFF', background=self.bgColor)

        for i in range(len(contestlist)):
            self.clist.insert(END, str(i) + ') ' + contestlist[i]['Name'])
            self.clist.insert(END, contestlist[i]['Platform'] + ' ' + contestlist[i]['EndTime'])
            self.clist.insert(END, contestlist[i]['url'])
            self.clist.insert(END, '')
            pass

        # adding callback to listbox
        self.clist.bind('<<ListboxSelect>>', self.bopen)
        self.clist.place(x=10, y=10, height=430, width=350)

        self.scrollbar = Scrollbar(self.clist)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.clist.yview)

        # adding quit button
        self.bQuit = Button(self.root, text="X", command=self.closeSelf)
        self.bQuit.place(x=375, y=0, height=25, width=25)
        self.bQuit.configure(background = '#77216F')

        self.root.lift()
        self.root.call('wm', 'attributes', '.', '-topmost', True)   # so that window is always topmost
        self.root.mainloop()

    def closeSelf(self):
        self.root.destroy()

    def bopen(self, event):
        i = int(self.clist.curselection()[0]) / 4    # set of 4 lines coresspond to a single url
        webbrowser.open(self.contestlist[i]['url'])

# app = App('hello').root.mainloop()
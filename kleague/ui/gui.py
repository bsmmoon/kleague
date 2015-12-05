from tkinter import *

class GUI(Frame):
    def __init__(self):
        self.root = Tk()
        self.root.resizable(width=False, height=False)
        self.root.geometry('{}x{}'.format(str(480), str(480)))
        Frame.__init__(self, self.root)
        self.grid()
        self.root.title('Grid')

        rows = 10
        cols = 6

        for r in range(rows):
            self.root.rowconfigure(r, weight=1)    
        for c in range(cols):
            self.root.columnconfigure(c, weight=1)
            # Button(self.root, text="Button {0}".format(c)).grid(row=6,column=c,sticky=E+W)

        for r in range(rows):
            for c in range(cols):
                Label(self.root, text='(' + str(r) + ',' + str(c) +')',
                    borderwidth = 1).grid(row = r, column = c)

        self.MenuFrame = Frame(self.root, bg="red")
        self.MenuFrame.grid(row = 9, column = 0, rowspan = 1, columnspan = cols, sticky = W+E+N+S)
        for c in range(cols):
            self.MenuFrame.columnconfigure(c, weight=1)
        self.MenuFrame.rowconfigure(0, weight=1)
        
        self.HeaderFrame = Frame(self.root, bg="blue")
        self.HeaderFrame.grid(row = 0, column = 0, rowspan = 1, columnspan = cols, sticky = W+E+N+S)
        for c in range(cols):
            self.HeaderFrame.columnconfigure(c, weight=1)
        self.HeaderFrame.rowconfigure(0, weight=1)

        self.createMenu()

        self.transfercentreIsOpen = False

    def createMenu(self):
        Button(self.MenuFrame, text="Menu1", command=self.say_hi).grid(row=0,column=0,columnspan=2,sticky=E+W)
        Button(self.MenuFrame, text="Menu2", command=self.transfercentre).grid(row=0,column=2,columnspan=2,sticky=E+W)
        Button(self.MenuFrame, text="Menu3", command=self.transfercentre).grid(row=0,column=4,columnspan=2,sticky=E+W)

    def transfercentre(self):
        if self.transfercentreIsOpen:
            return

        self.search_player = Entry(self)
        self.search_player.pack(side='left')

        self.search_team = Entry(self)
        self.search_team.pack(side='left')

        self.root.after(2000, self.repeatTest)

        self.transfercentreIsOpen = True

    def say_hi(self):
        print("hi there, everyone!")

    def repeatTest(self):
        print(self.search_player.get() + ' to ' + self.search_team.get())
        self.root.after(2000, self.repeatTest)

    def run(self):
        self.mainloop()

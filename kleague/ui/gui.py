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

        menuFrame = Frame(self.root, bg="red")
        menuFrame.grid(row = rows-1, column = 0, rowspan = 1, columnspan = cols, sticky = W+E+N+S)
        for c in range(cols):
            menuFrame.columnconfigure(c, weight=1)
        menuFrame.rowconfigure(0, weight=1)
        
        headerFrame = Frame(self.root, bg="blue")
        headerFrame.grid(row = 0, column = 0, rowspan = 1, columnspan = cols, sticky = W+E+N+S)
        for c in range(cols):
            headerFrame.columnconfigure(c, weight=1)
        headerFrame.rowconfigure(0, weight=1)

        mainFrame = Frame(self.root)
        mainFrame.grid(row = 1, column = 0, rowspan = rows - 2, columnspan = cols, sticky = W+E+N+S)
        for r in range(rows):
            mainFrame.rowconfigure(r, weight=1)
        for c in range(cols):
            mainFrame.columnconfigure(c, weight=1)
        mainFrame.rowconfigure(0, weight=1)

        self.openedMenu = 0

        self.createMenu(menuFrame, mainFrame)
        self.updateHeader(headerFrame)

    def createMenu(self, menuFrame, mainFrame):
        Button(menuFrame, text="Menu1", command=self.say_hi).grid(row=0,column=0,columnspan=2,sticky=E+W)
        Button(menuFrame, text="Transfer Centre", command=self.transfercentre(mainFrame)).grid(row=0,column=2,columnspan=2,sticky=E+W)
        Button(menuFrame, text="Menu3", command=self.transfercentre(mainFrame)).grid(row=0,column=4,columnspan=2,sticky=E+W)

    def updateHeader(self, headerFrame):
        if self.openedMenu == 0:
            Label(headerFrame, text='0', borderwidth = 1).grid(row = 0, column = 0, columnspan = 6)
        elif self.openedMenu == 1:
            Label(headerFrame, text='Transfer Centre', borderwidth = 1).grid(row = 0, column = 0, columnspan = 6)
        elif self.openedMenu == 2:
            Label(headerFrame, text='2', borderwidth = 1).grid(row = 0, column = 0, columnspan = 6)

    def transfercentre(self, mainFrame):
        if self.openedMenu == 1:
            return
        else:
            self.openedMenu = 1

        self.labelFrame(mainFrame, 8, 6)

        Label(mainFrame, text='Player').grid(row=0, column=0, columnspan=3)
        search_player = Entry(mainFrame)
        search_player.grid(row=1, column=0, columnspan=3)

        Label(mainFrame, text='Team').grid(row=0, column=3, columnspan=3)
        search_team = Entry(mainFrame)
        search_team.grid(row=1, column=3, columnspan=3)
        
        # self.root.after(2000, self.repeatTest(search_player, search_team))


    def say_hi(self):
        print("hi there, everyone!")

    def repeatTest(self, search_player, search_team):
        if self.openedMenu != 1:
            return
        print(search_player.get() + ' to ' + search_team.get())
        self.root.after(2000, self.repeatTest(search_player, search_team))

    def run(self):
        self.mainloop()

    def labelFrame(self, frame, rows, cols):
        for r in range(rows):
            for c in range(cols):
                Label(frame, text='(' + str(r) + ',' + str(c) +')',
                    borderwidth = 1).grid(row = r, column = c)


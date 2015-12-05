from tkinter import *

class GUI(Frame):
    def __init__(self):
        self._root = Tk()
        self._root.resizable(width=False, height=False)
        self._root.geometry('{}x{}'.format(str(480), str(480)))
        Frame.__init__(self, self._root)
        self.grid()
        self._root.title('Grid')

        rows = 10
        cols = 6

        for r in range(rows):
            self._root.rowconfigure(r, weight=1)    
        for c in range(cols):
            self._root.columnconfigure(c, weight=1)

        self._openedMenu = 0

        self.menu = Menu(self, rows-1, 0, 1, cols)
        self.header = Header(self, 0, 0, 1, cols)

        mainFrame = Frame(self._root)
        mainFrame.grid(row = 1, column = 0, rowspan = rows - 2, columnspan = cols, sticky = W+E+N+S)
        for r in range(rows - 2):
            mainFrame.rowconfigure(r, weight=1)
        for c in range(cols):
            mainFrame.columnconfigure(c, weight=1)
        mainFrame.rowconfigure(0, weight=1)

        self.menu1(mainFrame)
        self.header.update()
        self.menu.update(mainFrame)

    @property
    def openedMenu(self):
        return self._openedMenu

    @property
    def root(self):
        return self._root

    def transfercentre(self, mainFrame):
        if self._openedMenu == 1:
            return
        self._openedMenu = 1
        self.header.update()

        self.labelFrame(mainFrame, 8, 6)

        Label(mainFrame, text='Player').grid(row=0, column=0, columnspan=3)
        search_player = Entry(mainFrame)
        search_player.grid(row=1, column=0, columnspan=3)

        Label(mainFrame, text='Team').grid(row=0, column=3, columnspan=3)
        search_team = Entry(mainFrame)
        search_team.grid(row=1, column=3, columnspan=3)
        
        self._root.after(2000, lambda: self.repeatTest(search_player, search_team))


    def menu1(self, mainFrame):
        print("hi there, everyone!")
        self._openedMenu = 0
        self.header.update()

    def menu3(self, mainFrame):
        print("hi there, everyone!")
        self._openedMenu = 2
        self.header.update()

    def repeatTest(self, search_player, search_team):
        if self._openedMenu != 1:
            return
        print(search_player.get() + ' to ' + search_team.get())
        self._root.after(2000, lambda: self.repeatTest(search_player, search_team))

    def run(self):
        self.mainloop()

    def labelFrame(self, frame, rows, cols):
        for r in range(rows):
            for c in range(cols):
                Label(frame, text='(' + str(r) + ',' + str(c) +')',
                    borderwidth = 1).grid(row = r, column = c)

class FrameTemplate():
    def __init__(self, gui, row, column, rowspan, columnspan):
        self.gui = gui
        self.row = row
        self.column = column
        self.rowspan = rowspan
        self.columnspan = columnspan

        self.clear()

    def clear(self):
        self._frame = Frame(self.gui.root, bg="blue")
        self._frame.grid(row = self.row, column = self.column, rowspan = self.rowspan, columnspan = self.columnspan, sticky = W+E+N+S)
        for r in range(self.rowspan):
            self._frame.columnconfigure(r, weight=1)
        for c in range(self.columnspan):
            self._frame.columnconfigure(c, weight=1)
        self._frame.rowconfigure(0, weight=1)

    @property
    def frame(self):
        return self._frame

class Header(FrameTemplate):
    def update(self):
        self.clear()
        print(self.gui.openedMenu)
        if self.gui.openedMenu == 0:
            Label(self._frame, text='0', borderwidth = 1).grid(row = 0, column = 0, columnspan = 6)
        elif self.gui.openedMenu == 1:
            Label(self._frame, text='Transfer Centre', borderwidth = 1).grid(row = 0, column = 0, columnspan = 6)
        elif self.gui.openedMenu == 2:
            Label(self._frame, text='2', borderwidth = 1).grid(row = 0, column = 0, columnspan = 6)

class Menu(FrameTemplate):
    def update(self, mainFrame):
        self.clear()
        Button(self._frame, text="Menu1", command=lambda: self.gui.menu1(mainFrame)).grid(row=0,column=0,columnspan=2,sticky=E+W)
        Button(self._frame, text="Transfer Centre", command=lambda: self.gui.transfercentre(mainFrame)).grid(row=0,column=2,columnspan=2,sticky=E+W)
        Button(self._frame, text="Menu3", command=lambda: self.gui.menu3(mainFrame)).grid(row=0,column=4,columnspan=2,sticky=E+W)

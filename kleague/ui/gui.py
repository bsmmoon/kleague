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
        self.labelFrame(self._root, rows, cols)
        inputString = input('Your command? ')

        self._openedMenu = 0

        self.menu = Menu(self, self._root, rows-1, 0, 1, cols, 'red')
        self.header = Header(self, self._root, 0, 0, 1, cols, 'blue')
        mainFrame = MainFrame(self, self._root, 1, 0, rows-2, cols)

        self.header.update()
        self.menu.update(mainFrame)

    @property
    def openedMenu(self):
        return self._openedMenu

    @openedMenu.setter
    def openedMenu(self, openedMenu):
        self._openedMenu = openedMenu

    @property
    def root(self):
        return self._root

    def run(self):
        self.mainloop()

    def labelFrame(self, frame, rows, cols):
        for r in range(rows):
            for c in range(cols):
                Label(frame, text='(' + str(r) + ',' + str(c) +')',
                    borderwidth = 1).grid(row = r, column = c)


class FrameTemplate():
    def __init__(self, gui, parent, row, column, rowspan, columnspan, bg=None):
        self.gui = gui
        self.parent = parent
        self.row = row
        self.column = column
        self.rowspan = rowspan
        self.columnspan = columnspan
        self.bg = bg

        self.reset()

    def reset(self):
        self._frame = Frame(self.parent, bg = self.bg)
        self._frame.grid(row = self.row, column = self.column,
            rowspan = self.rowspan, columnspan = self.columnspan,
            sticky = W+E+N+S)
        for r in range(self.rowspan):
            self._frame.rowconfigure(r, weight=1)
        for c in range(self.columnspan):
            self._frame.columnconfigure(c, weight=1)

    @property
    def frame(self):
        return self._frame


class Header(FrameTemplate):
    def update(self):
        self.reset()
        print(self.gui.openedMenu)
        if self.gui.openedMenu == 0:
            Label(self._frame, text='0', borderwidth = 1).grid(row = 0, column = 0, columnspan = 6)
        elif self.gui.openedMenu == 1:
            Label(self._frame, text='Transfer Centre', borderwidth = 1).grid(row = 0, column = 0, columnspan = 6)
        elif self.gui.openedMenu == 2:
            Label(self._frame, text='2', borderwidth = 1).grid(row = 0, column = 0, columnspan = 6)


class Menu(FrameTemplate):
    def update(self, mainFrame):
        self.reset()
        Button(self._frame, text="Menu1", command=
            lambda: mainFrame.menu1()).grid(
            row=0,column=0,columnspan=2,sticky=E+W)
        Button(self._frame, text="Transfer Centre", command=
            lambda: mainFrame.transfercentre()).grid(
            row=0,column=2,columnspan=2,sticky=E+W)
        Button(self._frame, text="Menu3", command=
            lambda: mainFrame.menu3()).grid(
            row=0,column=4,columnspan=2,sticky=E+W)


class MainFrame(FrameTemplate):
    def menu1(self):
        print("hi there, everyone!")
        self.gui.openedMenu = 0
        self.reset()
        # self.header.update()

    def transfercentre(self):
        if self.gui.openedMenu == 1:
            return
        self.gui.openedMenu = 1
        self.reset()
        # self.header.update()

        self.gui.labelFrame(self._frame, self.rowspan, self.columnspan)

        # Label(self._frame, text='Player').grid(row=0, column=0, columnspan=3)
        # search_player = Entry(self._frame)
        # search_player.grid(row=1, column=0, columnspan=3)

        # Label(self._frame, text='Team').grid(row=0, column=3, columnspan=3)
        # search_team = Entry(self._frame)
        # search_team.grid(row=1, column=3, columnspan=3)
        
        # self.gui.root.after(2000, lambda: self.repeatTest(search_player, search_team))

    def menu3(self):
        print("hi there, everyone!")
        self.gui.openedMenu = 2
        self.reset()
        # self.header.update()

    def repeatTest(self, search_player, search_team):
        if self.gui.openedMenu != 1:
            return
        print(search_player.get() + ' to ' + search_team.get())
        self.gui.root.after(2000, lambda: self.repeatTest(search_player, search_team))

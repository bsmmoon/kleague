from tkinter import *
from kleague.model import Model

MENU1_ID = '1'
TRANSFER_CENTRE_ID = '2'
MENU3_ID = '3'

class GUI(Frame):
    def __init__(self):
        self._model = Model()

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

        self._openedMenu = MENU1_ID

        self.menu = MenuFrame(self, self._root, rows-1, 0, 
            1, cols, 1, 1, 'red')
        self.header = HeaderFrame(self, self._root, 0, 0, 
            1, cols, 1, 1, 'blue')
        mainFrame = MainFrame(self, self._root, 1, 0, 
            rows-2, cols, 1, 1)

        self.header.update()
        self.menu.update(mainFrame)

    @property
    def model(self):
        return self._model

    @property
    def openedMenu(self):
        return self._openedMenu

    @openedMenu.setter
    def openedMenu(self, openedMenu):
        self._openedMenu = openedMenu

    @property
    def root(self):
        return self._root

    def labelFrame(self, frame, rows, cols):
        for r in range(rows):
            for c in range(cols):
                Label(frame, text='(' + str(r) + ',' + str(c) +')',
                    borderwidth = 1).grid(row = r, column = c)

    def iteration(self):
        self.header.update()

    def run(self):
        self.mainloop()


class FrameTemplate():
    def __init__(self, gui, parent, row, column, rowspan,
        columnspan, rowWeight, colWeight, bg=None):
        self._gui = gui
        self._parent = parent
        self._row = row
        self._column = column
        self._rowspan = rowspan
        self._columnspan = columnspan
        self._rowWeight = rowWeight
        self._colWeight = colWeight
        self._bg = bg

        self.reset()

    def reset(self):
        self._frame = Frame(self._parent, bg = self._bg)
        self._frame.grid(row = self._row, column = self._column,
            rowspan = self._rowspan, columnspan = self._columnspan,
            sticky = W+E+N+S)
        for r in range(self._rowspan):
            self._frame.rowconfigure(r, weight=self._rowWeight)
        for c in range(self._columnspan):
            self._frame.columnconfigure(c, weight=self._colWeight)

    @property
    def frame(self):
        return self._frame


class HeaderFrame(FrameTemplate):
    def update(self):
        self.reset()
        print(self._gui.openedMenu)
        if self._gui.openedMenu == MENU1_ID:
            Label(self._frame, text='1', borderwidth = 1).grid(
                row = 0, column = 0, columnspan = 6)
        elif self._gui.openedMenu == TRANSFER_CENTRE_ID:
            Label(self._frame, text='Transfer Centre', 
                borderwidth = 1).grid(row = 0, column = 0, columnspan = 6)
        elif self._gui.openedMenu == MENU3_ID:
            Label(self._frame, text='3', borderwidth = 1).grid(
                row = 0, column = 0, columnspan = 6)


class MenuFrame(FrameTemplate):
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
        self._gui.openedMenu = MENU1_ID
        self.reset()
        self._gui.iteration()

    def transfercentre(self):
        if self._gui.openedMenu == TRANSFER_CENTRE_ID:
            return
        self._gui.openedMenu = TRANSFER_CENTRE_ID
        self.reset()
        self._gui.iteration()

        Label(self._frame, text='Player').grid(
            row=0, column=0, columnspan=3)
        search_player = Entry(self._frame)
        search_player.grid(row=1, column=0, columnspan=3)

        Label(self._frame, text='Team').grid(
            row=0, column=3, columnspan=3)
        search_team = Entry(self._frame)
        search_team.grid(row=1, column=3, columnspan=3)

        self._gui.root.after(2000, 
            lambda: self.repeatTest(search_player, search_team))

    def menu3(self):
        print("hi there, everyone!")
        self._gui.openedMenu = MENU3_ID
        self.reset()
        self._gui.iteration()

    def repeatTest(self, search_player, search_team):
        if self._gui.openedMenu != TRANSFER_CENTRE_ID:
            return
        print(search_player.get() + ' to ' + search_team.get())

        self._gui.model.insert('4;person;'+str(search_player.get()))
        results = self._gui.model.getSearchResult()
        playerSearchResultFrame = SearchResultFrame(
            self._gui, self._frame, 2, 0, self._rowspan-3, 3, 0, 1)
        playerSearchResultFrame.labelFrame('Search Result:')
        playerSearchResultFrame.insertTable(results)

        self._gui.model.insert('4;team;'+str(search_team.get()))
        results = self._gui.model.getSearchResult()
        teamSearchResultFrame = SearchResultFrame(
            self._gui, self._frame, 2, 3, self._rowspan-3, 3, 0, 1)
        teamSearchResultFrame.labelFrame('Search Result:')
        teamSearchResultFrame.insertTable(results)

        self._gui.root.after(2000, 
            lambda: self.repeatTest(search_player, search_team))

    def testPrint(self):
        print('yay~')

class SearchResultFrame(FrameTemplate):
    def labelFrame(self, label):
        Label(self._frame, text=label).grid(row=0, column=0, columnspan=3)

    def insertTable(self, results):
        row = 1
        for result in results:
            searchTeamResult = Label(self._frame, text=result)
            searchTeamResult.grid(
                row=row, column=0, columnspan=self._columnspan)
            searchTeamResult.bind('<Button-1>', 
                lambda: self.testPrint())
            row += 1
        
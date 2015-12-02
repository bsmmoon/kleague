import sys
from kleague.parser import Parser
from kleague.storage import Storage
from kleague.data import Data
from kleague.command import Client
from kleague.crawler import Crawler

class Model:


    def __init__(self):
        print('model init')
        self.storage = Storage()
        self.data = Data()
        self.parser = Parser()
        self.client = Client()
        self.crawler = Crawler()

        self.storage.load(self.data)

    def insert(self, inputString):
        print('model insert ({})'.format(inputString))
        command = self.parser.parse(inputString)
        self.client.insert(command)

    def update(self):
        print('model update')

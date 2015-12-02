import sys
sys.path.insert(0, '.kleague')
from storage import Storage
from data import Data
from parser import Parser
from command import Client
from crawler import Crawler

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
        print('model insert ({})'.format(command))
        command = self.parser.pasre(inputString)
        self.client.insert(command)

    def update(self):
        print('model update')

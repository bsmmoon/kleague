import sys
from kleague.parser import Parser
from kleague.storage import Storage
from kleague.data import Data
from kleague.command import Client
from kleague.crawler import Crawler

class Model:


    def __init__(self):
        self.data = Data()
        self.storage = Storage(self.data)
        self.parser = Parser()
        self.client = Client()
        self.crawler = Crawler()

        self.storage.load()

    def insert(self, inputString):
        command = self.parser.parse(inputString)
        command.insertData(self.data)
        self.client.insert(command)
        self.storage.save()

    def pull(self):
        return self.data.getContracts()

import sys
from kleague.parser import Parser
from kleague.storage import Storage
from kleague.data import Data
from kleague.command import Client
from kleague.crawler import Crawler

class Model:


    def __init__(self):
        self._data = Data()
        self._storage = Storage(self._data)
        self._parser = Parser()
        self._client = Client()
        self._crawler = Crawler()

        self._storage.load()

    def insert(self, inputString):
        command = self._parser.parse(inputString)
        command.insertData(self._data)
        self._client.insert(command)
        self._storage.save()

    def pull(self):
        output = []

        models = [
            self._data.getContracts(), 
            self._data.getPeople(), 
            self._data.getTeams()
        ]

        for model in models:
            string = ''
            for entry in model:
                string += '{' + str(entry) + '}'
            output.append(string)

        return output

    def getSearchResult(self):
        return self._data.searchResult
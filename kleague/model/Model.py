import sys
sys.path.insert(0, '.kleague')
from storage import Storage
from command import Client
from crawler import Crawler

class Model:


    def __init__(self):
        print('model init')
        self.storage = Storage()
        self.client = Client()
        self.crawler = Crawler()

    def insert(self, command):
        print('model insert ({})'.format(command))

    def update(self):
        print('model update')

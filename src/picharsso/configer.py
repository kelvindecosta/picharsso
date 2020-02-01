from json import load, dump
from types import SimpleNamespace
from os.path import join, dirname

class Configer:
    """A wrapper to load configuration
    """
    def __init__(self):
        self.config_file = join(dirname(__file__), "config.json")
        self.load_config()


    def load_config(self):
        with open(self.config_file, "r") as f:
            self.configuration = SimpleNamespace(**load(f))

    def config(self):
        print(self.config_file)
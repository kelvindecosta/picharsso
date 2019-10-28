from interface import Interface
from loader import Loader
from resizer import Resizer
from processor import Processor
from colorizer import Colorizer
from displayer import Displayer


class Session(Interface, Loader, Resizer, Processor, Colorizer, Displayer):
    """A wrapper for the program
    """
    def __init__(self):
        Interface.__init__(self)
        Loader.__init__(self)
        Resizer.__init__(self)
        Processor.__init__(self)
        Colorizer.__init__(self)
        Displayer.__init__(self)
        
        getattr(self, self.args.command)()

if __name__ == "__main__":
    sess = Session()
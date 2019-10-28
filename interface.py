from argparse import ArgumentParser


class Interface:
    """A wrapper for the command line interface
    """
    def __init__(self):
        """Creates a parser and parses arguments
        """
        self.args = self.get_argparser().parse_args()


    def get_argparser(self):
        """Defines the argument parser        
        """
        parser = ArgumentParser(description="Image to Text Art", prog="image-to-text-art")

        parser.add_argument("source", type=str, help="path to source image")
        parser.add_argument("-o", "--output", type=str, help="path to output file", metavar="")
        parser.add_argument("-c", "--color", action="store_true", help="keep color", default=False)
        parser.add_argument("-v", "--verbose", action="store_true", help="verbose output", default=False)
        
        parser.add_argument("-W", "--width", type=int, help="width of output in characters", metavar="", default=None)
        parser.add_argument("-H", "--height", type=int, help="height of output in characters", metavar="", default=None)
        parser.add_argument("-r", "--ratio", action="store_true", help="preserve aspect ratio", default=False)

        subparsers = parser.add_subparsers(dest="command")
        
        p_ascii = subparsers.add_parser("ascii", help="apply ASCII")

        p_braille = subparsers.add_parser("braille", help="apply Braille")
        p_braille.add_argument("-t", "--threshold", type=int, help="threshold for pixel", default=128, metavar="")
        
        return parser
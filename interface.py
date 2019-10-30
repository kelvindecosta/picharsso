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
        parser = ArgumentParser(description="Image to Text Art", prog="img2txt", usage="%(prog)s [options]\nconfig: {}\n".format(self.config_file))
        commands = parser.add_subparsers(dest="command")
        
        # art
        p_art = ArgumentParser(add_help=False)
        p_art.add_argument("image", type=str, help="path to image")
        p_art.add_argument("-c", "--color", action="store_true", help="keep color", default=False)
        p_art.add_argument("-W", "--width", nargs="?", type=int, help="width of output in characters, flags to fit terminal", metavar="width", default=False)
        p_art.add_argument("-H", "--height", nargs="?", type=int, help="height of output in characters, flags to fit terminal", metavar="height", default=False)
        p_art.add_argument("-o", "--output-type", choices=["ansi", "html"], default=self.config.output_type, help="type of output")
        p_art.add_argument("-f", "--output-file", type=str, help="path to output file")
        p_art.add_argument("-q", "--quiet", action="store_true", help="disable console output")

        # art > ascii
        p_ascii = commands.add_parser("ascii", help="apply ASCII", parents=[p_art])
        p_ascii.add_argument("-s", "--charset", type=int, help="choice of charset (options available in config)", choices=range(len(self.config.charsets)), default=self.config.charset)
        p_ascii.add_argument("-n", "--negative", action="store_true", help="reverse grayscale")

        # art > braille
        p_braille = commands.add_parser("braille", help="apply Braille", parents=[p_art])
        p_braille.add_argument("-t", "--threshold", type=int, help="threshold pixel intensity", default=self.config.threshold, metavar="threshold")

        return parser

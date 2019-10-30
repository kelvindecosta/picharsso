class Displayer:
    """A wrapper for displaying output
    """
    def display(self):
        """Displays text art and saves it to a file if necessary
        """
        output = {
            "ansi" : lambda x : "\n".join(["".join(row) for row in x]),
            "html" : lambda x : "<div>{}</div>".format("\n<br />".join(["".join(row) for row in x]))
        }
        art = output.get(self.args.output_type)(self.text)
        
        if not self.args.quiet:
            print(art)

        if self.args.output_file:
            with open(self.args.output_file, "w") as f:
                f.write(art)

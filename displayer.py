class Displayer:
    """A wrapper for displaying output
    """
    def display(self):
        """Displays text art and/or saves it to a file
        """
        art = "\n".join(["".join(row) for row in self.text])
        if self.args.output:
            with open(self.args.output, "w") as f:
                f.write(art)

        if self.args.verbose:
            print(art)
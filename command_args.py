import argparse

class CommandArgs:
    """A class to read the arguments from command line ."""

    def __init__(self):
        """Initialize command arguments."""
        # Use the argparse module in the Python standard library to parse command-line arguments.
        parser = argparse.ArgumentParser()
        # Receive the parameter of the file name to be translated in the command line.
        parser.add_argument("filename", help="Name of the input file")
        # Select if show the text and the translated text in the console.
        parser.add_argument("--show", help="Show the text and the translated text in the console", action="store_true")
        # Select if use the api from Azure.
        parser.add_argument("--azure", help="Use the api from Azure.", action="store_true")
        # The test mode: only translate the first 3 short texts
        parser.add_argument("--test", help="Only translate the first 3 short texts", action="store_true")
        # If use the translated name table
        parser.add_argument("--tlist", help="Use the translated name table", action="store_true")
        
        self.args = parser.parse_args()
        
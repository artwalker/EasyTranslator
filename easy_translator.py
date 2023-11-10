from command_args import CommandArgs
from parameter_reader import ParameterReader
from process_file import ProcessFile

class TranslateText:
    """Overall class to manage text translation."""

    def __init__(self):
        """Initialize parameters about the text translation."""
        # 1. Read the command line arguments.
        self.commandArgs = CommandArgs()
        # 2. Read the parameters from the settings.cfg file and the .env file.
        #    and process the parameters.
        self.parameterReader = ParameterReader(self.commandArgs)
        # 3. Prepare to translate the text.
        self.processFile = ProcessFile(self.parameterReader)

    def run_translation(self):
        """Run the text translation."""
        # 4. Process the file.
        self.processFile.get_title()
        self.processFile.convert_text()
        self.processFile.tranlate_file()
        self.processFile.caculate_tokens_costs()
        self.processFile.remove_jsonfile()

if __name__ == '__main__':
    # Make a translation instance, and run the translation.
    tt = TranslateText()
    tt.run_translation()

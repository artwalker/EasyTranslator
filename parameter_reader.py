import openai
import os
import chardet
import configparser
import random
import json

from dotenv import load_dotenv, find_dotenv
from command_args import CommandArgs

class ParameterReader:
    """A class to read the parameters from the settings.cfg file and the .env file."""

    def __init__(self, commandArgs):
        """Read the parameters from the settings.cfg file and the .env file."""
        # The command line arguments
        self.commandArgs = commandArgs
        self.filename = ""
        self.show = ""
        self.azure = ""
        self.test = ""
        self.tlist = ""
        self.base_filename = ""
        self.file_extension = ""
        self.new_filename = ""
        self.new_filenametxt = ""
        self.jsonfile = ""
        self.translated_dict = {}
        self.api_proxy_url = ""
        self.gpt_model = ""
        self.openai_api_engine_azure = ""
        self.gpt_temperature = ""
        
        # The arguments from the settings.cfg file
        self.language = ""
        self.prompt_template = ""
        self.prompt = ""
        self.bilingual_output = ""
        self.language_code = ""
        self.api_proxy = ""
        self.startpage = ""
        self.endpage = ""
        self.transliteration_list_file = ""
        self.transliteration_word_capi_low = ""

        # 1. Set the parameters from the command line.
        self._set_args_from_command()
        # 2. Set the OpenAI API key.
        self._access_openai_key()
        # 3. Set the OpenAI API url.
        self._access_openai_url()
        # 4. Set the parameters from the settings.cfg file and the .env file.
        self._set_args_from_parameter_reader()
        # 5. Load the translated dictionary from the json file.
        self._load_tranlated_dict()

    def _access_openai_key(self):
        """set the OpenAI API key."""
        _ = load_dotenv(find_dotenv(), override=True)
        self.gpt_temperature = float(os.getenv('GPT_TEMPERATURE'))
        if self.azure:
            # Get the OpenAI API keys from the .env file
            key_sets = os.getenv('OPENAI_API_KEY_AZURE')
            # If there are multiple keys, split them into an array
            key_array = key_sets.split(',')
            # Set the OpenAI API key
            openai.api_key  = random.choice(key_array)
            openai.api_base = os.getenv('OPENAI_API_BASE_AZURE')
            openai.api_type = os.getenv('OPENAI_API_TYPE_AZURE')
            openai.api_version = os.getenv('OPENAI_API_VERSION_AZURE')
            self.openai_api_engine_azure = os.getenv('OPENAI_API_ENGINE_AZURE')
        else:
            # Get the OpenAI API keys from the .env file
            key_sets = os.getenv('OPENAI_API_KEY')
            # If there are multiple keys, split them into an array
            key_array = key_sets.split(',')
            # Set the OpenAI API key
            openai.api_key  = random.choice(key_array)
            self.gpt_model = os.getenv('GPT_MODEL')

    def _access_openai_url(self):
        """Set the OpenAI API url."""
        # If there is proxy, then use it
        if len(self.api_proxy) == 0:
            print("-" * 3)
            print(f"\033[1;32mOpenAI API proxy not detected, currently using the api address: {openai.api_base}\033[0m") 
        else:
            self.api_proxy_url = self.api_proxy + "/v1"
            openai.api_base = os.environ.get("OPENAI_API_BASE", self.api_proxy_url)
            print("-" * 3)
            print(f"\033[1;32mUsing OpenAI API proxy, the proxy address is: {openai.api_base}\033[0m")

    def _set_args_from_parameter_reader(self):
        """Get the settings from the settings.cfg file."""
        with open('settings.cfg', 'rb') as f:
            content = f.read()
            self.encoding = chardet.detect(content)['encoding']

        with open('settings.cfg', encoding=self.encoding) as f:
            config_text = f.read()
            self.config = configparser.ConfigParser()
            self.config.read_string(config_text)
        
        # Get the settings from the settings.cfg file
        self.language = self.config.get('config', 'language')
        self.prompt_template = self.config.get('config', 'prompt')
        self.prompt = self.prompt_template.format(self.language)
        self.bilingual_output = self.config.get('config', 'bilingual-output')
        self.language_code = self.config.get('config', 'langcode')
        self.api_proxy=self.config.get('config', 'openai-proxy')
        # Get the start and end page of the PDF file
        self.startpage = self.config.getint('config', 'startpage', fallback=1)
        self.endpage = self.config.getint('config', 'endpage', fallback=-1)
        # Get the transliteration list file
        self.transliteration_list_file = self.config.get('config', 'transliteration-list')
        # Get the setting of case to determine whether to do transliteration
        self.transliteration_word_capi_low = self.config.get('config', 'transliteration-word-capi-low')

    def _set_args_from_command(self):
        """Set arguments from the command line."""
        self.filename = self.commandArgs.args.filename
        self.show = self.commandArgs.args.show
        self.test = self.commandArgs.args.test
        self.tlist = self.commandArgs.args.tlist
        self.azure = self.commandArgs.args.azure

        self.base_filename, self.file_extension = os.path.splitext(self.filename)
        self.new_filename = self.base_filename + "_translated.epub"
        self.new_filenametxt = self.base_filename + "_translated.txt"
        self.jsonfile = self.base_filename + "_process.json"

    def _load_tranlated_dict(self):
        """
        Load the translated dictionary from the json file.
        Such as the translation stoped in the middle, 
        and the translated dictionary is saved in the json file.
        So we can continue the translation from the last stop.
        """
        try:
            if os.path.getsize(self.jsonfile) > 0:
                with open(self.jsonfile, "r", encoding="utf-8") as f:
                    self.translated_dict = json.load(f)
        except Exception as e:
            #print(e)
            pass

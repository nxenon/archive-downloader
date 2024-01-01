from utils.argument_parser import ScriptParser
from utils.checker import start_checking

def start_engine():
    # check requirements
    start_checking()
    # start parser process
    script_parser = ScriptParser()
    script_parser.start_parsing()
    script_parser.check_arguments()

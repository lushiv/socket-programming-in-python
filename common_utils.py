import os.path,sys
from os.path import dirname, join, abspath
import configparser
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
conf_file = BASE_DIR+'/configuration.ini'
config = configparser.RawConfigParser()
config.read(conf_file)

sys.path.insert(0, abspath(join(dirname(__file__), '..')))

def get_error_traceback(sys, e):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    return "%s || %s || %s || %s" %(exc_type, fname, exc_tb.tb_lineno,e)
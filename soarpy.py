# Soarpy specific instances
from backend.tasks import *
from backend.utils import parsers
# default Python modules
import argparse
import logging

# Main method starting all stuff up
def soarpy():
    s = Start()
    print(parsers.get_func_info(s))

argparser = argparse.ArgumentParser(description='CLI for soarpy')
argparser.add_argument('d', action = "store_true", default = False, help='Activates debugmode')
args = argparser.parse_args()

if __name__ == "__main__":
    soarpy()
    
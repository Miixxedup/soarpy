from parsers import parse_playbook
from core import state
from tasks import *

def execute_script(name):
    tmp = eval(name)
    tmp.hello_world()

def main():
    sequence = parse_playbook.parse_playbook("playbooks/test.spy")
    for g in sequence:
        execute_script(g)
        

main()

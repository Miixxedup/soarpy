from parsers import parse_playbook
from core import state
from tasks import *

# Execute scripts from tasks folder when called.
def execute_script(name, inputs):
    tmp = eval(name)
    values = tmp.task(inputs)
    return values

# Mainloop which contains all the logic for a SOARPY instance.
def main():

    # Gather all instances to run
    sequence = parse_playbook.parse_playbook("playbooks/test.spy")
    
    for g in sequence:
        if g == "start":
            inputs = "ENTER VARIABLES HERE"
        else:    
            inputs = state.STATE_DICT[state.PREVIOUS_STATE]["OUTPUT"]
        result = execute_script(g, inputs)
        state.add_state(g,inputs, result)
        state.PREVIOUS_STATE = g

    state.show_states()
main()

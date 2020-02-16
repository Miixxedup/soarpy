# This method contains all logic dealing with the State.

# Main storage method for sharing variables between scripts.
# Store the name of a state, add for each state two other dicts which contain all
# input and output variables
STATE_DICT = {}
PREVIOUS_STATE = ""

# Add a new state to the dict.
def add_state(name, inputvars = [], outputvars= []):
    #Create new key for the state using the name
    STATE_DICT[name] = dict()
    #Store variables in INPUT and OUTPUT dict entry for the statename.
    STATE_DICT[name]["INPUT"] = inputvars
    STATE_DICT[name]["OUTPUT"] = outputvars

# Modify existing values.
def modify_state(name, values, inout = "OUTPUT"):
    STATE_DICT[name][inout] = values

# Show all states and all stored values
def show_states():
    for state in STATE_DICT:
        print(f"State: {state}")
        for i in STATE_DICT[state]:
            print(f"----{i}:{STATE_DICT[state][i]}")

# Show the variables within a state
def show_state(name):
    for i in STATE_DICT[name]:
        for j in i:
            print(j)

#Read a state
def read_state(name):
    pass

# Method to test if the state contains the required parameters.
def check_state(name):
    pass
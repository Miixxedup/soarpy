# This method contains all logic dealing with the State.

# Main storage method for sharing variables between scripts.
# Store the name of a state, add for each state two other dicts which contain all
# input and output variables
STATE_DICT = {}

# Add a new state to the dict.
def add_state(name, inputvars, outputvars):
    STATE_DICT[name] = inputvars
    STATE_DICT[name] = outputvars


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
def hello_world():
    return "Hello Finish!!"

# Required Task definition for the playbooks.
def task(*args):
    inputs = args[0]
    outputs = hello_world()
    return outputs

def hello_world():
    return "Hello Script1!!"

# Required Task definition for the playbooks.
def task(*args):
    inputs = args[0]
    outputs = hello_world()
    return outputs

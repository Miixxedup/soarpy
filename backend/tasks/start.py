class Start:
    __version__ = "1337"
    __name__ = "Start"
    """
    Basic testing class to get the correct details for the frontend
    """
    def __init__(self):
        print("Start class checking in")
    
    def hello_world(self, kappa, leet, copter = 4):
        groetjes  = 1
        return "Hello Start !!"

    # Methods
    def task(*args):
        inputs = args[0]
        outputs = hello_world()
        return outputs

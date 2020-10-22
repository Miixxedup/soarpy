import inspect
from types import FunctionType

# Create a 'convinient' entry which can be used later to invoke classes from the frontend interface
def get_func_info(f: FunctionType) -> dict:
    
    information = dict()  
    information['class_name'] = f.__name__
    information['functions'] = [d for d in dir(f) if not d.endswith("__")]
    # Get all functions + their params
    tmp_dict = dict()
    for g in information['functions']:
        o = getattr(f,g)
        o = inspect.signature(o)
        tmp_dict[g] = []
        for p in o._parameters.values():
            tmp_dict[g].append((p.name,p.default))    
    information["func+param"] = tmp_dict
    return information


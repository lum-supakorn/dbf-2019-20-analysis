from itertools import product

def generate(iter_dict):
    return [dict(zip(iter_dict, v)) for v in product(*iter_dict.values())]
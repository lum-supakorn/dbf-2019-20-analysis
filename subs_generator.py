from itertools import product
from IPython.display import clear_output

def generate(iter_dict):
    return [dict(zip(iter_dict, v)) for v in product(*iter_dict.values())]

def calculate(f, all_subs):
    n = len(all_subs)
    all_calc = []
    for count, subs in enumerate(all_subs):
        clear_output()
        print("{}/{}\t{:.2f}%".format(count, n, count * 100 / n))
        subs["total"] = f.subs(subs).evalf
        all_calc.append(subs)
    print("Sorting...")
    return sorted(all_calc, key=lambda x: x["total"], reverse=True)
        
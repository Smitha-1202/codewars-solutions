import re

def hydrate(drink_string):
    total = sum(int(n) for n in re.findall(r'\d+', drink_string))
    unit = "glass" if total == 1 else "glasses"
    return f"{total} {unit} of water"
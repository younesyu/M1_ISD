import numpy as np
# A vous
def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

def display_stat (dico) :
    min_pl = min(dico["petal_length"])
    max_pl = max(dico["petal_length"])
    min_sl = min(dico["sepal_length"])
    max_sl = max(dico["sepal_length"])
    
    
    min_pw = min(dico["petal_width"])
    max_pw = max(dico["petal_width"])
    min_sw = min(dico["sepal_width"])
    max_sw = max(dico["sepal_width"])
    
    avg_pl = mean(dico["petal_width"])
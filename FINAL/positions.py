import numpy as np
import handles

def create_var(var_name, var_value):
    globals()[var_name] = var_value

with open('pos.txt') as f:
    contents = f.readlines()

for i in range(0,len(contents)):
    if contents[i] == 'quit':
        break
    elif (i % 2 == 0):
        name = str(contents[i])
        name = name[1:-1]
    elif (i % 2 == 1):
        value = contents[i]
        value = value[:-1]
        value = value.split(";")
        for j in range(0,len(value)):
            value[j] = float(value[j])
        create_var(name, value)


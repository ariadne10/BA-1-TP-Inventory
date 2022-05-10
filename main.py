import pandas as pd
import numpy as np

df = pd.read_excel (r'C:\Users\rmeli\Desktop\BA-1 TP Inventory 01 Apr 2022 Area Chart.xlsx', sheet_name='Data')

tp_loading = 0.225
yield_per_ferm_run = 1465
EOM = 6850
FY22_ferm_run_plan = [0,3,6,0,0,0,0,6,0,0,0,0,0]

Month = ['March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'January', 'Feburary', 'March', 'April']

demand = []

input_string = input('Enter KG demand for blend A585002 from March 22 - March 23: ')

demand_A585002 = input_string.split()


for i in range(len(demand_A585002)):
    # convert each item to int type
    demand_A585002[i] = int(float(demand_A585002[i]))
    

for i in demand_A585002:
    x = i * tp_loading
    demand.append(x)

production = [0]

for i in FY22_ferm_run_plan:
    x = i * yield_per_ferm_run
    production.append(x)
    

EOM_inventory = [EOM]
for x,y,z in zip(production, demand, EOM_inventory):
    diff = x - y
    final = z + diff
    EOM_inventory.append(final)

pop = EOM_inventory.pop(0)


data_tuples = list(zip(Month, production, demand, EOM_inventory))



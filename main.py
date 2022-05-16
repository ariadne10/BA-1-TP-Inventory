# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Demonstrated KG yield per ferm run, EOM Inventory, FY22 Ferm Run Plan, KG demand, Sort, TP loading)
# dataset = dataset.drop_duplicates()


import pandas as pd
import numpy as np
import matplotlib.pylab as plt


Month = ['March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'January', 'Feburary', 'March', 'April']

input_demand_ = dataset['KG demand']
input_tp_loading = dataset.iloc[0]['TP loading']
input_yield_per_ferm_run = dataset.iloc[0]['Demonstrated KG yield per ferm run']
input_EOM = dataset.iloc[0]['EOM Inventory']
input_ferm_run_plan = dataset['FY22 Ferm Run Plan']

input_demand_ = ' '.join(str(i) for i in input_demand_)
#input_tp_loading = ' '.join(str(input_tp_loading))
#input_yield_per_ferm_run = ' '.join(str(input_yield_per_ferm_run))
#input_EOM = ' '.join(str(input_EOM))
input_ferm_run_plan = ' '.join(str(i) for i in input_ferm_run_plan)


demand_A585002 = input_demand_.split()
tp_loading = float(input_tp_loading)
yield_per_ferm_run = float(input_yield_per_ferm_run)
EOM = float(input_EOM)
FY22_ferm_run_plan = input_ferm_run_plan.split()



for i in range(len(demand_A585002)):
    # convert each item to int type
    demand_A585002[i] = float(demand_A585002[i])


for i in range(len(FY22_ferm_run_plan)):
    # convert each item to int type
    FY22_ferm_run_plan[i] = float(FY22_ferm_run_plan[i])


demand = []

for i in demand_A585002:
    x = i * float(tp_loading)
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

plt.rcParams["figure.figsize"] = (10,5)

df = pd.DataFrame(data_tuples, columns=['Month', 'production', 'demand', 'EOM_inventory'])

print(df)

df.plot(x ='Month', kind = 'bar')

plt.title("BA-1 TP 15620 Inventory 01-Apr-2022")

plt.show()


"""
"""
from utilities import dict_to_csv

with open("capitals.txt", "w") as capitals_file:
    capitals_file.write("New Delhi\nMumbai\nBangalore\nChennai\nKolkata\n")

with open("states.txt", "w") as states_file:
    states_file.write("Delhi\nMaharashtra\nKarnataka\nTamil Nadu\nWest Bengal\n")

def clean_data(data):
    clean_data=[]
    for line in data:
        clean_data.append(line.strip())
    return clean_data

with open("capitals.txt", "r") as capitals_file:
    capitals = clean_data(capitals_file.readlines())

with open("states.txt", "r") as states_file:
    states = clean_data(states_file.readlines())
state_capital_list=[] 
if len(capitals) != len(states):
    print("The number of states and capitals do not match!")
else:
    
    for i in range(len(states)):
        state_capital_dict = {}
        # state_capital_dict[states[i]] = capitals[i]
        state_capital_dict['states'] = states[i]
        state_capital_dict['capitals'] = capitals[i]
        state_capital_list.append(state_capital_dict)        

    print("State-Capital Dictionary:")
    for state, capital in state_capital_dict.items():
        print(f"{state}: {capital}")
dict_to_csv(data=state_capital_list,filename='state_capitals.csv', fieldnames=["states","capitals"])
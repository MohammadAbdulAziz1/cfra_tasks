import pandas as pd
import os
df = pd.read_csv('StatewiseTestingDetails.csv')

script_name = os.path.splitext(os.path.basename(__file__))[0]
output_folder = script_name
os.makedirs(output_folder, exist_ok=True)

states = df.State.unique()

for state in states:
    state_df = df[df['State'] == state]

    state_file_name = state.replace(" ", "_") + ".csv"

    output_path = os.path.join(output_folder, state_file_name)

    state_df.to_csv(output_path, index=False)
print(f"All files have been saved in the folder: {output_folder}")

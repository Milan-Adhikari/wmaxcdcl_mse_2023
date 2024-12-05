import os
import re
from utils.parse_wmaxcdcl_output_2 import parse_wmaxcdcl_output

cwd = os.getcwd()
individual_file_path = os.path.join(cwd, 'results/uf250_30_31_individual.csv')

new_file_identifier = '#$!=' 

with open(individual_file_path, 'r') as f:
    lines = f.readlines()
    
data_dict = {}
current_file = None
current_data = []

for line in lines:
    if line.startswith(new_file_identifier):
        if current_file:
            data_dict[current_file] = "\n".join(current_data)
            current_data = []
             
        current_file = line.split(new_file_identifier)[1].strip()
    else:
        current_data.append(line)
        
if current_file:
    data_dict[current_file] = "\n".join(current_data)

output_file = 'uf250_30_31_individual.csv'

with open(output_file, 'w') as of:
    of.write('file_name; optimization_time; optimal_objective; total_time; remarks;\n')
    
    for key, value in data_dict.items():
        parsed_data = parse_wmaxcdcl_output(value)
        of.write(f'{key}; {parsed_data["time"]}; {parsed_data["optimal_value"]}; {parsed_data["time"]}; ' + str({'status': 'OPTIMAL'}) + ";\n")
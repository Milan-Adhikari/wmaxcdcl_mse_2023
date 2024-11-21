import os
import lzma
from utils.list_all_paths_in_a_folder_containing_files import list_all_paths_in_a_folder_containing_files

def zip_into_xz(input_file_path, output_file_path):
    output_file_path = output_file_path + '.xz'
    with open(input_file_path, 'rb') as input_file, lzma.open(output_file_path, 'wb') as output_file:
        output_file.write(input_file.read())

CWD = os.getcwd()  # Current working directory

# Path to the directory containing the files to be zipped
dir_path = os.path.join(CWD, 'converted-benchmarks')

# Path to the directory where the zipped files will be stored
zip_dir_path = os.path.join(CWD, 'converted-benchmarks-zipped')
os.makedirs(zip_dir_path, exist_ok=True)

all_paths_in_dir = list_all_paths_in_a_folder_containing_files(dir_path)

# print(f'Zipping files in {dir_path}...')
# print(f'{all_paths_in_dir}')
for path in all_paths_in_dir:
    for file in os.listdir(path):
        input_file_path = os.path.join(path, file)
        output_file_path = input_file_path.replace(dir_path, zip_dir_path)
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
        zip_into_xz(input_file_path, output_file_path)
        print(f'Zipped {input_file_path} to {output_file_path}.xz')

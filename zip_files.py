import os
import lzma

def zip_into_xz(input_file_path, output_file_path):
    output_file_path = output_file_path + '.xz'
    with open(input_file_path, 'rb') as input_file, lzma.open(output_file_path, 'wb') as output_file:
        output_file.write(input_file.read())

CWD = os.getcwd()  # Current working directory

# Path to the directory containing the files to be zipped
dir_path = os.path.join(CWD, 'satlib_uf250')

# Path to the directory where the zipped files will be stored
zip_dir_path = os.path.join(CWD, 'satlib_uf250_zipped')
os.makedirs(zip_dir_path, exist_ok=True)

# Iterate over the files in the directory
for file_name in os.listdir(dir_path):
    file_path = os.path.join(dir_path, file_name)
    zip_file_path = os.path.join(zip_dir_path, file_name)
    zip_into_xz(file_path, zip_file_path)
    print(f'{file_name} zipped successfully')

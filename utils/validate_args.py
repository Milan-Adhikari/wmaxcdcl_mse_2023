import os
from global_variables import CWD

def validate_folder(folder: str, benchmark_folder) -> None:
    if not os.path.exists(CWD + "/" + benchmark_folder + "/" + folder):
        print(f'Invalid folder "{folder}" ! Available folders are: ')
        for folder in os.listdir(CWD + "/" + benchmark_folder):
            print(folder)
        exit(1)
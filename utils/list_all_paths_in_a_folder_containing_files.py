import os

def list_all_paths_in_a_folder_containing_files(folder_path):
    subpaths = []
    for root, _, files in os.walk(folder_path):
        if files:
            subpaths.append(root)
    return subpaths

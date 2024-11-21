import time
import argparse
import subprocess
from global_variables import *
from utils.validate_args import validate_folder
from utils.parse_wmaxcdcl_output import parse_wmaxcdcl_output
from utils.check_file_size_limit import validate_file_size_exceeded
from utils.read_file_names_from_results import read_the_existing_file_names

def wmaxcdcl_main(file_path: str) -> None:
    # remarks for several cases that happen in the code
    remarks = {}
    cmd = [WMAXCDCL_COMMAND, file_path]

    try:
        # keep the optimization output to save in the file
        result = subprocess.run(
            cmd,
            text=True,
            capture_output=True,
            # timeout=500
        )
        # get the output
        captured_output = result.stdout
        # parse the output
        output = parse_wmaxcdcl_output(captured_output)
        # individual file
        ind_file = captured_output
        # combined file
        combined_file = [output["time"], output["optimal_value"]]
        # remarks
        remarks["status"] = "OPTIMAL"
        # return the optimal value and the time
        return ind_file, combined_file, remarks
    except subprocess.CalledProcessError as e:
        # return the output of the command if it failed
        remarks["status"] = "ERROR : " + str(e)
        return "None", ["None", "None"], remarks
    except Exception as e:
        print(f"Exception: {e}")
        remarks["status"] = "ERROR : " + str(e)
        return "None", ["None", "None"], remarks
    except subprocess.TimeoutExpired as e:
        # return the exception as a string if the command failed
        remarks["status"] = "TIMEOUT : " + str(e)
        return "None", ["None", "None"], remarks

# we are going to parse the arguments because we want to run different folders from the command line
parser = argparse.ArgumentParser(description='WMAXCDCL Main')
# add arguments
parser.add_argument('folder', type=str, help='Folder name')
# parse arguments
args = parser.parse_args()
# get the folder name
folder_name = args.folder

if __name__ == "__main__":
    # validate the folder such that it exists
    validate_folder(folder_name, CONVERTED_BENCHMARK_FOLDER)
    # benchmark folder for the original benchmarks
    benchmark_folder = CWD + "/" + CONVERTED_BENCHMARK_FOLDER + "/" + folder_name
    # results folder for the gurobi original
    results_folder = CWD + "/" + RESULTS_FOLDER + "/" + "wmaxcdcl" + "/" + folder_name
    os.makedirs(results_folder, exist_ok=True)
    # results_path
    combined_results_path = results_folder + "/" + folder_name + ".csv"
    individual_results_path = results_folder + "/" + folder_name + "_individual.csv"
    already_processed_files = []
    # if the combined results file exists, then read the file names to avoid processing them again
    if os.path.exists(combined_results_path):
        already_processed_files = read_the_existing_file_names(combined_results_path)
        if "file_name" in already_processed_files:
            already_processed_files.remove("file_name")
    else:
        # write the headers to the combined results file
        with open(combined_results_path, "w") as f:
            f.write(f"{WMAXCDCL_HEADERS}\n")

    # get all the files in the benchmark folder
    all_files = [f for f in os.listdir(benchmark_folder) if f.endswith(".wcnf.xz")]
    all_files.sort()

    for file in all_files:
        # now we treat each file independently
        t = time.time() # start the timer
        # skip the file if it is already processed
        if file in already_processed_files:
            print(f"File: {file} already processed")
            continue
        # get the file path
        file_path = benchmark_folder + "/" + file  # file path
        # validate file size limit that it is not exceeded
        if validate_file_size_exceeded(file_path):
            print(f"File size exceeded for file: {file_path}")
            continue
        print(f"Processing file: {file_path}")
        # run the wmaxcdcl solver
        individual_file, combined_file, remarks = wmaxcdcl_main(file_path)
        total_time = time.time()-t
        print(f"Total time taken: {total_time}")
        # write to the combined file
        with open(combined_results_path, "a") as f:
            f.write(f"{file}; {combined_file[0]}; {combined_file[1]}; {total_time}; {remarks};\n")

        # write to the individual file
        with open(individual_results_path, "a") as f:
            f.write(f"#$!={file}#$!=\n")
            f.write(individual_file)   


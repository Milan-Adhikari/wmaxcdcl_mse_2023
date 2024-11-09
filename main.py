import os
from utils.run_solver import run_solver
from utils.parse_wmaxcdcl_output import parse_output
from utils.check_file_size_limit import validate_file_size_exceeded


def main():
    combined_csv_file_name = BENCHMARK_DIR.split('/')[-1] + '.csv'
    benchmark_csv_file = os.path.join(OUTPUT_DIR, combined_csv_file_name)
    already_computed_files = []
    
    # Read the already computed files if the file exists
    if os.path.exists(benchmark_csv_file):
        with open(benchmark_csv_file, 'r') as f:
            lines = f.readlines()
            already_computed_files = [line.split(';')[0] for line in lines[1:]]  # Skip the header line and get the benchmark file names
    else:
        # Create the file if it does not exist
        with open(benchmark_csv_file, 'w') as f:
            f.write('wcnf_file_name; optimum_value;\n')  # Write the header
    
    # Iterate over the benchmarks
    for benchmark in os.listdir(BENCHMARK_DIR):
        # Skip already computed files
        if benchmark in already_computed_files:
            print(f'{benchmark} already computed. Skipping...')
            continue

        benchmark_path = os.path.join(BENCHMARK_DIR, benchmark)

        file_size_exceeded = validate_file_size_exceeded(benchmark_path)
        if file_size_exceeded:
            print(f'{benchmark} exceeds the file size limit. Skipping...')
            continue

        print(f'Running {benchmark_path}')

        # Run the solver 
        output = run_solver(BINARY_PATH, benchmark_path)
        # Parse the output
        optimum_value = parse_output(output)
        
        if optimum_value is not None:
            print(f'Optimum value: {optimum_value}')
            # Append to combined CSV file
            with open(benchmark_csv_file, 'a') as f:
                f.write(f'{benchmark}; {optimum_value};\n')
                # f.close()
        else:
            print('No optimum found')
            with open(benchmark_csv_file, 'a') as f:
                f.write(f'{benchmark}; None;\n')
                # f.close()
        
        # Write entire solver output to a file
        output_file = os.path.join(INDIVIDUAL_RESULTS_DIR, benchmark.replace(".wcnf.xz", ".txt") + '.txt')
        with open(output_file, 'w') as f:
            f.write(output)
            f.close()


CWD = os.getcwd()  # Current working directory
BENCHMARK_DIR = os.path.join(CWD, 'mse23-exact-weighted-benchmarks')  # Directory containing benchmarks
BINARY_PATH = os.path.join(CWD, 'starexec_run_wmaxcdcl-scip600-maxhs1200')  # Path to the binary
OUTPUT_DIR = os.path.join(CWD, 'output')  # Directory to store output
# Create output directory if it does not exist
os.makedirs(OUTPUT_DIR, exist_ok=True)
INDIVIDUAL_RESULTS_DIR = os.path.join(OUTPUT_DIR, 'individual_results')  # Directory to store individual results
os.makedirs(INDIVIDUAL_RESULTS_DIR, exist_ok=True)


main()
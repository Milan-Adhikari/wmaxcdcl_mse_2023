import os
# current working directory
CWD = os.getcwd()

# time limit for the solvers
TIMEOUT_LIMIT = 500
# file size limit for the solvers
FILE_SIZE_LIMIT = 5 * 1024 * 1024
CONVERTED_BENCHMARK_FOLDER = "converted-benchmarks-zipped"
# results folder
RESULTS_FOLDER = "results"
# WMAXCDCL COMMAND
WMAXCDCL_COMMAND = CWD + "/starexec_run_wmaxcdcl-scip600-maxhs1200"

# FILE ENTRIES FOR CONSISTENCY
FILE_NAME = "file_name"
OPTIMIZATION_TIME = "optimization_time"
OPTIMAL_OBJ = "optimal_objective"
CPU_TIME = "cpu_time"
MAXSAT = "maxsat"
HARD_CONFLICTS = "hard_conflicts"
REMARKS = "remarks"
MODEL = "model"
OFFSET = "offset"
TOTAL_TIME = "total_time"

WMAXCDCL_HEADERS = f"{FILE_NAME}; {OPTIMIZATION_TIME}; {OPTIMAL_OBJ}; {TOTAL_TIME}; {REMARKS};"


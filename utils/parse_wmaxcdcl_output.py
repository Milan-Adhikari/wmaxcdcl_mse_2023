import re

def parse_output(output):
    # Regular expression to find 'o <optimum_value>' followed by 's OPTIMUM FOUND'
    # match = re.search(r'o\s+(\d+)\s+s OPTIMUM FOUND', output)
    optimum_found_match = re.search(r's\s+(OPTIMUM FOUND)', output)
    if optimum_found_match:
        optimal_value_match = re.search(r'o\s+(\d+)', output)
        if optimal_value_match:
            optimum_value = int(optimal_value_match.group(1))
            return optimum_value
        else:
            return None
    else:
        return None
    

def parse_wmaxcdcl_output(output):
    # solved by scip
    scip_solved_match = re.search(r'Solved by SCIP', output)
    wmaxcdcl_match = re.search(r'This is WMaxCDCL', output)
    optimal_value = "None"
    time = -1

    if scip_solved_match:
        if wmaxcdcl_match:
            optimum_found_match = re.search(r's\s+(OPTIMUM FOUND)', output)
            if optimum_found_match:
                optimum_value_match = re.search(r'optimal:\s+(\d+)', output)
                if optimum_value_match:
                    optimum_value = int(optimum_value_match.group(1))
                    optimal_value = optimum_value
                wallclock_time_match = re.search(r'c\s+time\s+(\d+(\.\d+)?)', output)
                if wallclock_time_match:
                    wallclock_time = float(wallclock_time_match.group(1))
                    time = wallclock_time
        else:
            optimal_value = None
            time = None
            optimum_found_match = re.search(r's\s+(OPTIMUM FOUND)', output)
            if optimum_found_match:
                optimal_value_match = re.search(r'o\s+(\d+)', output)
                if optimal_value_match:
                    optimum_value = int(optimal_value_match.group(1))
                    optimal_value = optimum_value
                wallclock_time_match = re.search(r'WCTIME=(\d+(\.\d+)?)', output)
                if wallclock_time_match:
                    wallclock_time = float(wallclock_time_match.group(1))
                    time = wallclock_time
        
    return {
        "optimal_value": optimal_value,
        "time": time
    }
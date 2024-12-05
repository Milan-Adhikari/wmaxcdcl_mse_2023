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
    maxhs_match = re.search(r'Solved by MaxHS', output)
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
    elif maxhs_match:
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
    else:
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
    
# test = '''
# c [MSE2023] -- begin -- [MSE2023]
# 599.69/600.01	c Stop SCIP
# 623.29/623.66	c Solved by MaxHS
# 623.29/623.67	c MaxHS 5.0.0
# 623.29/623.67	c Instance: maxsat.wcnf
# 623.29/623.67	c Instance: maxsat.wcnf
# 623.29/623.67	c #vars: 250
# 623.29/623.67	c #Clauses: 1272
# 623.29/623.67	c Total Soft Cls Wt: 302
# 623.29/623.67	c HARD: #Clauses = 1065, Total Lits = 3195, Ave Len = 3.0000 #units = 0
# 623.29/623.67	c SOFT: #Clauses = 207, Total Lits = 207, Ave Len = 1.0000
# 623.29/623.67	c Total Soft Clause Weight (+ basecost): 302 (+ 0 from 0 false softs)
# 623.29/623.67	c SOFT%: 16.2736%
# 623.29/623.67	c #distinct weights: 2, mean = 1.4589, std. dev = 0.4995, min = 1, max = 2
# 623.29/623.67	c Parse time: 0.0003 secs.
# 623.29/623.67	c Wcnf Space Required: 0.0000MB
# 623.29/623.67	c ================================
# 623.29/623.67	c WCNF: found 0 pure literals
# 623.29/623.67	c Solved by solve_wt_lsu (fine).
# 623.29/623.67	o 123
# 623.29/623.67	s OPTIMUM FOUND
# 623.29/623.67	v 1111101111010110000010000000000000001001000101001010101110001100111001100111001110010000011111000001011110110000010000001000011010000011100001110110111111001011110010001100101101101011110101010101000010011010110110010000101101010001010111110111101101
# 623.29/623.67	c Solved: Number of falsified softs = 84
# 623.29/623.67	c SAT: #calls 751
# 623.29/623.67	c SAT: Total time 23.6008
# 623.29/623.67	c SAT: #muser calls 71 (100.0000 % successful)
# 623.29/623.67	c SAT: Minimize time 23.5461 (99.7682%)
# 623.29/623.67	c SAT: Avg constraint minimization 10.1690
# 623.29/623.67	c SAT: number of variables substituted 0
# 623.29/623.67	c GREEDY: #calls 0
# 623.29/623.67	c GREEDY: Total time 0.0000
# 623.29/623.67	c MEM MB: 49.0000
# 623.29/623.67	c CPU: 23.6075
# # WCTIME: wall clock time in seconds
# WCTIME=623.672
# # CPUTIME: CPU time in seconds
# CPUTIME=623.373
# # USERTIME: CPU time spent in user mode in seconds
# USERTIME=623.114
# # SYSTEMTIME: CPU time spent in system mode in seconds
# SYSTEMTIME=0.259085
# # CPUUSAGE: CPUTIME/WCTIME in percent
# CPUUSAGE=99.9521
# # MAXVM: maximum virtual memory used in KiB
# MAXVM=217616
# c [MSE2023] -- end -- [MSE2023]
# '''

# output = parse_wmaxcdcl_output(test)
# print(output)
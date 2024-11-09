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
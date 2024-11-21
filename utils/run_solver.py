import subprocess

def run_solver(binary_path, benchmark_path):
    # create a list of command line arguments
    cmd = [binary_path, benchmark_path]
    try:
        # run the command and capture the output, timeout after 500 seconds
        result = subprocess.run(
            cmd,
            text=True,
            capture_output=True,
            # timeout=500
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        # return the output of the command if it failed
        return e.output
    except Exception as e:
        # return the exception as a string if the command failed
        return str(e)
    except subprocess.TimeoutExpired as e:
        # return the exception as a string if the command failed
        return str(e)
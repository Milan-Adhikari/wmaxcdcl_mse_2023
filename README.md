This repository consists of code to run the WMaxCDCL MAXSAT solver on the exact weighted benchmark problems from [MAXSAT Evaluations 2023 (MSE 2023)](https://maxsat-evaluations.github.io/2023/).<br>
The program runs the solver on the benchmark instances, and creates output for each instance. <br> There is a combined output csv file, which consists optimum values of all the instances, while there are individual
output files for each of the instances as well.
<br>
This program was necessary for me because, WMaxCDCL has 3 binaries, that it uses based on the problem instance.<br>
It uses SCIP solver, MAXHS solver, and a WMaxCDCL static solver and uses fallback methods to change the solver to optimize the benchmark instance.

# Running the code
> I needed the results for some research work that I have been doing. So, there is a bash script run.sh that runs the wmaxcdcl_mse23.sh bash script, which in turn invokes the main.py
> If you want to run it in the local machine, you can simply run the main.py program.
>
>> Steps
>> 1. Go to the MSE 2023 github page [here](https://maxsat-evaluations.github.io/2023/descriptions.html) and download the WMaxCDCL codebase.
>> 2. Unzip the file, and copy the entire contents of the bin folder. bin folder contains all their binaries and bash scripts that we will use.
>> 3. Paste the content in the main working directory, where main.py is located
>> 4. Go to the MSE 2023 github page [here](https://maxsat-evaluations.github.io/2023/benchmarks.html) and download the exact weighted benchmarks.
>> 5. Unzip the folder, but leave the individual instances zipped, as the solver binary accepts .xz compressed files.
>> 6. Run the main.py script, or the run.sh bash script
>
>Keep in mind that the folder name for the benchmarks might need to be changed.

# WMaxCDCL
> WMaxCDCL is a MAXSAT solver which performed very well in the MSE 2023.
> > The binary for the solver is available freely in [here](https://maxsat-evaluations.github.io/2023/descriptions.html).
>

> Benchmark
> The Benchmark instances used in here are the Exact Weighted Benchmarks from MSE 2023.
> > The benchmarks are freely available in [here](https://maxsat-evaluations.github.io/2023/benchmarks.html).
>

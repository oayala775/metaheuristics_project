# Metaheuristics project

## Import environment using conda
In the main path of the project theres a `environment.yml` file, it is intended to import all the packages and python specific version that allowed this program to run right away, in order to do so just execute `conda env create -f environment.yml`.

In order to check whether the importing process was successful or not just execute `conda env list` and search for `proyecto_algoritmos` environment, if it shows it means that the importing process was successful.
### In case of error
We've added a bash script to install all dependencies if you have a UNIX system, to execute it do the following:
- Give execution permition with `chmod +x dependencies.sh`
- Execute the command with `./dependencies.sh`
# Performance metrics
The project is intended to be measured using the following metrics:
- PSNR
- MSE
- STD
- SSIM
- FSIM

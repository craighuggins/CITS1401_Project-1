# CITS1401_Project-1
Computing the World Happiness Index from the 2018 World Happiness Report

Details of the 2018 report can be found here:
https://worldhappiness.report/ed/2018/
https://en.wikipedia.org/wiki/World_Happiness_Report

The underlying data can be found in the files:
WHR2018Chapter2_reduced.csv
WHR2018Chapter2_reduced_sample.csv

Running the program:
- start by calling the main() function

Inputs:
- provide 3 inputs at the prompts:
    - the name of the input data file
    - the name of the metric to be computed. 
      Allowed values are "min", "mean", "median", "harmonic_mean"
    - the name of the action to be performed. 
      Allowed values are "list", which lists the countries in descending order of the computed metric, or "correlation" which uses the Spearman rank correlation coefficient to compute the correlation between ranks according to the computed metric and the ranks according to the Life Ladder score.
  
Output:
The output, printed to standard output, will be either a listing of the countries in descending order based on the computed metric, or a statement containing the correlation value

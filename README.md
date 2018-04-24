#############################################################################
# Project : machine-learning-assignment-1                                   #
# Autor : Simon Bonnaud - Arthur Chevallier - Anaïs Pignet - Eliott Vincent #
# Subject : data-mining														#
#############################################################################

#################### DESCRIPTION ####################
This program is designed to load a set of data from a 
CSV file. The code then generates:
* The Data Quality Report for continuous features (./data/A-DQR-CategoricalFeatures.csv)
* The Data Quality Report for categorical features (./data/A-DQR-ContinuousFeatures.csv)
* The graphs (histograms or bar plots) for each continuous feature (./data/FEATURENAME-histogram.html or ./data/FEATURENAME-bar-plot.html)
* The graphs (bar plots) for each categorical feature (./data/FEATURENAME-bar-plot.html)

#################### COMPOSITION ####################
Files ->
* .gitignore: a git ignore file for versioning purpose
* A-GenerateDQR.py: the main file
* LICENSE: the software license to tell others what they can and can't do with our source code
* README.md: the present file
Folders ->
* ./data/: the folder containing the data set (DataSet.csv) and the generated files

################### ENVIRONNEMENT ###################
Python: 3.6.4
Modules: collections, pandas, numpy and plotly

##################### EXECUTION #####################
command: python A-GenerateDQR.py

################# OUTPUTS FORMATS ###################
Data Quality Reports: CSV format
Histograms and bar plots: HTML format

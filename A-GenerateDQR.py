__author__ = "Eliott Vincent, Arthur Chevallier, Anais Pignet, Simon Bonneaud"

__license__ = "MIT"
__version__ = "0.1"

#================================================================================
# modules
#================================================================================
import pandas as pd
import numpy as np


#================================================================================
# properties
#================================================================================
continuousFeatures = ['age', 'fnlwgt', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']
categoricalFeatures = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country', 'target']
continuousStatistics = ['feature_name', 'count', 'miss_percentage', 'card', 'minimum', 'first_quartile', 'mean', 'median', 'third_quartile', 'maximum', 'std_dev']
categoricalStatistics = ['feature_name', 'count', 'miss_percentage', 'card', 'mode', 'mode_frequency', 'mode_percentage', 'second_mode', 'second_mode_frequency', 'second_mode_percentage']
dataPath = './data/'
teamName = 'A'


def main():
	df = load_dataframe('DataSet.csv')

	continuousDf = getContinuousDf(df)
	categoricalDf = getCategorical(df)

	continuousReport = generateContinuousReport(continuousDf)
	categoricalReport = generateCategoricalReport(categoricalDf)
	
	write_dataframe(continuousReport, teamName + '-DQR-ContinuousFeatures.csv')
	write_dataframe(categoricalReport, teamName + '-DQR-CategoricalFeatures.csv')




#  ██╗███╗   ██╗██████╗ ██╗   ██╗████████╗    ██████╗ ██╗   ██╗████████╗██████╗ ██╗   ██╗████████╗
#  ██║████╗  ██║██╔══██╗██║   ██║╚══██╔══╝   ██╔═══██╗██║   ██║╚══██╔══╝██╔══██╗██║   ██║╚══██╔══╝
#  ██║██╔██╗ ██║██████╔╝██║   ██║   ██║█████╗██║   ██║██║   ██║   ██║   ██████╔╝██║   ██║   ██║   
#  ██║██║╚██╗██║██╔═══╝ ██║   ██║   ██║╚════╝██║   ██║██║   ██║   ██║   ██╔═══╝ ██║   ██║   ██║   
#  ██║██║ ╚████║██║     ╚██████╔╝   ██║      ╚██████╔╝╚██████╔╝   ██║   ██║     ╚██████╔╝   ██║   
#  ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝    ╚═╝       ╚═════╝  ╚═════╝    ╚═╝   ╚═╝      ╚═════╝    ╚═╝   


def load_dataframe(fileName):
	path = dataPath + fileName
	return pd.read_csv(path, header=0, index_col='id', na_values=['?'])

def write_dataframe(df, fileName):
	path = dataPath + fileName
	df.to_csv(path)

def getContinuousDf(df):
	return df.drop(categoricalFeatures, axis=1)

def getCategorical(df):
	return df.drop(continuousFeatures, axis=1)




#  ███████╗████████╗ █████╗ ████████╗██╗███████╗████████╗██╗ ██████╗███████╗
#  ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║██╔════╝╚══██╔══╝██║██╔════╝██╔════╝
#  ███████╗   ██║   ███████║   ██║   ██║███████╗   ██║   ██║██║     ███████╗
#  ╚════██║   ██║   ██╔══██║   ██║   ██║╚════██║   ██║   ██║██║     ╚════██║
#  ███████║   ██║   ██║  ██║   ██║   ██║███████║   ██║   ██║╚██████╗███████║
#  ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝╚══════╝   ╚═╝   ╚═╝ ╚═════╝╚══════╝


def computeContinuousStatistics(df):
	"""computeContinuousStatistics
	Computes statistics for continuous features.

    Input:
    df -- DataFrame to use
    
	Output:
	{} -- a dictionary containing the statistics
    """

	# init. values
	count=0
	miss=0
	valuesTab=[]
	card=0

	# computing statistics
	for values in df:
		count+=1
		if values==' ?' or values=='?':
			miss+=1
		if values not in valuesTab:
			valuesTab.append(values)
			card+=1

	# returning final statistics
	return {
		'count': count,
		'miss_percentage': (miss/count)*100,
		'card': card,
		'minimum': df.min(),
		'first_quartile': df.quantile([0.25][0]),
		'mean': df.mean(),
		'median': df.median(),
		'third_quartile': df.quantile([0.75][0]),
		'maximum': df.max(),
		'std_dev': df.std()
	}


def computeCategoricalStatistics(df):
	"""computeCategoricalStatistics
	Computes statistics for categorical features.

    Input:
    df -- DataFrame to use
    
	Output:
	{} -- a dictionary containing the statistics
    """

	# init. values
	count=0
	miss=0
	valuesTab=[]
	card=0

	# computing statistics
	for values in df:
		count+=1
		if values==' ?' or values=='?':
			miss+=1
		if values not in valuesTab:
			valuesTab.append(values)
			card+=1

	# returning final statistics
	return {
		'count': card,
		'miss_percentage': card,
		'card': card,
		'mode': card,
		'mode_frequency': card,
		'mode_percentage': card,
		'second_mode': card,
		'second_mode_frequency': card,
		'second_mode_percentage': card
	}




#  ██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗███████╗
#  ██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝
#  ██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   ███████╗
#  ██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   ╚════██║
#  ██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   ███████║
#  ╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝


def generateContinuousReport(continuousDf):
	"""generateContinuousReport
	Generates a report of continuous features statistics from a dataframe.

    Input:
    continuousDf -- DataFrame to use
    
	Output:
	generateReport() -- output of the generateReport() method
    """
	return generateReport(continuousDf, continuousStatistics, computeContinuousStatistics)


def generateCategoricalReport(categoricalDf):
	"""generateCategoricalReport
	Generates a report of categorical features statistics from a dataframe.

    Input:
    categoricalDf -- DataFrame to use
    
	Output:
	generateReport() -- output of the generateReport() method
    """
	return generateReport(categoricalDf, categoricalStatistics, computeCategoricalStatistics)


def generateReport(dataFrame, statisticsNames, computeFunction):
	"""generateReport
	Generates a report from a dataframe.

    Input:
    dataFrame -- DataFrame to use
    statisticsNames -- statistics to compute
    computeFunction -- method to use to compute the mesures

	Output:
	statisticsDf -- DataFrame containing the statistics
    """

	# 1st step: create an empty dataframe with the statistics names as columns
	statisticsDf = pd.DataFrame(columns=statisticsNames)
	statisticsDf.set_index('feature_name', inplace=True)

	# 2nd step: loop over each feature
	for featureName in dataFrame:
		
		# gathering all values for the current feature
		featureValues = dataFrame[featureName]

		# computing statistics
		statisticsDict = computeFunction(featureValues)

		# creating a serie with those statistics
		statisticsSeries = pd.Series(statisticsDict, name=featureName)

		# adding the serie to the final dataframe
		statisticsDf = statisticsDf.append(statisticsSeries)

	# 3rd step: return the completed dataframe
	return statisticsDf

main()
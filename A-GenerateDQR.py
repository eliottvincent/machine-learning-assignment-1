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
	#print(len(df['workclass'])-df['workclass'].count())

	continuousReport = generateContinuousReport(df)
	print(continuousReport)
	categoricalReport = generateCategoricalReport(df)
	print(categoricalReport)
	
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
	return pd.read_csv(path, header=0, index_col='id', na_values=[' ?'])

def write_dataframe(df, fileName):
	path = dataPath + fileName
	df.to_csv(path)




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

	# returning statistics
	return {
		'count': len(df),
		'miss_percentage': ((len(df)-df.count())*100)/len(df),
		'card': df.nunique(),
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
	
	# find modes
	newDf = df.copy()
	firstMode = newDf.mode()[0]
	firstModeFrequency = newDf.describe()[3]
	firstModePercentage = (firstModeFrequency/count)*100
	
	newDf = newDf[newDf != firstMode]
	secondMode = newDf.mode()[0]
	secondModeFrequency = newDf.describe()[3]
	secondModePercentage = (secondModeFrequency/count)*100

	# returning final statistics
	return {
		'count': len(df),
		'miss_percentage': ((len(df)-df.count())*100)/len(df),
		'card': df.nunique(),
		'mode': firstMode,
		'mode_frequency': firstModeFrequency,
		'mode_percentage': firstModePercentage,
		'second_mode': secondMode,
		'second_mode_frequency': secondModeFrequency,
		'second_mode_percentage': secondModePercentage
	}


#  ██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗███████╗
#  ██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝
#  ██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   ███████╗
#  ██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   ╚════██║
#  ██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   ███████║
#  ╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝


def generateContinuousReport(df):
	"""generateContinuousReport
	Generates a report of continuous features statistics from a dataframe.

    Input:
    df -- DataFrame to use
    
	Output:
	generateReport() -- output of the generateReport() method
    """
	return generateReport(df, continuousFeatures, continuousStatistics, computeContinuousStatistics)


def generateCategoricalReport(df):
	"""generateCategoricalReport
	Generates a report of categorical features statistics from a dataframe.

    Input:
    df -- DataFrame to use
    
	Output:
	generateReport() -- output of the generateReport() method
    """
	return generateReport(df, categoricalFeatures, categoricalStatistics, computeCategoricalStatistics)


def generateReport(dataFrame, featuresNames, statisticsNames, computeFunction):
	"""generateReport
	Generates a report from a dataframe.

    Input:
    dataFrame -- DataFrame to use
    featuresNames -- features to analyse
    statisticsNames -- statistics to compute
    computeFunction -- method to use to compute the mesures

	Output:
	statisticsDf -- DataFrame containing the statistics
    """

	# 1st step: create an empty dataframe with the statistics names as columns
	statisticsDf = pd.DataFrame(columns=statisticsNames)
	statisticsDf.set_index('feature_name', inplace=True)

	# 2nd step: loop over each feature
	for featureName in featuresNames:
		
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

# Lancement du programme
if __name__ == '__main__':
	main()
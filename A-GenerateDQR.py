__author__ = "Eliott Vincent, Arthur Chevallier, Anaïs Pignet, Simon Bonnaud"

__license__ = "MIT"
__version__ = "0.1"

#================================================================================
# modules
#================================================================================
import pandas as pd
import numpy as np
import plotly
from plotly.graph_objs import Scatter, Layout
import plotly.graph_objs as go
from collections import Counter


#================================================================================
# properties
#================================================================================
continuousFeatures = ['age', 'fnlwgt', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']
categoricalFeatures = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country', 'target']
continuousStatistics = ['FEATURENAME', 'count', 'miss_percentage', 'card', 'minimum', 'first_quartile', 'mean', 'median', 'third_quartile', 'maximum', 'std_dev']
categoricalStatistics = ['FEATURENAME', 'count', 'miss_percentage', 'card', 'mode', 'mode_frequency', 'mode_percentage', 'second_mode', 'second_mode_frequency', 'second_mode_percentage']
dataPath = './data/'
teamName = 'A'


def main():
	df = load_dataframe('DataSet.csv')
	#print(len(df['workclass'])-df['workclass'].count())

	continuousDf = getContinuousDf(df)
	categoricalDf = getCategorical(df)

	continuousReport = generateContinuousReport(continuousDf)
	categoricalReport = generateCategoricalReport(categoricalDf)
	
	write_dataframe(continuousReport, teamName + '-DQR-ContinuousFeatures.csv')
	write_dataframe(categoricalReport, teamName + '-DQR-CategoricalFeatures.csv')

	generateContinuousGraphs(continuousDf, continuousReport)
	generateCategoricalGraphs(categoricalDf)




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
	statisticsDf.set_index('FEATURENAME', inplace=True)

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

# Lancement du programme
if __name__ == '__main__':
	main()



#   ██████╗ ██████╗  █████╗ ██████╗ ██╗  ██╗███████╗
#  ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██║  ██║██╔════╝
#  ██║  ███╗██████╔╝███████║██████╔╝███████║███████╗
#  ██║   ██║██╔══██╗██╔══██║██╔═══╝ ██╔══██║╚════██║
#  ╚██████╔╝██║  ██║██║  ██║██║     ██║  ██║███████║
#   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝


def drawHistogramFromFeature(featureName, featureValues):
	data = [go.Histogram(x=featureValues)]
	path = dataPath + featureName + '-histogram.html'
	plotly.offline.plot(data, filename=path, auto_open=False)

def drawBarPlotFromFeature(featureName, featureValues):
	
	occurrences = Counter(featureValues)
	x_axis = []
	y_axis = []
	for occurrence in occurrences:
		x_axis.append(occurrence)
		y_axis.append(occurrences[occurrence])

	data = [go.Bar(x=x_axis, y=y_axis)]

	path = dataPath + featureName + '-bar-plot.html'
	plotly.offline.plot(data, filename=path, auto_open=False)

def generateContinuousGraphs(continuousDf, continuousReport):

	for featureName in continuousDf:

		currentFeatureReport = continuousReport.loc[featureName]
		currentCard = currentFeatureReport['card']

		# if the continuous feature has a low cardinality (< 10), we draw a bar plot
		if currentCard < 10:
			drawBarPlotFromFeature(featureName, continuousDf[featureName])
		# else we draw an histogram
		else:
			drawHistogramFromFeature(featureName, continuousDf[featureName])

def generateCategoricalGraphs(categoricalDf):
	
	for featureName in categoricalDf:
		drawBarPlotFromFeature(featureName, categoricalDf[featureName])


main()
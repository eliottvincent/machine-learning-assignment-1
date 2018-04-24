import pandas as pd
import numpy as np

continuousFeatures = ['age', 'fnlwgt', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']
categoricalFeatures = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country', 'target']
continuousMeasures = ['feature_name', 'count', 'miss_percentage', 'card', 'minimum', 'first_quartile', 'mean', 'median', 'third_quartile', 'maximum', 'std_dev']
categoricalMeasures = ['feature_name', 'count', 'miss_percentage', 'card', 'mode', 'mode_frequency', 'mode_percentage', 'second_mode', 'second_mode_frequency', 'second_mode_percentage']

# main
def main():
	df = load_dataframe('./data/DataSet.csv')
	write_dataframe('./data/Test.csv', df)
	continuousReport = generateContinuousReport(df)
	print(continuousReport)




#  ██╗███╗   ██╗██████╗ ██╗   ██╗████████╗    ██████╗ ██╗   ██╗████████╗██████╗ ██╗   ██╗████████╗
#  ██║████╗  ██║██╔══██╗██║   ██║╚══██╔══╝   ██╔═══██╗██║   ██║╚══██╔══╝██╔══██╗██║   ██║╚══██╔══╝
#  ██║██╔██╗ ██║██████╔╝██║   ██║   ██║█████╗██║   ██║██║   ██║   ██║   ██████╔╝██║   ██║   ██║   
#  ██║██║╚██╗██║██╔═══╝ ██║   ██║   ██║╚════╝██║   ██║██║   ██║   ██║   ██╔═══╝ ██║   ██║   ██║   
#  ██║██║ ╚████║██║     ╚██████╔╝   ██║      ╚██████╔╝╚██████╔╝   ██║   ██║     ╚██████╔╝   ██║   
#  ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝    ╚═╝       ╚═════╝  ╚═════╝    ╚═╝   ╚═╝      ╚═════╝    ╚═╝   


def load_dataframe(path):
	return pd.read_csv(path, header=0, index_col='id', na_values=['?'])

# write_dataframe
def write_dataframe(path,df):
	df.to_csv(path)




#  ███╗   ███╗███████╗ █████╗ ███████╗██╗   ██╗██████╗ ███████╗███████╗
#  ████╗ ████║██╔════╝██╔══██╗██╔════╝██║   ██║██╔══██╗██╔════╝██╔════╝
#  ██╔████╔██║█████╗  ███████║███████╗██║   ██║██████╔╝█████╗  ███████╗
#  ██║╚██╔╝██║██╔══╝  ██╔══██║╚════██║██║   ██║██╔══██╗██╔══╝  ╚════██║
#  ██║ ╚═╝ ██║███████╗██║  ██║███████║╚██████╔╝██║  ██║███████╗███████║
#  ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝


def computeContinuousMeasures(df):
	"""computeContinuousMeasures
	Computes measures for continuous features.

    Input:
    df -- DataFrame to use
    
	Output:
	{} -- a dictionary containing the measures
    """

	# init. values
	count=0
	miss=0
	valuesTab=[]
	card=0

	# computing measures
	for values in df:
		count+=1
		if values==' ?' or values=='?':
			miss+=1
		if values not in valuesTab:
			valuesTab.append(values)
			card+=1

	# returning final measures
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


def computeCategoricalMeasures(df):
	"""computeCategoricalMeasures
	Computes measures for categorical features.

    Input:
    df -- DataFrame to use
    
	Output:
	{} -- a dictionary containing the measures
    """

	# init. values
	count=0
	miss=0
	valuesTab=[]
	card=0

	# computing measures
	for values in df:
		count+=1
		if values==' ?' or values=='?':
			miss+=1
		if values not in valuesTab:
			valuesTab.append(values)
			card+=1

	# returning final measures
	return {
		'count': count,
		'miss_percentage': (miss/count)*100,
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


def generateContinuousReport(df):
	"""generateContinuousReport
	Generates a report of continuous features measures from a dataframe.

    Input:
    df -- DataFrame to use
    
	Output:
	generateReport() -- output of the generateReport() method
    """
	return generateReport(df, continuousFeatures, continuousMeasures, computeContinuousMeasures)


def generateCategoricalReport(df):
	"""generateCategoricalReport
	Generates a report of categorical features measures from a dataframe.

    Input:
    df -- DataFrame to use
    
	Output:
	generateReport() -- output of the generateReport() method
    """
	return generateReport(df, categoricalFeatures, categoricalMeasures, computeCategoricalMeasures)


def generateReport(dataFrame, featuresNames, measuresNames, computeFunction):
	"""generateReport
	Generates a report from a dataframe.

    Input:
    dataFrame -- DataFrame to use
    featuresNames -- features to analyse
    measuresNames -- measures to compute
    computeFunction -- method to use to compute the mesures

	Output:
	measuresDf -- DataFrame containing the measures
    """

	# 1st step: create an empty dataframe with the measures names as columns
	measuresDf = pd.DataFrame(columns=measuresNames)
	measuresDf.set_index('feature_name', inplace=True)

	# 2nd step: loop over each feature
	for featureName in featuresNames:
		
		# gathering all values for the current feature
		featureValues = dataFrame[featureName]

		# computing measures
		measuresDict = computeFunction(featureValues)

		# creating a serie with those measures
		measuresSeries = pd.Series(measuresDict, name=featureName)

		# adding the serie to the final dataframe
		measuresDf = measuresDf.append(measuresSeries)

	# 3rd step: return the completed dataframe
	return measuresDf

main()
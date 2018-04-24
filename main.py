import pandas as pd
import numpy as np

continuousFeatures = ['age', 'fnlwgt', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']
categoricalFeatures = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country', 'target']
continuousMeasuresNames = ['feature_name', 'count', 'miss_percentage', 'card', 'minimum', 'first_quartile', 'mean', 'median', 'third_quartile', 'maximum', 'std_dev']
categoricalMeasuresNames = ['feature_name', 'count', 'miss_percentage', 'card', 'mode', 'mode_frequency', 'mode_percentage', 'second_mode', 'second_mode_frequency', 'second_mode_percentage']

# main
def main():
	df = load_dataframe('./data/DataSet.csv')
	write_dataframe('./data/Test.csv', df)
	continuousReport = generateContinuousReport(df)
	print(continuousReport)

# load_dataFrame
def load_dataframe(path):
	return pd.read_csv(path, header=0, index_col='id', na_values=['?'])

# write_dataframe
def write_dataframe(path,df):
	df.to_csv(path)

# computeContinuousMeasures
def computeContinuousMeasures(df):
	
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

# generateContinuousReport
def generateContinuousReport(df):
	
	# 1st step: create a new dataframe from continuousFeatures
	continuousDf = df.drop(categoricalFeatures, axis=1)

	# 2nd step: create an empty dataframe with the continuous measures names as columns
	measuresDf = pd.DataFrame(columns=continuousMeasuresNames)
	measuresDf.set_index('feature_name', inplace=True)

	# 3rd step: loop over the continuous dataframe
	for columnName in continuousDf:
		
		# gathering all values for the current column
		columnValues = df[columnName]

		# computing each measure (count, miss, card, etc.)
		measures = computeContinuousMeasures(columnValues)

		# creating a serie with those measures
		measuresSeries = pd.Series(measures, name=columnName)

		# adding the serie to the final dataframe
		measuresDf = measuresDf.append(measuresSeries)

	# 4th step: setting feature_name as the index
	return measuresDf


def generateCategoricalReport(df):
	# 1st step: create a new dataframe from continuousFeatures
	categoricalDf = df.drop(continuousFeatures, axis=1)

	# 2nd step: create an empty dataframe for the continuous measures
	measuresDf = pd.DataFrame(columns=categoricalMeasuresNames)
	measuresDf.set_index('feature_name', inplace=True)

	# 3rd step: loop over the new dataframe
	for column in categoricalDf:
		
		# gathering all values for the current column
		columnValues = df[column]

		# computing each measure (count, miss, card, etc.)
		measures = computeCategoricalMeasures(columnValues)

		# creating a dataframe with the current column's measures
		currentDf = pd.DataFrame(np.array([measures]), columns=categoricalMeasuresNames)
		currentDf.set_index('feature_name', inplace=True)

		# merging into the final dataframe
		measuresDf = pd.concat([measuresDf, currentDf], axis=0)

	# 4th step: setting feature_name as the index
	return measuresDf

main()
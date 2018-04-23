import pandas as pd
import numpy as np

continuousFeatures = ['age', 'fnlwgt', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']
categoricalFeatures = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country', 'target']
continuousMeasuresNames = ['feature_name', 'count', 'miss_percentage', 'card', 'minimum', 'first_quartile', 'mean', 'median', 'third_quartile', 'maximum', 'std_dev']
categoricalMeasuresNames = ['feature_name', 'count', 'miss_percentage', 'card', 'mode', 'mode_frequency', 'mode_percentage', 'second_mode', 'second_mode_frequency', 'second_mode_percentage']

# main
def main():
	df = load_dataframe('./data/DataSet.csv')
	# print(df)
	write_dataframe('./data/Test.csv',df)
	continuousReport = generateContinuousReport(df)
	print(continuousReport)

# load_dataFrame
def load_dataframe(path):
	return pd.read_csv(path, header=0, index_col='id', na_values=['?'])

# write_dataframe
def write_dataframe(path,dataframe):
	dataframe.to_csv(path)

# 
def generateContinuousReport(df):
	
	# 1st step: create a new dataframe from continuousFeatures
	continuousDf = df.drop(categoricalFeatures, axis=1)

	# 2nd step: create an empty dataframe for the continuous measures
	measuresDf = pd.DataFrame(columns=continuousMeasuresNames)
	measuresDf.set_index('feature_name', inplace=True)

	# print(measuresDf)
	# 3rd step: loop over the new dataframe
	for column in continuousDf:
		
		# gathering all values for the current column
		columnValues = df[column]

		# computing each measure (count, miss, card, etc.)
		measures = computeContinuousMeasures(columnValues)

		# creating a dataframe with the current column's measures
		currentDf = pd.DataFrame(np.array([measures]), columns=continuousMeasuresNames)
		currentDf.set_index('feature_name', inplace=True)

		# merging into the final dataframe
		measuresDf = pd.concat([measuresDf, currentDf], axis=0)

	# 4th step: setting feature_name as the index
	return measuresDf



def generateCategoricalReport(df):
	# 1st step: create a new dataframe from categoricalFeatures
	categoricalDf = df.drop(continuousFeatures, axis=1)

	# 2nd step: create a dataframe for the categorical measures
	measuresDf = pd.DataFrame.from_records([], categoricalMeasuresNames)

	# 3rd step: loop over the new dataframe
		# computing each measure (count, miss, card, etc.) (with Arthur's methods)
		# adding the row to the global result dataframe

	# 4th step: return the final dataframe
	return measuresDf

def computeContinuousMeasures(values):
	return ['test', 'test', 'test', 'test', 'test', 'test', 'test', 'test', 'test', 'test', 'test']


main()
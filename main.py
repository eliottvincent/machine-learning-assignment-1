import pandas as pd

continuousFeatures = ['age', 'fnlwgt', 'education-num', 'capital-gain', 'capital-gain', 'hours-per-week']
categoricalFeatures = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country']
continuousMeasures = ['feature_name', 'count', 'miss_percentage', 'card', 'min', 'first_quartile', 'mean', 'median', 'third_quartile', 'max', 'std_dev']
categoricalMeasures = ['feature_name', 'count', 'miss_percentage', 'card', 'mode', 'mode_frequency', 'mode_percentage', 'second_mode', 'second_mode_frequency', 'second_mode_percentage']

# main
def main():
	df = load_dataframe('./data/DataSet.csv')
	print(df)
	write_dataframe('./data/Test.csv',df)
	generateContinuousReport(df)

# load_dataFrame
def load_dataframe(path):
	return pd.read_csv(path, header=0, index_col='id', na_values=['?'])

# write_dataframe
def write_dataframe(path,dataframe):
	dataframe.to_csv(path)

# 
def generateContinuousReport(df):
	
	# 1st step: create a new dataframe from continuousFeatures

	# 2nd step: create an empty dataframe for the continuous measures
	continuousDf = pd.DataFrame.from_records([], continuousMeasures)

	print(continuousDf)
	# 3rd step: loop over the new dataframe
		# computing each measure (count, miss, card, etc.) (with Arthur's methods)
		# adding the row to the global result dataframe
		

	# 4th step: return the final dataframe
	return continuousDf



def generateCategoricalReport(df):
	# 1st step: create a new dataframe from categoricalFeatures

	# 2nd step: create a dataframe for the categorical measures
	categoricalDf = pd.DataFrame.from_records([], categoricalMeasures)

	# 3rd step: loop over the new dataframe
		# computing each measure (count, miss, card, etc.) (with Arthur's methods)
		# adding the row to the global result dataframe

	# 4th step: return the final dataframe
	return df
main()
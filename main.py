import pandas as pd

continuousFeatures = ['age', 'fnlwgt', 'education-num', 'capital-gain', 'capital-gain', 'hours-per-week']
categoricalFeatures = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country']
continuousMeasures = ['feature_name', 'count', 'miss_percentage', 'card', 'min', 'first_quartile', 'mean', 'median', 'third_quartile', 'max', 'std_dev'];
categoricalMeasures = ['feature_name', 'count', 'miss_percentage', 'card', 'mode', 'mode_frequency', 'mode_percentage', 'second_mode', 'second_mode_frequency', 'second_mode_percentage'];

# main
def main():
	df = load_dataframe('./data/DataSet.csv')
	print(df)
	write_dataframe('./data/Test.csv',df)

# load_dataFrame
def load_dataframe(path):
	return pd.read_csv(path, header=0, index_col='id', na_values=['?'])

# write_dataframe
def write_dataframe(path,dataframe):
	dataframe.to_csv(path)

# num_missing
def num_missing(x):
  return sum(x.isnull())


main()
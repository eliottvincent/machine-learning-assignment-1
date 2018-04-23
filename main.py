import pandas as pd

# main
def main():
	df = load_dataframe('./data/DataSet.csv')
	print(df)
	write_dataframe('./data/Test.csv',df)


# load_DataFrame
def load_dataframe(path):
	return pd.read_csv(path, header=0, index_col='id')

# write_dataframe
def write_dataframe(path,dataframe):
	dataframe.to_csv(path)

# num_missing
def num_missing(x):
  return sum(x.isnull())


main()
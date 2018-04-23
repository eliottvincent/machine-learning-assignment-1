import pandas as pd

# main
def main():
	df = load_dataframe('./data/DataSet.csv')
	print(df)


# load_DataFrame
def load_dataframe(path):
	return pd.read_csv(path, header=None)


# num_missing
def num_missing(x):
  return sum(x.isnull())


main()
import pandas as pd

# main
def main():
	df = load_dataframe('./data/DataSet.csv')
	# print(df)
	# write_dataframe('./data/Test.csv',df)
	test=computeContinuousMeasures(df['age'])
	print(test)

# load_DataFrame
def load_dataframe(path):
	return pd.read_csv(path, header=0, index_col='id')

# write_dataframe
def write_dataframe(path,df):
	df.to_csv(path)

# computeContinuousMeasures
def computeContinuousMeasures(df):
	count=0
	miss=0
	valuesTab=[]
	card=0
	minimum=0
	quart1=0
	for values in df:
		count+=1
		if values==' ?' or values=='?':
			miss+=1
		if values not in valuesTab:
			valuesTab.append(values)
			card+=1
	return {'count': count, 'miss': (miss/count)*100, 'card': card, 'min': df.min(), 'quart1': df.quantile([0.25][0]), 'mean': df.mean(), 'median': df.median(),'quart3': df.quantile([0.75][0]), 'max': df.max(), 'StdDev': df.std()}

# num_missing
def num_missing(x):
	return sum(x.isnull())


main()
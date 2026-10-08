import pandas as pd

data = pd.read_csv('../Data/Raw/EmployeeAttrition.csv')
print(data.head())
print(data.info())
print(data.describe())
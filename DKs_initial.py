import pandas ## import pandas library

DK_data = pandas.read_csv("..\Draft_Kings_Salaries_WK4SunMon.csv") ## read .csv and define datafile

print DK_data.head(5) ## Show the first 5 lines
print DK_data.dtypes ## List of data types for each field
print DK_data.shape ## size of dataset
print DK_data['Salary'].describe(include='all') ## key statistics for Salary field

DK_data_RB = DK_data[DK_data['Position']=='RB'] ## define RB data
print DK_data_RB['Salary'].describe(include='all') ## key statistics for Salary field
print DK_data_RB.head(10) ## top 10 RB in list

DK_data_RB_1 = DK_data_RB.sort_values(by='AvgPointsPerGame', ascending=False)
print DK_data_RB_1['Name'].head(10)


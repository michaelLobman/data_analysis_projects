import pandas as pd

def calculate_demographic_data(print_data=True):
	df = pd.read_csv('./adult.data.csv')
	race_count = df.race.value_counts()
	average_age_men = round(df[df.sex == 'Male'].age.mean(), 1)
	percent_bachelors = round((df.education.value_counts()['Bachelors'] / len(df)) * 100, 1)

	higher_education = (df.education == 'Bachelors') | (df.education == 'Masters') | (df.education == 'Doctorate')
	lower_education = (df.education != 'Bachelors') & (df.education != 'Masters') & (df.education != 'Doctorate')

	rich = (df.salary == ">50K")

	higher_education_rich = round((len(df.loc[higher_education & rich]) / len(df[higher_education]) * 100), 1)
	lower_education_rich = round((len(df.loc[lower_education & rich]) / len(df[lower_education]) * 100), 1)

	min_work_hours = df['hours-per-week'].min()

	min_hours_mask = (df['hours-per-week'] == min_work_hours)

	num_min_workers = len(df[min_hours_mask])


	rich_percentage = round(len(df.loc[rich & min_hours_mask]) / num_min_workers * 100, 1)



	# just have to figure out how to do this for each particular country
	# i think this can be googled and looked up on the google collab -
	#i t's just about getting native country to be a certain value essentially

	# query = df.groupby(['native-country']).size()
	# query2 = df[rich]['native-country'].count()



	# print(query2)

	# closest effort
	query = df[rich]['native-country'].value_counts()
	query2 = df['native-country'].value_counts()
	query3 = round((df.loc[rich]['native-country'].value_counts() / df['native-country'].value_counts() * 100).sort_values(ascending=False).head(1).iloc[0], 1)

	print(query3)

	# old effort
	# df['pct_rich'] = len(df[rich]['native-country']) / len(df['native-country'])
	# highest_earning_country = df[rich]['native-country']
	# print(df['fnlwgt']['native-country'].value_counts())



	highest_earning_country_percentage = round((df[rich]['native-country'].value_counts()['United-States'] / len(df[rich])) * 100, 1)

	india = (df['native-country'] == 'India')

	df.loc[rich & india]['occupation'].value_counts().idxmax()

	# print(df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K')])





calculate_demographic_data()
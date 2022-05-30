import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

df = pd.read_csv(
	'./fcc-forum-pageviews.csv',
	index_col=0,
	parse_dates=True
	)
df.rename({'value': 'page_views'}, axis=1, inplace=True)


clean_mask = (
	df['page_views'] > df['page_views'].quantile(0.025)
	) & (
	df['page_views'] < df['page_views'].quantile(0.975)
	)

df = df.loc[clean_mask]

# *** First figure code ***

df_lp = df.copy()
lp = sns.lineplot(data=df_lp, x="date", y="page_views")
lp.set( title= "Daily freeCodeCamp Forum Page Views 5/2016-12/2019", xlabel="Date", ylabel="Page Views")

# *** Second figure code ***
full_onths = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

df_bar = df.copy()
df_bar = df_bar.resample('M').mean()
df_bar['date'] = df_bar.index
df_bar['year'] = df_bar['date'].dt.year
df_bar['month'] = df_bar['date'].dt.month_name()
df_bar['month'] = pd.Categorical(df_bar['month'], categories=full_months, ordered=True)
df_bar = df_bar.sort_values(by="month")
bar = sns.barplot(x="year", y="page_views", hue="month", data=df_bar)
bar.set( xlabel="Years", ylabel="Average Page Views")


# *** Third figure code ***

df_box = df.copy()
df_box.reset_index(inplace=True)

df_box['year'] = [d.year for d in df_box.date]
df_box['month'] = [d.strftime('%b') for d in df_box.date]
df_box['month'] = pd.Categorical(df_box['month'], categories=months, ordered=True)

df_box2 = pd.melt(df_box, id_vars="month", value_vars="page_views")
df_box2 = df_box2.sort_values(by="month")

f, axes = plt.subplots(1,2)

box_year = sns.boxplot(x="year", y="page_views", data=df_box, ax=axes[0])
box_month = sns.boxplot(x="month", y="value", data=df_box2, ax=axes[1])
box_month.set( title="Month-wise Box Plot (Seasonality)", xlabel="Month", ylabel="Page Views")
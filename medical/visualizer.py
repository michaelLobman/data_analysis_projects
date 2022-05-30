import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sns.set_theme(style="ticks", color_codes=True)

df = pd.read_csv('./medical_examination.csv')
df['overweight'] = np.where(df['weight'] / ((df['height'] / 100) ** 2) > 25, 1, 0)


df['cholesterol'] = np.where(df['cholesterol'] > 1, 1, 0)
df['gluc'] = np.where(df['gluc'] > 1, 1, 0)

category_order = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']

df_cat = pd.melt(df, id_vars='cardio', value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
p = sns.catplot(x='variable', kind='count', aspect=0.7, col='cardio', hue='value', data=df_cat, order=category_order)
p.set(ylabel="total")

clean_masks = (
	df['ap_lo'] <= df['ap_hi']
	) & (
	df['height'] >= df['height'].quantile(0.025)
	) & (
	df['height'] <= df['height'].quantile(0.975)
	) & (
	df['weight'] >= df['weight'].quantile(0.025)
	) & (
	df['weight'] <= df['weight'].quantile(0.975)
)

df_heat = df.loc[clean_masks]
corr = df_heat.corr()
corr = round(corr, 1)
mask = np.zeros_like(corr)
mask[np.triu_indices_from(mask)] = True
with sns.axes_style("white"):
    f, ax = plt.subplots(figsize=(7, 5))
    hm = sns.heatmap(corr, fmt='.1f', mask=mask, vmax=.3, annot=True, square=True)

fig = hm.get_figure()
plt.show()
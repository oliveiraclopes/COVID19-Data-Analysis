import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('worldometer_data.csv')
top_countries = df.groupby('Country/Region')['TotalCases'].sum().nlargest(5)

plt.figure(figsize = (8, 8))
plt.pie(top_countries, labels = top_countries.index, autopct = '%1.1f%%', startangle = 140)
plt.title('Top 5 Countries with the Most Cases')
viridian_palette = sns.light_palette('#40826D', n_colors=5)
sns.set_palette(viridian_palette)
plt.show()
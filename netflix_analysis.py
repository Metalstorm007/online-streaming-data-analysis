# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# print("Data Analytics Project Started")

import pandas as pd

df = pd.read_csv("netflix_titles.csv")

print(df.head())

print(df['type'].value_counts())

import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(x='type', data=df)
plt.title("Movies vs TV shows on Netflix")
plt.show()
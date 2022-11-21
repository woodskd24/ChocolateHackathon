# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sns

cocoa = pd.read_csv("C:/Users/Kelsey/Documents/ChocolateCleanOfficial2.csv")
cocoa["rating"] = cocoa.rating

#%%
cocoa.rating.value_counts()
cocoa.rating.value_counts(normalize=True)
#%%
cocoa.rating.mean()
#%%
cocoa.shape
#%%
cocoa.info()
#%%
cocoa.duplicated().sum()
#%%
cocoa.rating.value_counts().plot(kind="bar")
plt.title("Value counts of the target variable")
plt.xlabel("Wine type")
plt.xticks(rotation=0)
plt.ylabel("Count")
plt.show()

#%%
cocoa.rating.describe()

#%%
print(f"Skewness: {cocoa['rating'].skew()}")
print(f"Kurtosis: {cocoa['rating'].kurt()}")
#%%
sns.catplot(x="rating", y="company_location", data=cocoa, kind="box", aspect=1.5)
plt.title("Boxplot for target vs proline")
plt.show()
#%%
sns.catplot(x="rating", y="country_of_bean_origin", data=cocoa, kind="box", aspect=1.5)
plt.title("Boxplot for target vs proline")
plt.show()
#%%
cocoa.corr()
#%%
sns.heatmap(cocoa.corr())
#%%
cocoa[['rating']].boxplot()
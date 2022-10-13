%%markdown
Missigness is when the value for a certain variable is not stored.The variable is empty.
    1. Gender: Categorical/string
    2. Name: string/categorical
    3. Date: datetime
#%%
import pandas as pd
import numpy as np
import seaborn as sns

#%%
df = pd.read_csv("lifeExp-Cleaned.csv")
df.head()

#%%
df.describe()

#%%
df.describe(include="all")

#%%
df.columns

#%%
df_grouped = df.groupby(['Region']).mean()
df_grouped['LifeExp']
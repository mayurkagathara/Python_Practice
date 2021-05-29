# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

haberman = pd.read_csv('/home/mayur/git/Pythonpractice/Python_Practice/Blogger/UOH_practice/Sem_1/Sub_2/haberman.csv',header=None)
haberman.columns = ['Patient_Age','Operation_Year','positive_ax_nodes','Survival_Status']

# %%
print(haberman.shape)
haberman.head()
# %%

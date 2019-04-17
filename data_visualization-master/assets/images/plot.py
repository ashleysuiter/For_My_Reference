import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('~/ga/lessons/data_visualization/assets/data/drinks.csv')
df.plot(kind='bar')
plt.savefig('test.png')
import matplotlib.pyplot as plt; import importlib; importlib.reload(plt)
import pandas as pd
plt.clf()

df = pd.read_csv('http://assets.datacamp.com/course/intermediate_python/gapminder.csv', index_col = 0)
pop = list(df['population']/1000000)
life_exp = list(df.life_exp)

# Build Scatter plot
plt.scatter(pop, life_exp)

# Show plot
plt.show()
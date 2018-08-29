import matplotlib.pyplot as plt; import importlib; importlib.reload(plt)
import pandas as pd
plt.clf()
df = pd.read_csv('http://assets.datacamp.com/course/intermediate_python/gapminder.csv', index_col = 0)
life_exp = list(df.life_exp)

# Create histogram of life_exp data
plt.hist(life_exp)

# Display histogram
plt.show()
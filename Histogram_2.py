import matplotlib.pyplot as plt; import importlib; importlib.reload(plt)
import pandas as pd
plt.clf()
df = pd.read_csv('http://assets.datacamp.com/course/intermediate_python/gapminder.csv', index_col = 0)
life_exp = list(df.life_exp)

#To control the number of bins to divide your data in, you can set the bins argument.

# Build histogram with 5 bins
plt.hist(life_exp, bins = 5)

# Show and clear plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp, bins = 20)

# Show and clear plot again
plt.show()
plt.clf()
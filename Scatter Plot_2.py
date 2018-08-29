import matplotlib.pyplot as plt; import importlib; importlib.reload(plt)
import pandas as pd
plt.clf()
#any dataset as CSV
df = pd.read_csv('.csv', index_col = 0)
pop = list(df['population']/1000000)
life_exp = list(df.life_exp)

# Build Scatter plot
plt.scatter(pop, life_exp)

# Show plot
plt.show()

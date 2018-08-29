import matplotlib.pyplot as plt; import importlib; importlib.reload(plt)
import pandas as pd
plt.clf()
#Any CSV dataset 
df = pd.read_csv('.csv', index_col = 0)
life_exp = list(df.life_exp)

# Create histogram of life_exp data
plt.hist(life_exp)

# Display histogram
plt.show()

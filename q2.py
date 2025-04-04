import pandas as pd

data = [['Alice', 25, 'New York'], ['Bob', 30, 'Chicago'], ['Charlie', 35, 'Los Angeles']]
df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
df_indexed = df.set_index('Name')
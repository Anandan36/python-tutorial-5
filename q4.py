import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Chicago', 'Los Angeles', 'Houston']
}

df = pd.DataFrame(data)
df.to_excel('sample_data.xlsx', index=False)
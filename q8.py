import pandas as pd

auto_data = {
    'company': ['Toyota', 'Honda', 'BMW', 'Audi', 'Toyota', 'Mercedes', 'BMW'],
    'body-style': ['Sedan', 'SUV', 'Coupe', 'Sedan', 'Hatchback', 'SUV', 'Sedan'],
    'wheel-base': [102, 104, 106, 105, 101, 108, 107],
    'length': [175, 180, 185, 183, 170, 190, 187],
    'engine-type': ['gas', 'gas', 'diesel', 'gas', 'hybrid', 'diesel', 'gas'],
    'num-of-cylinders': [4, 4, 6, 6, 4, 8, 6],
    'horsepower': [150, 160, 220, 200, 120, 280, 230],
    'average-mileage': [28, 25, 22, 24, 32, 20, 23],
    'price': [22000, 25000, 45000, 40000, 24000, 60000, 48000]
}

auto_df = pd.DataFrame(auto_data)
auto_df.to_csv('auto.csv', index_label='index')

auto_df = pd.read_csv('auto.csv')
auto_df = auto_df.dropna()

most_expensive = auto_df.loc[auto_df['price'].idxmax()]
toyota_cars = auto_df[auto_df['company'] == 'Toyota']
company_counts = auto_df['company'].value_counts()
highest_priced = auto_df.groupby('company')['price'].max()
avg_mileage = auto_df.groupby('company')['average-mileage'].mean()
sorted_by_price = auto_df.sort_values(by='price')
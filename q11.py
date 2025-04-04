import pandas as pd
import matplotlib.pyplot as plt

sales_data = {
    'month_number': list(range(1, 13)),
    'facecream': [2500, 2630, 2140, 3400, 3600, 2760, 2980, 3700, 3540, 1990, 2340, 2900],
    'facewash': [1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760],
    'toothpaste': [5200, 5100, 4550, 5870, 4560, 4890, 4780, 5860, 6100, 4580, 5200, 5300],
    'bathingsoap': [9200, 6100, 9550, 8870, 7760, 7490, 8980, 9960, 8100, 7580, 5200, 7300],
    'shampoo': [1200, 2100, 3550, 1870, 1560, 1890, 1780, 2860, 2100, 2580, 2200, 1300],
    'moisturizer': [1500, 1200, 1700, 2000, 1500, 1800, 2100, 1750, 1800, 1900, 2200, 1500]
}

sales_df = pd.DataFrame(sales_data)

sales_df['total_units'] = sales_df['facecream'] + sales_df['facewash'] + sales_df['toothpaste'] + \
                          sales_df['bathingsoap'] + sales_df['shampoo'] + sales_df['moisturizer']
sales_df['total_profit'] = sales_df['total_units'] * 0.10

sales_df.to_csv('sales.csv', index=False)

plt.figure(figsize=(10, 6))
plt.scatter(sales_df['month_number'], sales_df['toothpaste'], color='blue', marker='o')
plt.title('Toothpaste Sales Data')
plt.xlabel('Month Number')
plt.ylabel('Sales Units')
plt.grid(True)
plt.savefig('toothpaste_sales_scatter.png')
plt.close()

plt.figure(figsize=(12, 6))
X = sales_df['month_number']
plt.bar(X-0.2, sales_df['facecream'], width=0.4, label='Face Cream')
plt.bar(X+0.2, sales_df['facewash'], width=0.4, label='Face Wash')
plt.xlabel('Month Number')
plt.ylabel('Sales Units')
plt.title('Face Cream and Face Wash Sales Data')
plt.legend()
plt.grid(True)
plt.savefig('facecream_facewash_bar.png')
plt.close()

product_sales = [
    sales_df['facecream'].sum(),
    sales_df['facewash'].sum(),
    sales_df['toothpaste'].sum(),
    sales_df['bathingsoap'].sum(),
    sales_df['shampoo'].sum(),
    sales_df['moisturizer'].sum()
]

product_names = ['Face Cream', 'Face Wash', 'Toothpaste', 'Bathing Soap', 'Shampoo', 'Moisturizer']

plt.figure(figsize=(10, 8))
plt.pie(product_sales, labels=product_names, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Total Sales Data by Product')
plt.savefig('product_sales_pie.png')
plt.close()
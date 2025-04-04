import pandas as pd
import matplotlib.pyplot as plt

stud_data = {
    'rollno': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy'],
    'place': ['New York', 'Chicago', 'Los Angeles', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose'],
    'mark': [85, 92, 78, 95, 88, 76, 90, 82, 79, 91]
}

stud_df = pd.DataFrame(stud_data)
stud_df.to_csv('stud.csv', index=False)

stud_df = pd.read_csv('stud.csv')
stud_df_indexed = stud_df.set_index('rollno')
stud_df_indexed[['name', 'mark']]
sorted_by_name = stud_df.sort_values(by='name')
sorted_by_mark_desc = stud_df.sort_values(by='mark', ascending=False)

avg_mark = stud_df['mark'].mean()
median_mark = stud_df['mark'].median()
mode_mark = stud_df['mark'].mode()[0]
min_mark = stud_df['mark'].min()
max_mark = stud_df['mark'].max()
variance = stud_df['mark'].var()
std_dev = stud_df['mark'].std()

plt.figure(figsize=(10, 6))
plt.hist(stud_df['mark'], bins=10, edgecolor='black')
plt.title('Histogram of Marks')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.savefig('marks_histogram.png')
plt.close()

stud_df_no_place = stud_df.drop('place', axis=1)
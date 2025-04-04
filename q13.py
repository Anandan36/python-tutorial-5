import pandas as pd

employee_data = {
    'name': ['Alice Smith', 'Bob Johnson', 'Charlie Brown', 'Diana Ross', 'Ethan Hunt', 'Fiona Apple', 'George Lucas', 'Helen Mirren'],
    'gender': ['F', 'M', 'M', 'F', 'M', 'F', 'M', 'F'],
    'start_date': ['2018-05-01', '2019-01-15', '2017-10-10', '2020-03-20', '2018-12-05', '2019-08-30', '2017-06-15', '2020-02-10'],
    'salary': [75000, 82000, 60000, 95000, 78000, 72000, 90000, 88000],
    'team': ['Sales', 'Engineering', 'Support', 'Management', 'Engineering', 'Sales', 'Research', 'Management']
}

employee_df = pd.DataFrame(employee_data)
employee_df.to_csv('employee.csv', index=False)

employee_df = pd.read_csv('employee.csv')
employee_df.head(7)
sorted_names = sorted(employee_df['name'])
highest_salary_employee = employee_df.loc[employee_df['salary'].idxmax()]
male_employees = employee_df[employee_df['gender'] == 'M']
unique_teams = employee_df['team'].unique()
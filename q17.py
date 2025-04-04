import pandas as pd

student_data = {
    'Name': ['Alice Smith', 'Bob Johnson', 'Charlie Brown', 'Diana Ross', 'Ethan Hunt',
             'Fiona Apple', 'George Lucas', 'Helen Mirren', 'Ian McKellen', 'Jane Austen'],
    'Branch': ['CSE', 'ECE', 'CSE', 'Mechanical', 'CSE', 'ECE', 'CSE', 'Chemical', 'CSE', 'Civil'],
    'Year': [1, 2, 3, 2, 4, 1, 3, 2, 4, 3],
    'CGPA': [9.5, 8.7, 9.2, 8.3, 9.8, 8.9, 7.5, 8.6, 9.1, 8.8]
}

student_df = pd.DataFrame(student_data)
student_df.to_csv('student.csv', index=False)

student_df = pd.read_csv('student.csv')
avg_cgpa = student_df['CGPA'].mean()
high_cgpa_students = student_df[student_df['CGPA'] > 9]
cse_high_cgpa = student_df[(student_df['Branch'] == 'CSE') & (student_df['CGPA'] > 9)]
max_cgpa_student = student_df.loc[student_df['CGPA'].idxmax()]
branch_avg_cgpa = student_df.groupby('Branch')['CGPA'].mean()
import pandas as pd

students_data = {
    'Reg_no': [10001, 10002, 10003],
    'Name': ['Jack', 'John', 'Alex'],
    'Sub_Mark1': [76, 77, 74],
    'Sub_Mark2': [88, 84, 79],
    'Sub_Mark3': [76, 79, 81]
}

students_df = pd.DataFrame(students_data)
students_df.to_csv('students.csv', index=False)
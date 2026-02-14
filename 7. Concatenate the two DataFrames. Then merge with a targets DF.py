#7. Concatenate the two DataFrames. Then merge with a targets DataFrame.
import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    'id':[1,2,3,4,5,6,7],
    'role':['data analyst', 'data scientist', 'data engineer', 'software engineer', 'controller', 'HRM', 'CFO']
})

df2 = pd.DataFrame({
    'department':['IT', 'IT', 'IT', 'IT', 'Finance', 'HR', 'Finance']
})

df3 = pd.DataFrame({
    'id':[1,2,3,4,5,6,8],
    'salary':[50000, 70000, 80000, 90000, 70000, 80000, 120000]
})

#concatenate
concat = pd.concat([df1, df2], axis='columns')
print(concat)

#merge
merged = pd.merge(concat, df3, on='id', how='outer')
print(merged)

#fill na
median_salary = merged['salary'].median()
merged['salary'] = merged['salary'].fillna(median_salary)
merged['department'] = merged['department'].fillna('remaining budget')
merged['role'] = merged['role'].fillna('new role')
print(merged)

#group by
grouped = merged.groupby('department')
final = grouped[['salary']].mean()
print(final)

#sort descending
sort_by_salary = final.sort_values(by= 'salary', ascending=False)
print(sort_by_salary)
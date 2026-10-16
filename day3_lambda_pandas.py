import pandas as pd

data = {
    'Name' : ['Alice', 'Bob', 'Charlie'],
    'Salary': [60000, 120000, 96000],
    'Bonus': [5000, 10000, 8000]
}

df = pd.DataFrame(data)
print(df)

# Transforming a single column
df['Raised_Salary'] = df['Salary'].apply(lambda x: x * 1.10)
print(df)

# Using if else on a column
df['Tax_Bracket'] = df['Raised_Salary'].apply(lambda x: '30%' if x > 150000 else ('20%' if 100000 < x <= 150000 else '0%'))
print(df)

# Row-wise operations (Multiple columns). axis = 1 ==> process row by row
df['Total_Comp'] = df.apply(lambda row: row['Raised_Salary'] + row['Bonus'], axis = 1)
print(df)

# String manipulation
df['Name_Lower'] = df['Name'].apply(lambda name: name.lower())
print(df)
#reads a csv of student grades and calculates some basic stats
import pandas as pd

#load the csv into a pandas dataframe
#a dataframe is basically a table, like in excel.
df = pd.read_csv('grades.csv')

print('--- original data ---')
print(df)
print('') # for a blank line

#calculate the stats from the 'grade' column
avg_grade = df['grade'].mean()
max_grade = df['grade'].max()
min_grade = df['grade'].min()

#print what we found
print('--- analysis ---')
print(f'average grade: {avg_grade:.2f}')
print(f'highest grade: {max_grade}')
print(f'lowest grade: {min_grade}')
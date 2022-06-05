# -*- coding: utf-8 -*-
"""
Created on Mon May 16 23:36:06 2022

@author: ranro
"""
import pandas as pd
from datetime import datetime
df = pd.read_csv('glassdoor_jobs.csv')
df.drop('Unnamed: 0',axis=1, inplace=True)

# ------ TO-DO -------
# Salary Parsing
# Company name text only
# State Field
# Age of company
# Parsing of job description (python, etc.)

df = df[df['Salary Estimate'] != '-1']   # Removing -1 from salary estimations

######## Salary Parsing

# Adding columns for hourly and annual salary as indicators
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)

# Adding a column for 'Employer provided' as indicator
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided' in x.lower() else 0)

salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

min_hr = minus_kd.apply(lambda x: x.lower().replace('per hour', '').replace('employer provided salary:', ''))

df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))

# Adding the average salary
df['avg_salary'] = (df['min_salary'] + df['max_salary']) / 2


######## Company name text only
df['Company_txt'] = df.apply(lambda x: x['Company Name'].replace(str(x['Rating']),''),axis=1)


######## State Field
df['state'] = df['Location'].str.split(',').apply(lambda x: x[1].strip())

# Check if the lcoation is at the headquarters location
df['same_state'] = df.apply(lambda x: 1 if x.Location==x.Headquarters else 0, axis=1)

######## Age Of Company
df['age_of_company'] = df['Founded'].apply(lambda x: x if x<1 else int(datetime.now().year) - int(x))


######## Parsing of Job Description
# Python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)

# R studio
df['r_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)

# Spark
df['spark_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() or 'spark' in x.lower() else 0)

# AWS
df['aws_yn'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() or 'excel
                                             
# Excel
df['excel_yn'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() or 'excel' in x.lower() else 0)

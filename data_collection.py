# -*- coding: utf-8 -*-
"""
Created on Sun May 15 23:18:55 2022

@author: ranro
"""

import glassdor_scraper as gs
import pandas as pd
path = 'C:/Users/ranro/Documents/chromedriver'


df = pd.read_csv('glassdoor_jobs.csv')
df.drop('Unnamed: 0', axis=1, inplace=True)
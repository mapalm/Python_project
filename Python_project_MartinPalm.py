#!/usr/bin/env python

# Imports the pandas package as pd
import pandas as pd

# Creates a data frame from the data .csv file
df = pd.read_csv('C:/Users/KMB/Documents/Python course/test_data.csv', sep=';')

# Creates a list of antibiotics from the antibiotics.csv file
antibiotics_list = list(pd.read_csv('C:/Users/KMB/Documents/Python course/antibiotics.csv', sep=';'))

# Creates a list of strains from the strains.csv file
strain_list = list(pd.read_csv('C:/Users/KMB/Documents/Python course/strains.csv', sep=';'))

# Pulls out all information about strains resistant ('r') to antibiotic in antibiotics_list and saves it in separate .csv files
def antibiotic_to_resistance(antibiotics_list):
    for antibiotic in antibiotics_list:
        output = df.loc[df[antibiotic].isin(['r'])]
        output.to_csv('Resistance to '+antibiotic+'.csv', sep=';', mode='w', index=False)
        #print(df.loc[df[str(antibiotic)].isin(['r'])])
        
antibiotic_to_resistance(antibiotics_list)

# Pulls all the information about strains listed in strain_list        
def strain_to_resistance(strain_list):
    result = pd.DataFrame()
    for strain in strain_list:
        output2 = df.loc[df['Our identifier'].isin([strain])]
        result = result.append(output2)
    # Save the result WITH SPECIFIC COLUMNS          
    result.to_csv('Resistances.csv', sep=';', mode='w', index=False)
    
strain_to_resistance(strain_list)
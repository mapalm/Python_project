#!/usr/bin/env python

# Imports the pandas package as pd
import pandas as pd

# Creates a data frame from the data .csv file
df = pd.read_csv('C:/Users/KMB/Documents/Python course/test_data.csv', sep=';')

# Creates a list of antibiotics from the antibiotics.csv file
antibiotics_list = list(pd.read_csv('C:/Users/KMB/Documents/Python course/antibiotics.csv', sep=';'))

# Creates a list of strains from the strains.csv file
strain_list = list(pd.read_csv('C:/Users/KMB/Documents/Python course/strains.csv', sep=';'))

# Pulls out all information about strains that are resistant to a specific antibiotic and saves it in a .csv file
def antibiotic_to_resistance(antibiotic):
    output = df.loc[df[antibiotic].isin(['r'])]
    output.to_csv('Resistance to '+antibiotic+'.csv', sep=';', mode='w', index=False)
        

# Pulls out all information about strains resistant ('r') to antibiotic in antibiotics_list and saves it in separate .csv files
def antibiotics_to_resistance(antibiotics_list):
    for antibiotic in antibiotics_list:
        output = df.loc[df[antibiotic].isin(['r'])]
        output.to_csv('Resistance to '+antibiotic+'.csv', sep=';', mode='w', index=False)
        #print(df.loc[df[str(antibiotic)].isin(['r'])])

# Remove the # to test the function
#antibiotics_to_resistance(antibiotics_list)

def strain_to_resistance(strain):
    result = pd.DataFrame()
    output = df.loc[df['Our identifier'].isin([strain])]
    result = result.append(output)
    result.to_csv('Resistances for '+strain+'.csv', columns=['Our identifier', 'Ampicillin', 'Ceftazidime', 'Cefotaxime', 'Cefuroxime', 'Ciprofloxacin', 'Gentamycin', 'Tobramycin', 'Trimethoprim'], sep=';', mode='w', index=False)

# Remove the # to test the function
#strain_to_resistance('GU48')


# Pulls all the information about strains listed in strain_list        
def strains_to_resistance(strain_list):
    result = pd.DataFrame()
    for strain in strain_list:
        output = df.loc[df['Our identifier'].isin([strain])]
        result = result.append(output)
    # Saves only the resistance columns to a .csv file          
    result.to_csv('Resistances.csv', columns=['Our identifier', 'Ampicillin', 'Ceftazidime', 'Cefotaxime', 'Cefuroxime', 'Ciprofloxacin', 'Gentamycin', 'Tobramycin', 'Trimethoprim'], sep=';', mode='w', index=False)

# Remove the # to test the function   
#strains_to_resistance(strain_list)

def accession(strain_list):
    result = pd.DataFrame()
    for strain in strain_list:
        output = df.loc[df['Our identifier'].isin([strain])]
        result = result.append(output)
    # Saves only the accession number column to a .csv file
    result.to_csv('Accessions.csv', columns=['Our identifier', 'Accession number (if available)'], sep=';', mode='w', index=False)
    
# Remove the # to test the function 
#accession(strain_list)


# Asks the user for input on what data to pull out and based on what information (strains, antibiotics)
query = input('What information do you want to pull out (resistances, accessions etc.)? ')
if len(query) > 0 and ((query == 'resistances' or query == 'Resistances') or (query == 'accession' or query == 'Accession')):
    if query == 'resistances' or 'Resistances':
        query2 = input('From a list of strains or antibiotics? ')
    if query2 == 'strains' or query2 == 'Strains':
        query3 = input('For which strain? If you have a list of strains please enter "list". ')
        if query3 == 'list':
            query4 = list(pd.read_csv('C:/Users/KMB/Documents/Python course/' + input('Please give the name of your strain list (including file extension, e.g. .csv). Remember to place it in the same folder as this script. '), sep=';'))
    elif query2 == 'antibiotics' or query2 == 'Antibiotics':
        query5 = input('For which antibiotic? If you have a list of antibiotics please enter "list". ')
        if query5 == 'list':
            query6 = list(pd.read_csv('C:/Users/KMB/Documents/Python course/' + input('Please give the name of your list of antibiotics (including file extension, e.g. .csv). Remember to place it in the same folder as this script. '), sep=';'))
    else:
        print('Please enter a correct type of data. The available types of data are "resistances", "accession". ')
else:
    print('Please enter a correct type of data. The available types of data are "resistances", "accession". ')

# Calls the functions defined above based on the input given by the user
if query == 'resistances' or query == 'Resistances':
    if query2 == 'strains':
        if query3 == 'list':
            strains_to_resistance(query4)
        else:
            strain_to_resistance(query3)
    elif query2 == 'antibiotics':
        if query5 == 'list':
            antibiotics_to_resistance(query6)
        else:
            antibiotic_to_resistance(query5)


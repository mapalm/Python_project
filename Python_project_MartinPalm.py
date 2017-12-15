#!/usr/bin/env python

# Imports the pandas package as pd
import pandas as pd
# Imports the os package, used to make folders
import os

# Creates a data frame from the data .csv file
input_file = input('Please enter the name of your data .csv file. Remember to place it in the same folder as this script. ')
df = pd.read_csv('./' + input_file + '.csv', sep=';')

# Creates a list of antibiotics from the antibiotics.csv file
antibiotics_list = list(pd.read_csv('./antibiotics.csv', sep=';'))

# Creates a list of strains from the strains.csv file
strain_list = list(pd.read_csv('./strains.csv', sep=';'))


# Pulls out all information available for strain
def all_info(strain):
    result = pd.DataFrame()
    output = df.loc[df['Our identifier'].isin([strain])]
    result = result.append(output)
    result.to_csv('./Results for ' + input_file + '/All information for ' + strain + '.csv', sep=';', mode='w', index=False)

# Pulls out all information available for strain in strain_list
def all_info_multiple(strain_list):
    result = pd.DataFrame()
    for strain in strain_list:
        output = df.loc[df['Our identifier'].isin([strain])]
        result = result.append(output)
        result.to_csv('./Results for ' + input_file + '/All information.csv', sep=';', mode='w', index=False)

# Pulls out all information about strains that are resistant to a specific antibiotic and saves it in a .csv file
def antibiotic_to_resistance(antibiotic):
    output = df.loc[df[antibiotic].isin(['R'])]
    output.to_csv('./Results for ' + input_file +'/Resistance to '+antibiotic+'.csv', sep=';', mode='w', index=False)
        

# Pulls out all information about strains resistant ('r') to antibiotic in antibiotics_list and saves it in separate .csv files
def antibiotics_to_resistance(antibiotics_list):
    for antibiotic in antibiotics_list:
        output = df.loc[df[antibiotic].isin(['R'])]
        output.to_csv('./Results for ' + input_file + '/Resistance to '+antibiotic+'.csv', sep=';', mode='w', index=False)
        #print(df.loc[df[str(antibiotic)].isin(['r'])])

# Remove the # to test the function
#antibiotics_to_resistance(antibiotics_list)

def strain_to_resistance(strain):
    result = pd.DataFrame()
    output = df.loc[df['Our identifier'].isin([strain])]
    result = result.append(output)
    result.to_csv('./Results for ' + input_file + '/Resistances for '+strain+'.csv', columns=['Our identifier', 'Ampicillin', 'Ceftazidime', 'Cefotaxime', 'Cefuroxime', 'Ciprofloxacin', 'Gentamycin', 'Tobramycin', 'Trimethoprim'], sep=';', mode='w', index=False)

# Remove the # to test the function
#strain_to_resistance('GU48')


# Pulls all the information about strains listed in strain_list        
def strains_to_resistance(strain_list):
    result = pd.DataFrame()
    for strain in strain_list:
        output = df.loc[df['Our identifier'].isin([strain])]
        result = result.append(output)
    # Saves only the resistance columns to a .csv file          
    result.to_csv('./Results for ' + input_file + '/Resistances.csv', columns=['Our identifier', 'Ampicillin', 'Ceftazidime', 'Cefotaxime', 'Cefuroxime', 'Ciprofloxacin', 'Gentamycin', 'Tobramycin', 'Trimethoprim'], sep=';', mode='w', index=False)

# Remove the # to test the function   
#strains_to_resistance(strain_list)

# Pulls out the accession number for strain
def accession(strain):
    result = pd.DataFrame()
    output = df.loc[df['Our identifier'].isin([strain])]
    result = result.append(output)
    # Saves only the accession number column to a .csv file
    result.to_csv('./Results for ' + input_file + '/Accession number for '+strain+'.csv', columns=['Our identifier', 'Accession number (if available)'], sep=';', mode='w', index=False)


# Pulls out the accession numbers for the strains in strain_list
def accessions(strain_list):
    result = pd.DataFrame()
    for strain in strain_list:
        output = df.loc[df['Our identifier'].isin([strain])]
        result = result.append(output)
    # Saves only the accession number column to a .csv file
    result.to_csv('./Results for ' + input_file + '/Accessions.csv', columns=['Our identifier', 'Accession number (if available)'], sep=';', mode='w', index=False)

# Remove the # to test the function 
#accession(strain_list)

def position(strain):
    result = pd.DataFrame()
    output = df.loc[df['Our identifier'].isin([strain])]
    result = result.append(output)
    result.to_csv('./Results for ' + input_file + '/Positions for ' + strain + '.csv', columns=['Our identifier', '96 well plate', '96 well position', '384 well plate', '384 well position', 'Genomic DNA plate (if isolated)', 'Genomic DNA plate position', 'Sequencing plate', 'Sequencing plate position'], sep=';', mode='w', index=False)


# Pulls out all the positions for strains in strain_list
def positions(strain_list):
    result = pd.DataFrame()
    for strain in strain_list:
        output = df.loc[df['Our identifier'].isin([strain])]
        result = result.append(output)
    result.to_csv('./Results for ' + input_file + '/Positions.csv', columns=['Our identifier', '96 well plate', '96 well position', '384 well plate', '384 well position', 'Genomic DNA plate (if isolated)', 'Genomic DNA plate position', 'Sequencing plate', 'Sequencing plate position'], sep=';', mode='w', index=False)
        
      
# Asks the user for input on what data to pull out and based on what information (strains, antibiotics)
query = input('What information do you want to pull out (all, resistances, accessions, positions etc.)? ')
if len(query) > 0 and (query == 'resistances' or query == 'Resistances'):
    if query == ('resistances' or query == 'Resistances') or (query == 'accession' or query == 'Accession'):
        query2 = input('From a list of strains or antibiotics? ')
    if query2 == 'strains' or query2 == 'Strains':
        query3 = input('For which strain? If you have a list of strains please enter "list". ')
        if query3 == 'list':
            query4 = list(pd.read_csv('./' + input('Please give the name of your strain list (including file extension, e.g. .csv). Remember to place it in the same folder as this script. '), sep=';'))
    elif query2 == 'antibiotics' or query2 == 'Antibiotics':
        query5 = input('For which antibiotic? If you have a list of antibiotics please enter "list". ')
        if query5 == 'list':
            query6 = list(pd.read_csv('./' + input('Please give the name of your list of antibiotics (including file extension, e.g. .csv). Remember to place it in the same folder as this script. '), sep=';'))
    else:
        print('Please enter a correct type of data. The available types of data are "resistances", "accession". ')
        
elif query == 'accession' or query == 'Accession':
    query2 = input('For which strain? If you have a list of strains please enter "list". ')
    if query2 == 'list':
        query3 = list(pd.read_csv('./' + input('Please give the name of your strain list (including file extension). Remember to place it in the same folder as this script. '), sep=';'))

elif query == 'positions' or query == ' Positions':
    query2 = input('For which strain? If you have a list of strains please enter "list". ')
    if query2 == 'list':
        query3 = list(pd.read_csv('./' + input('Please give the name of your strain list (including file extension). Remember to place it in the same folder as this script. '), sep=';'))

elif query == 'all' or query == 'All':
    query2 = input('For which strain? If you have a list of strains please enter "list". ')
    if query2 == 'list':
        query3 = list(pd.read_csv('./' + input('Please give the name of your strain list (including file extension). Remember to place it in the same folder as this script. '), sep=';'))
else:
    print('Please enter a correct type of data. The available types of data are "resistances", "accession". ')

# Creates a folder named for the specific input file if it does not exists
if not os.path.exists('./Results for ' + input_file):
    os.mkdir('./Results for ' + input_file)

# Calls the functions defined above based on the input given by the user

if query == 'all' or query == 'All':
    if query2 == 'list':
        all_info_multiple(query3)
    else:
        all_info(query2)
        
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
            
if query == 'accession' or query == 'Accession':
    if query2 == 'list':
        accessions(query3)
    else:
        accession(query2)
        
if query == 'positions' or query == 'Positions':
    if query2 == 'list':
        positions(query3)
    else:
        position(query2)


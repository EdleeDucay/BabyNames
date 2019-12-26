"""

CMPT 103 - Programming Project Milestone # 1, 2 & 3
Date: Fall 2018
Author: Edlee Ducay

The purpose of this program is to explore the baby name data

"""

import fnmatch
from draw_graph import *
from process_files import *

menu = f'''
Alberta Baby names 1980 to 2017
{"-"*31}
(0) Quit
(1) Load and process text file
(2) Save processed data
(3) Open processed data
(4) Print top ten lists
(5) Search for a name
(6) Names that appear only once in a year
(7) Longest name
(8) Search for names with specific letters
(9) Graphically display the trend of a name
'''

def main():
    '''
    This is the text-based menu system for the program
    
    Parameters:
    none
    Return:
    none
    
    '''
    
    # While loop to keep program running until 0 is inputted
    num = ''
    loaded = False

    while num != '0':
        print(menu)
        num = input('Enter command: ')
        
        # Command 1
        if num == '1':
            (topTen_dict, names_dict) = load_file()    
        
        # Command 2
        if num == '2':
            filename = input('Enter a file name [baby_names.p]: ') or 'baby_names.p'
            try:
                save_dicts(filename, topTen_dict, names_dict)
            except:
                print('\nError saving file!')    
    
        # Command 3
        if num == '3':
            try:
                loaded_dicts = load_pickle()            
            except:
                print('\nError loading file!')        
            else:
                loaded = True

        # Command 4
        if num =='4' and loaded == True:
            print_top_ten(loaded_dicts[0])
            
        # Command 5
        if num == '5' and loaded == True:
            names_search(loaded_dicts[1])
        
        # Command 6
        if num == '6' and loaded == True:
            get_unique_names(loaded_dicts[1])
        
        # Command 7
        if num == '7' and loaded == True:
            longest_names(loaded_dicts[1])
        
        # Command 8
        if num == '8' and loaded == True:
            wildcard_search(loaded_dicts[1])
        
        # Command 9
        if num == '9' and loaded == True:
            draw_graph(loaded_dicts[1])

        if loaded == False and num > '3':
            print('\nError: No files loaded!')
            
    print('Goodbye')

def print_top_ten(topTen_dict):
    '''
    (Command 4)
    This function prints the top ten list for 
    a certain gender and certain year (Command 4)

    Parameters:
    dictionary
        the top ten dictionary
    Returns:
        none
        
    '''
    
    # Getting user input
    gender = ''
    year = 0
    while gender not in ('b','g'):
        gender = input("Enter B for boy's names or G for girl's names: ").lower()
    if gender == 'b':
        gender = 'boys'
    else:
        gender = 'girls'
    while year not in range(1980,2018):
        try:
            year = int(input('Enter year (1980 to 2017): '))
        except:
            return None
    if year not in topTen_dict[gender]:
        return None
        
    # Printing the top ten lists
    print(f'\nTop 10 names for baby {gender} born in Alberta in {year}:')
    for i in range(len(topTen_dict[gender][year])):
        name = topTen_dict[gender][year].pop(0)
        print(f'\t{name[0]} {name[1]} {name[2]}')
      
def names_search(names_dict):
    ''' 
    (Command 5)
    This function prints the frequencies of boys and girls given the name

    Parameters:
    dictionary
        the names dictionary
    Returns:
        none
    
    '''
    
    # Printing the names frequencies
    name = input('Enter a name: ').capitalize()
    
    if name not in names_dict:
        print(f'There were no babies named {name} born in Alberta between 1980 and 2017')
        print(menu)                
        return None
    
    print(f'\n{name}:\n\tBoys\tGirls')
    name = names_dict[name]
    for year in range(1980,2018):
        freq_b = 0
        freq_g = 0
        for info in name:
            if year in info and 'Boy' in info:
                freq_b = info[0]
            elif year in info and 'Girl' in info:
                freq_g = info[0]
        if freq_b == 0 and freq_g == 0:
            None
        else:
            print(f'{year}\t{freq_b}\t{freq_g}')
    
    return None

def get_unique_names(names_dict):
    '''
    (Command 6)
    This function displays all names with a frequency of 1 for a specified year

    Parameters:
    dictionary
        the names dicitonary
    Returns:
    none
    
    '''
    
    # Getting user input and error checking
    year = 0
    while year not in range(1980,2018):
        try:
            year = int(input('Enter a year (1980 - 2017): '))
        except:
            return None        
    boynames_list = []
    girlnames_list = []
    
    # Finding the names with frequency of 1
    for name, years in names_dict.items():
        for info in years:
            if year == info[2] and info[0] == 1 and info[1] == 'Girl':
                girlnames_list.append(name)
            elif year == info[2] and info[0] == 1 and info[1] == 'Boy':
                boynames_list.append(name)
    girlnames_list = sorted(girlnames_list)
    boynames_list = sorted(boynames_list)
    
    # Displaying the names with frequency of 1
    print('Unique names - Girls:\n')
    names = [girlnames_list[i:i+4] for i in range(0, len(girlnames_list), 4)]
    width = max(len(name) for row in names for name in row) + 2
    for row in names:
        print(''.join(name.ljust(width) for name in row))
    
    print('\nUnique names - Boys:\n')
    names = [boynames_list[i:i+4] for i in range(0, len(boynames_list), 4)]
    width = max(len(name) for row in names for name in row) + 2
    for row in names:
        print(''.join(name.ljust(width) for name in row))    

def longest_names(names_dict):
    '''
    (Command 7)
    This function finds and displays the longest hyphenated & unhyphenated names

    Parameters:
    dictionary
        the names dicitonary
    Returns
    none
     
    '''
    
    # Finding the longest names
    gh_name = ''
    guh_name = ''
    bh_name = ''
    buh_name = ''

    for name, years in names_dict.items():
        for info in years:
            if '-' in name and len(name) > len(gh_name) and info[1] == 'Girl':
                gh_name = name
                gh_year = info[2]
            elif '-' not in name and len(name) > len(guh_name) and info[1] == 'Girl':
                guh_name = name
                guh_year = info[2]
            elif '-' in name and len(name) > len(bh_name) and info[1] == 'Boy':
                bh_name = name
                bh_year = info[2]
            elif '-' not in name and len(name) > len(buh_name) and info[1] == 'Boy':
                buh_name = name
                buh_year = info[2]
    
    # Displaying the names
    print(f'The longest name given to a baby girl between 1980 and 2017 was \
 {gh_name} in {gh_year}')
    print(f'The longest non-hyphenated name given to a baby girl between 1980\
 and 2017 was {guh_name} in {guh_year}\n')
    print(f'The longest name given to a baby boy between 1980 and 2017 was \
 {bh_name} in {bh_year}')
    print(f'The longest non-hyphenated name given to a baby boy between 1980\
 and 2017 was {buh_name} in {buh_year}')    
    
    return None

def wildcard_search(names_dict):
    '''
    (Command 8)
    This function finds names that have what is inputted + any missing letters
    
    Parameters:
    dicitonary
        the names dictionary
    Returns:
    none
    
    '''
    
    # Getting user input
    user_name = input('Enter name with * indicating missing letters: ').capitalize()
    has_name = False
    
    # Looking for matching names and displaying if found
    for name, years in names_dict.items():
        if fnmatch.fnmatch(name, user_name) == True:
            has_name = True
            print(f'\tBoys\tGirls\n{name}')
            for year in range(1980,2018):
                freq_b = 0
                freq_g = 0            
                for info in years:
                    if 'Boy' in info and year in info:
                        freq_b = info[0]
                    elif 'Girl' in info and year in info:
                        freq_g = info[0]
                if freq_b == 0 and freq_g == 0:
                    None
                else:
                    print(f'{year}:\t{freq_b}\t{freq_g}')
            print()
    
    # If no results were found
    if has_name == False and user_name.endswith('*'):
        print(f"There were no babies given a name beginning with '{user_name[0:-1]}'")
    elif has_name == False and user_name.startswith('*'):
        print(f"There were no babies given a name ending with '{user_name[1:]}'")
    elif has_name == False and '*' in user_name[1:-1]:
        name_split = user_name.split('*')
        print(f"There were no babies given a name beginning with '{name_split[0]}'\
 and ending with '{name_split[1]}'")     
    
main()

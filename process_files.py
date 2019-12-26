'''
Commands 1,2,3 
Functions for reading text files
Processes the read data and creates
dictionaries to implement more functions

'''
import pickle

def load_file(filename = 'baby-names-frequency-2017.txt'):
    '''
    This function will load the file and create/return dictionaries for the names
    
    Parameters:
    string
        filename of the list of names
    Return:
    dictionary
        a dictionary for the top ten lists and the names
        
    '''
    
    filename = input(f'Enter a file name [{filename}]: ') or filename
    # Error Checking the files
    try:
        file = open(filename, 'r', encoding = 'utf-16')
        data = file.read()
        file.close()
    except:
        print('File does not exist')
        return None
    
    # Splitting data and removing unnecessary lines
    data = data.split('\n')
    for i in range(5):
        data.pop(0)
    
    # Processing data
    topTen_dict = create_topTen_dict(data)
    names_dict = create_names_dict(data)
    print('Data has been loaded and processed')

    return (topTen_dict, names_dict)
    
def create_topTen_dict(data):
    '''
    This function creates the top ten dictionary
    
    Parameters:
    list
        data of names in form of a list
    Return:
    dictionary
        the top ten dictionary
        
    '''
    
    # Creating the dictionary
    topTen_dict = {'boys': {}, 'girls': {}}
    data.pop()
    
    for line in data:
        name = line.split('\t')

        if 'Boy' in name and int(name[0]) <= 10:
            topTen_dict['boys'].setdefault(int(name[4]))
            if topTen_dict['boys'][int(name[4])] == None:
                topTen_dict['boys'][int(name[4])] = []
            topTen_dict['boys'][int(name[4])].append([int(name[0]), name[1], int(name[2])])
        elif 'Girl' in name and int(name[0]) <= 10:
            topTen_dict['girls'].setdefault(int(name[4]))
            if topTen_dict['girls'][int(name[4])] == None:
                topTen_dict['girls'][int(name[4])] = []
            topTen_dict['girls'][int(name[4])].append([int(name[0]), name[1], int(name[2])])

    return topTen_dict

def create_names_dict(data):
    '''
    This function creates the names dictionary
    
    Parameters:
    list
        data of names in form of a list
    Return
    dictionary
        the names dictionary
        
    '''
    
    # Creating the dictionary
    names_dict = {}
    for line in data:
        name = line.split('\t')
        names_dict.setdefault(name[1])
        if names_dict[name[1]] == None:
            names_dict[name[1]] = []
        names_dict[name[1]].append([int(name[2]), name[3], int(name[4])])

    return names_dict

def save_dicts(filename,topTen_dict, names_dict):
    '''
    This function saves the dictionaries with the filename
    
    Parameters:
    string, dictionary
        string of the filename and the two dictionaries
    Return:
    none
    
    '''
    
    # Saving dictionaries to filename
    bothDict = [topTen_dict, names_dict]
    pickle.dump(bothDict, open(filename, 'wb'))
    print(f'Saved pickled data in {filename}.')
    
    return None

def load_pickle(filename = 'baby_names.p'):
    '''
    This function opens the saved dictionaries
    
    Parameters:
    string
        the filename of the pickle file
    Returns:
    dictionary
        the dictionaries for the top ten lists and the names
        
    '''
    
    # Error checking the filename
    filename = input(f'Enter a file name [{filename}]: ') or filename
    try:
        both_dict = pickle.load(open(filename, 'rb'))
    except:
        print('File does not exist')
        return None
    print(f'Loaded pickled data from {filename}.')
    
    return both_dict
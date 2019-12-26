'''
Functions for graph creation


'''

from graphics import *

def draw_graph(names_dict):
    '''
    (Command 9)
    This function will draw the graph of an inputted name's trend and close
    the graph on user command
    
    Parameters:
    dictionary
        the names dictionary
    Returns:
        none
    
    '''
    
    name = input('Enter a name: ').capitalize()
    if name not in names_dict:
        print(f'There were no babies named {name} born in Alberta between 1980 and 2017')
        return None
    info = names_dict[name]
    
    # Creating the graph
    win = GraphWin(name, 1200, 800)
    
    create_axis(win,info)
    create_text(win,name)
    create_lines(win, info, name)
    
    # Closing the graph on mouse click
    win.getMouse()
    win.close()
        
    return None

def create_axis(win, info):
    ''' 
    This function will create the x and y axis for the graph
    
    Parameters
    window
        the window to draw the graph on and the list of the name info
    Returns:
    none
    
    '''
    
    # Drawing titles and lines for both x and y axis
    x_axis = Line(Point(75, 725), Point(1150,725))
    y_axis = Line(Point(75,725), Point(75,75))
    x_axis.draw(win)
    y_axis.draw(win)
    xaxis_title = Text(Point(600,775), 'Year')
    yaxis_title = Text(Point(35,60), 'Frequency')
    xaxis_title.draw(win)
    yaxis_title.draw(win)
    
    # X-axis increments
    year = 1980
    for x in range(75,1150,(1150-75)//9):
        tick = Line(Point(x,725), Point(x,730))
        tick.draw(win)
        num = Text(Point(x,740), year)
        num.draw(win)
        year += 4
    
    largest_freq = 0
    for year in info: 
        if largest_freq < year[0]:
            largest_freq = year[0]
    
    # Y-axis increments
    num = 0  

    for y in range(725,75, -(650//6)):
        tick = Line(Point(70,y), Point(75,y))
        tick.draw(win)
        if largest_freq == 1:
            freq = Text(Point(60, 75), 1)
        else:
            freq = Text(Point(60,y), num)
        freq.draw(win)
        num += largest_freq//6

    return None

def create_text(win, name):
    '''
    This function will create text for the titles of the graph
    
    Parameters:
    window, list, name
        the window for the graph and the name inputted
    Return:
    none
    
    '''
    
    # Drawing the texts for the title
    title = Text(Point(600,25), f'Trend for the name {name}')
    title.setStyle('bold')
    title.setSize(28)
    title.draw(win)
    exit = Text(Point(600,50), 'Click anywhere to close window')
    exit.setStyle('bold')
    exit.setSize(18)
    exit.setTextColor('red')
    exit.draw(win)    

def create_lines(win, info, name):
    '''
    This function will draw the trendlines for the names
    
    Parameters:
    window, list, name
        the window for the graph, the name's info in a list and the name
    Return:
    none
    
    '''
    
    # Find Largest frequency to be able to make a ratio with graph coords
    largest_freq = 0
    for year in info: 
        if largest_freq < year[0]:
            largest_freq = year[0]    
            
    win.setCoords(-75,-75,1125,725)
    binfo,ginfo = split_list(info)
    num = 0
            
    # First loop to go through boys info and girls info
    for info in (binfo,ginfo):
        start = Point(0,0)
        x = int(1075/35)
        colours = ['dark blue', 'hot pink' ]
        if len(info) != 0 and 1980 in info[0]:
            data = info.pop(0)
            start = Point(0,data[0]*650//largest_freq)
                
        # Second loop to draw the lines 
        for year in range(1981,2018):
            if len(info) != 0 and year in info[0]:
                data = info.pop(0)
                line = Line(start, Point(x,data[0]*650//largest_freq))
                start = Point(x, data[0]*650//largest_freq)
            else:
                line = Line(start, Point(x,0))
                start = Point(x,0)
                
            line.setFill(colours[num])
            line.setWidth(5-num*2)        
            line.draw(win)   
            x += int(1075/35)
        num += 1
            
    return None

def split_list(info):
    '''
    This function will split the boys and girls information into two lists
    
    Parameters:
    list
        list of the data from the names dictionary
    Returns:
    tuple
        a tuple of the two lists
    
    '''
    
    # Splitting the list into two
    ginfo = []
    binfo = []
    for data in info:
        if 'Boy' in data:
            binfo.append(data)
        elif 'Girl' in data:
            ginfo.append(data)

    return binfo,ginfo

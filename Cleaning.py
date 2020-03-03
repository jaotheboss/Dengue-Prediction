# the code here is an example, and only works for a single region.
# this is because, there'll be another function below that'll combine
# everything

# changing from text edit to lists 
file = open('') # enter the file name
lines = []
for line in file.readlines():
    lines.append(line)
header = lines.pop(0)

# make each value be a index itself
lines = list(map(lambda x: x.split(','), lines))
# remove lines that are incomplete
lines = list(filter(lambda x: x[3] != '\n', lines))
# remove the '\n' from the temperature index
for line in lines:
    line[3] = line[3][:4]
    
"""
header information (index wise)
0 == year
1 == month
2 == day
3 == Mean Temperature
"""
# convert list to dataframe
import pandas as pd
admiralty = pd.DataFrame(lines, columns = ['Year',
                                           'Month',
                                           'Day',
                                           'Mean Temperature'])

## function to convert textedit to dataframe (pandas)
import pandas as pd
import os
import datetime

# datetime.date(2010, 6, 16).isocalendar()[1]
# change date to week



## Start by looking through the directory

# files in directory
names = os.listdir()

# converts a text file into a dataframe
# works on individual locations within a region
def texttodf(filename):
    """
    function: converts a text file into a dataframe for this particular dataset
    input:    file_name
    output:   dataframe 
    """
    file = open(filename)
    lines = []
    # reads each line of the file and collates them all under 'lines'
    for line in file.readlines():
        lines.append(line)
    header = lines.pop(0)
    
    # cleans the observations 
    lines = list(map(lambda x: x.split(','), lines))
    lines = list(filter(lambda x: x[3] != '\n', lines))
    
    header = header.split(',')
    header[3] = header[3].split('\n')[0]
    
    # further cleaning based on variable name
    if header[3] == 'Daily Rainfall Total (mm)':
        for line in lines:
            line[3] = line[3].split('\n')[0]
    else:
        header[3] = 'Mean Temperature (C)'
        for line in lines:
            line[3] = line[3][:4]

    # create a dataframe out of the list
    result = pd.DataFrame(lines, columns = ['Year', 
                                            'Month', 
                                            'Day', 
                                            header[3]])
    # finding the week numbers for the observations
    week = []
    yrs = []
    for line in result.values:
        yr, wk = datetime.date(int(line[0]),
                           int(line[1]),
                           int(line[2])).isocalendar()[:2]
        # monday being the first day of the week
        week.append(wk)
        yrs.append(yr)
    result['Week No.'] = week
    result['year'] = yrs
    
    # to tally the years and week numbers with the iso calendar
    fltr = (result.loc[:,'Year'].astype(int)) == result.loc[:, 'year']
    result = result[fltr]
    
    result = result[['year', 'Week No.', header[3]]]
    result.columns = ['Year', 'Week No.', header[3]]
    
    # converting to int and float
    result['Year'] = result['Year'].astype(int)
    result['Week No.'] = result['Week No.'].astype(int)
    result[header[3]] = result[header[3]].astype(float)
    
    return result
 
# groups then averages out the values for each week
def clean(df):
    """
    function: aggregates the dataframe by their year and week, and finds the average of them
    input:    dataframe
    output:   cleaner dataframe
    """
    x = df.groupby(['Year', 'Week No.'])
    y = x.mean()
    return y

regions = ['North', 
           'North-east', 
           'East', 
           'Central', 
           'West']

# in a folder with the region folders
# we are able to access each folder to extract 
# clean data for each region
def getregiondata(region):
    """
    function:   start from an outside a folder that contains folders of each region,
                where each region folder contains files from each location in the region.
                this function will take that region folder and aggregate all the data in
                each of the location within that region and churn out a clean dataframe
    input:      the region that we want the dataframe of
    output:     cleaner dataframe
    """
    print(region)
    origin = os.getcwd() # get current directory
    os.chdir(origin + '/' + region) # change directory
    locations = os.listdir()
    
    if '.DS_Store' in locations:
        locations.remove('.DS_Store')
        
    result = texttodf(locations[0])
    #result = clean(result)
    print(locations[0])
    for location in locations[1:]:
        print(location)
        df = texttodf(location)
        #df = clean(df)
        result = result.append(df)
    #result = result.groupby(['Year', 'Week No.'])
    #result = result.mean()
    result = clean(result)
    
    os.chdir(origin) # return back to the original folder
    
    # result.reset_index(inplace = True)
    # uncomment this if you want result to be the full dataframe
    # else it'll be 1 col with row names as year and week no.
    
    export = eval(input('Do you want to export? [True/False] '))
    if export:
        result.to_csv(origin + '/clean_' + region, index = True)
        # index = True means to include the row names
     
    return result

def run1():
    for region in regions:
        getregiondata(region)
        
#### collates the weeks of the years
"""
this chunk of code basically cleans up the year files and collates them all
into 1 file
"""
# init
# adds the years to the dataframe that's only weeks of the year
os.chdir('/Users/jaoming/Downloads/IoT Datathon 3.0/Datathon Data (Clean)/incident rates')
complete = pd.read_csv('2012.csv')
year = ['2012']*52
complete['Year'] = year
complete = complete.loc[:, ['Year', 'Epidemiology Wk', 'dengue']]
complete.columns = ['Year', 'Week No.', 'Dengue (Count)']

# do it for all the years
years = ['2013', '2014', '2015', '2016', '2017', '2018', '2019']
for year in years:
    df = pd.read_csv(year + '.csv')
    yr = [year]*len(df)
    df['Year'] = yr
    df = df.loc[:, ['Year', 'Epidemiology Wk', 'dengue']]
    df.columns = ['Year', 'Week No.', 'Dengue (Count)']
    complete = complete.append(df)
    
os.chdir('/Users/jaoming/Downloads/IoT Datathon 3.0')
complete.to_csv('from_2012 (incidence)', index = False)

#### Filtering out pre-2012
os.chdir('/Users/jaoming/Downloads/IoT Datathon 3.0/Raw Data/Datathon Data (Clean)')
def fil2012():
    origin = os.getcwd()
    
    # handling rainfall
    os.chdir(origin + '/rainfall')
    file_names = list(filter(lambda x: x[:5] == 'clean', os.listdir()))
    for name in file_names:
        file = pd.read_csv(name)
        clean_file = file.loc[file.loc[:, 'Year'] >= 2012, :]
        clean_file.to_csv('/Users/jaoming/Downloads/IoT Datathon 3.0/Raw Data/from_2012 (rain)/' + name + '.csv', index = False)
    os.chdir(origin)
    
    # handling temp
    os.chdir(origin + '/temperature')
    file_names = list(filter(lambda x: x[:5] == 'clean', os.listdir()))
    for name in file_names:
        file = pd.read_csv(name)
        clean_file = file.loc[file.loc[:, 'Year'] >= 2012, :]
        clean_file.to_csv('/Users/jaoming/Downloads/IoT Datathon 3.0/Raw Data/from_2012 (temp)/' + name + '.csv', index = False)
    os.chdir(origin)


#### Getting the full data for each region
regions = ['North', 
           'North-east', 
           'East', 
           'Central', 
           'West']
os.chdir('/Users/jaoming/Downloads/IoT Datathon 3.0/Raw Data')
rain_folder = 'from_2012 (rain)'
temp_folder = 'from_2012 (temp)'

def regiondata(region):
    """
    function: collates the rainfall and temp data of that particular region, with all the years
    input:    the region of interest
    output:   dataframe
    """
    origin = os.getcwd()
    base = pd.read_csv('from_2012 (incidence)')
    # rainfall
    os.chdir(origin + '/' + rain_folder)
    rainfall = pd.read_csv('clean_' + region + '.csv')
    col_name = rainfall.columns[2]
    base[col_name] = rainfall.iloc[:, 2]
    os.chdir(origin)
    # temp
    os.chdir(origin + '/' + temp_folder)
    temp = pd.read_csv('clean_' + region + '.csv')
    col_name = temp.columns[2]
    base[col_name] = temp.iloc[:, 2]
    os.chdir(origin)
    
    # further organizing
    base = base.loc[:, ['Year', 'Week No.', 'Daily Rainfall Total (mm)', 'Mean Temperature (C)', 'Dengue (Count)']]
    # base.columns = ['Year', 'Week No.', 'Daily Rainfall Total (mm)', 'Mean Temperature (C)', 'Dengue (Count)']
    
    export = eval(input('Do you want to export? [True/False] '))
    if export:
        base.to_csv('/Users/jaoming/Downloads/IoT Datathon 3.0/' + region + '.csv', index = False)
    
    return base
    
for region in regions:
    regiondata(region)

############ After this we should have done all the cleaning for the data






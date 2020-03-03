import pandas as pd
import matplotlib.pyplot as plt
import os 

# Data extraction
origin = os.getcwd()
os.chdir(origin + '/Final Data')

north = pd.read_csv('North.csv')
east = pd.read_csv('East.csv')
north_east = pd.read_csv('North-east.csv')
central = pd.read_csv('Central.csv')
west = pd.read_csv('West.csv')
sg = pd.read_csv('Singapore (Incidence)')


## Collate and Average Regions across Singapore
summary = north.append(east)
summary = summary.append(north_east)
summary = summary.append(central)
summary = summary.append(west)

summary = summary.groupby(['Year', 'Week No.']).mean()
summary.to_csv('Singapore.csv')


## Visualizations for the different years across Singapore
sg_2012 = sg.loc[sg.loc[:, 'Year'] == 2012, :].loc[:, ['Week No.', 'Dengue (Count)']]
sg_2013 = sg.loc[sg.loc[:, 'Year'] == 2013, :].loc[:, ['Week No.', 'Dengue (Count)']]
sg_2014 = sg.loc[sg.loc[:, 'Year'] == 2014, :].loc[:, ['Week No.', 'Dengue (Count)']]
sg_2015 = sg.loc[sg.loc[:, 'Year'] == 2015, :].loc[:, ['Week No.', 'Dengue (Count)']]
sg_2016 = sg.loc[sg.loc[:, 'Year'] == 2016, :].loc[:, ['Week No.', 'Dengue (Count)']]
sg_2017 = sg.loc[sg.loc[:, 'Year'] == 2017, :].loc[:, ['Week No.', 'Dengue (Count)']]
sg_2018 = sg.loc[sg.loc[:, 'Year'] == 2018, :].loc[:, ['Week No.', 'Dengue (Count)']]
sg_2019 = sg.loc[sg.loc[:, 'Year'] == 2019, :].loc[:, ['Week No.', 'Dengue (Count)']]

def show_incidencerates():
    plt.plot(sg_2012.iloc[:, 0], sg_2012.iloc[:, 1], label = '2012')
    plt.plot(sg_2013.iloc[:, 0], sg_2013.iloc[:, 1], label = '2013')
    plt.plot(sg_2014.iloc[:, 0], sg_2014.iloc[:, 1], label = '2014')
    plt.plot(sg_2015.iloc[:, 0], sg_2015.iloc[:, 1], label = '2015')
    plt.plot(sg_2016.iloc[:, 0], sg_2016.iloc[:, 1], label = '2016')
    plt.plot(sg_2017.iloc[:, 0], sg_2017.iloc[:, 1], label = '2017')
    plt.plot(sg_2018.iloc[:, 0], sg_2018.iloc[:, 1], label = '2018')
    plt.plot(sg_2019.iloc[:, 0], sg_2019.iloc[:, 1], label = '2019')
    plt.plot(sg_2019.iloc[:, 0], [500]*len(sg_2019), label = 'Threshold', color = 'k')
    
    plt.title('Dengue Incidences over the Year [Singapore]'); plt.legend()
    plt.xlabel('Week'); plt.ylabel('Incidences')
    plt.show()  
show_incidencerates()

# This goes to show that there are 4 years between 2012 to 2019 
# that shows an outbreak of dengue fever. This is assuming that
# our threshold for an outbreak is 500 cases that happened at 
# any part of the year

## Visualization of Temp for the different region across the years
# 2012
north_2012 = north.loc[north.loc[:, 'Year'] == 2012, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
east_2012 = east.loc[east.loc[:, 'Year'] == 2012, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
north_east_2012 = north_east.loc[north_east.loc[:, 'Year'] == 2012, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
central_2012 = central.loc[central.loc[:, 'Year'] == 2012, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
west_2012 = west.loc[west.loc[:, 'Year'] == 2012, :].loc[:, ['Week No.', 'Mean Temperature (C)']]

def show_temp_2012():
    plt.plot(north_2012.iloc[:, 0], north_2012.iloc[:, 1], label = 'North')
    plt.plot(east_2012.iloc[:, 0], east_2012.iloc[:, 1], label = 'East')
    plt.plot(north_east_2012.iloc[:, 0], north_east_2012.iloc[:, 1], label = 'North-East')
    plt.plot(central_2012.iloc[:, 0], central_2012.iloc[:, 1], label = 'Central')
    plt.plot(west_2012.iloc[:, 0], west_2012.iloc[:, 1], label = 'West')
    
    plt.title('Temperature over the Regions [2012]'); plt.legend()
    plt.xlabel('Week'); plt.ylabel('Temperature (C)')
    plt.show()
show_temp_2012()

# 2013
north_2013 = north.loc[north.loc[:, 'Year'] == 2013, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
east_2013 = east.loc[east.loc[:, 'Year'] == 2013, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
north_east_2013 = north_east.loc[north_east.loc[:, 'Year'] == 2013, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
central_2013 = central.loc[central.loc[:, 'Year'] == 2013, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
west_2013 = west.loc[west.loc[:, 'Year'] == 2013, :].loc[:, ['Week No.', 'Mean Temperature (C)']]

def show_temp_2013():
    plt.plot(north_2013.iloc[:, 0], north_2013.iloc[:, 1], label = 'North')
    plt.plot(east_2013.iloc[:, 0], east_2013.iloc[:, 1], label = 'East')
    plt.plot(north_east_2013.iloc[:, 0], north_east_2013.iloc[:, 1], label = 'North-East')
    plt.plot(central_2013.iloc[:, 0], central_2013.iloc[:, 1], label = 'Central')
    plt.plot(west_2013.iloc[:, 0], west_2013.iloc[:, 1], label = 'West')
    
    plt.title('Temperature over the Regions [2013]'); plt.legend()
    plt.xlabel('Week'); plt.ylabel('Temperature (C)')
    plt.show()
show_temp_2013()

# 2014
north_2014 = north.loc[north.loc[:, 'Year'] == 2014, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
east_2014 = east.loc[east.loc[:, 'Year'] == 2014, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
north_east_2014 = north_east.loc[north_east.loc[:, 'Year'] == 2014, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
central_2014 = central.loc[central.loc[:, 'Year'] == 2014, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
west_2014 = west.loc[west.loc[:, 'Year'] == 2014, :].loc[:, ['Week No.', 'Mean Temperature (C)']]

def show_temp_2014():
    plt.plot(north_2014.iloc[:, 0], north_2014.iloc[:, 1], label = 'North')
    plt.plot(east_2014.iloc[:, 0], east_2014.iloc[:, 1], label = 'East')
    plt.plot(north_east_2014.iloc[:, 0], north_east_2014.iloc[:, 1], label = 'North-East')
    plt.plot(central_2014.iloc[:, 0], central_2014.iloc[:, 1], label = 'Central')
    plt.plot(west_2014.iloc[:, 0], west_2014.iloc[:, 1], label = 'West')
    
    plt.title('Temperature over the Regions [2014]'); plt.legend()
    plt.xlabel('Week'); plt.ylabel('Temperature (C)')
    plt.show()
show_temp_2014()

# 2015
north_2015 = north.loc[north.loc[:, 'Year'] == 2015, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
east_2015 = east.loc[east.loc[:, 'Year'] == 2015, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
north_east_2015 = north_east.loc[north_east.loc[:, 'Year'] == 2015, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
central_2015 = central.loc[central.loc[:, 'Year'] == 2015, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
west_2015 = west.loc[west.loc[:, 'Year'] == 2015, :].loc[:, ['Week No.', 'Mean Temperature (C)']]

def show_temp_2015():
    plt.plot(north_2015.iloc[:, 0], north_2015.iloc[:, 1], label = 'North')
    plt.plot(east_2015.iloc[:, 0], east_2015.iloc[:, 1], label = 'East')
    plt.plot(north_east_2015.iloc[:, 0], north_east_2015.iloc[:, 1], label = 'North-East')
    plt.plot(central_2015.iloc[:, 0], central_2015.iloc[:, 1], label = 'Central')
    plt.plot(west_2015.iloc[:, 0], west_2015.iloc[:, 1], label = 'West')
    
    plt.title('Temperature over the Regions [2015]'); plt.legend()
    plt.xlabel('Week'); plt.ylabel('Temperature (C)')
    plt.show()
show_temp_2015()

# 2016
north_2016 = north.loc[north.loc[:, 'Year'] == 2016, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
east_2016 = east.loc[east.loc[:, 'Year'] == 2016, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
north_east_2016 = north_east.loc[north_east.loc[:, 'Year'] == 2016, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
central_2016 = central.loc[central.loc[:, 'Year'] == 2016, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
west_2016 = west.loc[west.loc[:, 'Year'] == 2016, :].loc[:, ['Week No.', 'Mean Temperature (C)']]

def show_temp_2016():
    plt.plot(north_2016.iloc[:, 0], north_2016.iloc[:, 1], label = 'North')
    plt.plot(east_2016.iloc[:, 0], east_2016.iloc[:, 1], label = 'East')
    plt.plot(north_east_2016.iloc[:, 0], north_east_2016.iloc[:, 1], label = 'North-East')
    plt.plot(central_2016.iloc[:, 0], central_2016.iloc[:, 1], label = 'Central')
    plt.plot(west_2016.iloc[:, 0], west_2016.iloc[:, 1], label = 'West')
    
    plt.title('Temperature over the Regions [2016]'); plt.legend()
    plt.xlabel('Week'); plt.ylabel('Temperature (C)')
    plt.show()
show_temp_2016()

# 2017
north_2017 = north.loc[north.loc[:, 'Year'] == 2017, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
east_2017 = east.loc[east.loc[:, 'Year'] == 2017, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
north_east_2017 = north_east.loc[north_east.loc[:, 'Year'] == 2017, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
central_2017 = central.loc[central.loc[:, 'Year'] == 2017, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
west_2017 = west.loc[west.loc[:, 'Year'] == 2017, :].loc[:, ['Week No.', 'Mean Temperature (C)']]

def show_temp_2017():
    plt.plot(north_2017.iloc[:, 0], north_2017.iloc[:, 1], label = 'North')
    plt.plot(east_2017.iloc[:, 0], east_2017.iloc[:, 1], label = 'East')
    plt.plot(north_east_2017.iloc[:, 0], north_east_2017.iloc[:, 1], label = 'North-East')
    plt.plot(central_2017.iloc[:, 0], central_2017.iloc[:, 1], label = 'Central')
    plt.plot(west_2017.iloc[:, 0], west_2017.iloc[:, 1], label = 'West')
    
    plt.title('Temperature over the Regions [2017]'); plt.legend()
    plt.xlabel('Week'); plt.ylabel('Temperature (C)')
    plt.show()
show_temp_2017()

# 2018
north_2018 = north.loc[north.loc[:, 'Year'] == 2018, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
east_2018 = east.loc[east.loc[:, 'Year'] == 2018, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
north_east_2018 = north_east.loc[north_east.loc[:, 'Year'] == 2018, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
central_2018 = central.loc[central.loc[:, 'Year'] == 2018, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
west_2018 = west.loc[west.loc[:, 'Year'] == 2018, :].loc[:, ['Week No.', 'Mean Temperature (C)']]

def show_temp_2018():
    plt.plot(north_2018.iloc[:, 0], north_2018.iloc[:, 1], label = 'North')
    plt.plot(east_2018.iloc[:, 0], east_2018.iloc[:, 1], label = 'East')
    plt.plot(north_east_2018.iloc[:, 0], north_east_2018.iloc[:, 1], label = 'North-East')
    plt.plot(central_2018.iloc[:, 0], central_2018.iloc[:, 1], label = 'Central')
    plt.plot(west_2018.iloc[:, 0], west_2018.iloc[:, 1], label = 'West')
    
    plt.title('Temperature over the Regions [2018]'); plt.legend()
    plt.xlabel('Week'); plt.ylabel('Temperature (C)')
    plt.show()
show_temp_2018()

# 2019
north_2019 = north.loc[north.loc[:, 'Year'] == 2019, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
east_2019 = east.loc[east.loc[:, 'Year'] == 2019, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
north_east_2019 = north_east.loc[north_east.loc[:, 'Year'] == 2019, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
central_2019 = central.loc[central.loc[:, 'Year'] == 2019, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
west_2019 = west.loc[west.loc[:, 'Year'] == 2019, :].loc[:, ['Week No.', 'Mean Temperature (C)']]

def show_temp_2019():
    plt.plot(north_2019.iloc[:, 0], north_2019.iloc[:, 1], label = 'North')
    plt.plot(east_2019.iloc[:, 0], east_2019.iloc[:, 1], label = 'East')
    plt.plot(north_east_2019.iloc[:, 0], north_east_2019.iloc[:, 1], label = 'North-East')
    plt.plot(central_2019.iloc[:, 0], central_2019.iloc[:, 1], label = 'Central')
    plt.plot(west_2019.iloc[:, 0], west_2019.iloc[:, 1], label = 'West')
    
    plt.title('Temperature over the Regions [2019]'); plt.legend()
    plt.xlabel('Week'); plt.ylabel('Temperature (C)')
    plt.show()
show_temp_2019()


## Visualization of Rainfall for the different region across the years
# 2012
north_2012 = north.loc[north.loc[:, 'Year'] == 2012, :].loc[:, ['Week No.', 'Daily Rainfall Total (mm)']]
east_2012 = east.loc[east.loc[:, 'Year'] == 2012, :].loc[:, ['Week No.', 'Daily Rainfall Total (mm)']]
north_east_2012 = north_east.loc[north_east.loc[:, 'Year'] == 2012, :].loc[:, ['Week No.', 'Daily Rainfall Total (mm)']]
central_2012 = central.loc[central.loc[:, 'Year'] == 2012, :].loc[:, ['Week No.', 'Daily Rainfall Total (mm)']]
west_2012 = west.loc[west.loc[:, 'Year'] == 2012, :].loc[:, ['Week No.', 'Daily Rainfall Total (mm)']]

def show_rainfall_2012():
    plt.plot(north_2012.iloc[:, 0], north_2012.iloc[:, 1], label = 'North')
    plt.plot(east_2012.iloc[:, 0], east_2012.iloc[:, 1], label = 'East')
    plt.plot(north_east_2012.iloc[:, 0], north_east_2012.iloc[:, 1], label = 'North-East')
    plt.plot(central_2012.iloc[:, 0], central_2012.iloc[:, 1], label = 'Central')
    plt.plot(west_2012.iloc[:, 0], west_2012.iloc[:, 1], label = 'West')
    
    plt.title('Temperature over the Regions [2012]'); plt.legend()
    plt.xlabel('Week'); plt.ylabel('Rainfall (mm)')
    plt.show()
show_rainfall_2012()

# 2013
north_2013 = north.loc[north.loc[:, 'Year'] == 2013, :].loc[:, ['Week No.', 'Daily Rainfall Total (mm)']]
east_2013 = east.loc[east.loc[:, 'Year'] == 2013, :].loc[:, ['Week No.', 'Daily Rainfall Total (mm)']]
north_east_2013 = north_east.loc[north_east.loc[:, 'Year'] == 2013, :].loc[:, ['Week No.', 'Daily Rainfall Total (mm)']]
central_2013 = central.loc[central.loc[:, 'Year'] == 2013, :].loc[:, ['Week No.', 'Daily Rainfall Total (mm)']]
west_2013 = west.loc[west.loc[:, 'Year'] == 2013, :].loc[:, ['Week No.', 'Daily Rainfall Total (mm)']]

def show_rainfall_2013():
    plt.plot(north_2013.iloc[:, 0], north_2013.iloc[:, 1], label = 'North')
    plt.plot(east_2013.iloc[:, 0], east_2013.iloc[:, 1], label = 'East')
    plt.plot(north_east_2013.iloc[:, 0], north_east_2013.iloc[:, 1], label = 'North-East')
    plt.plot(central_2013.iloc[:, 0], central_2013.iloc[:, 1], label = 'Central')
    plt.plot(west_2013.iloc[:, 0], west_2013.iloc[:, 1], label = 'West')
    
    plt.title('Temperature over the Regions [2013]'); plt.legend()
    plt.xlabel('Week'); plt.ylabel('Rainfall (mm)')
    plt.show()
show_rainfall_2013()

# 2014
north_2014 = north.loc[north.loc[:, 'Year'] == 2014, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
east_2014 = east.loc[east.loc[:, 'Year'] == 2014, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
north_east_2014 = north_east.loc[north_east.loc[:, 'Year'] == 2014, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
central_2014 = central.loc[central.loc[:, 'Year'] == 2014, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
west_2014 = west.loc[west.loc[:, 'Year'] == 2014, :].loc[:, ['Week No.', 'Mean Temperature (C)']]

def show_temp_2014():
    plt.plot(north_2014.iloc[:, 0], north_2014.iloc[:, 1], label = 'North')
    plt.plot(east_2014.iloc[:, 0], east_2014.iloc[:, 1], label = 'East')
    plt.plot(north_east_2014.iloc[:, 0], north_east_2014.iloc[:, 1], label = 'North-East')
    plt.plot(central_2014.iloc[:, 0], central_2014.iloc[:, 1], label = 'Central')
    plt.plot(west_2014.iloc[:, 0], west_2014.iloc[:, 1], label = 'West')
    
    plt.title('Temperature over the Regions [2014]'); plt.legend()
    plt.xlabel('Week'); plt.ylabel('Temperature (C)')
    plt.show()
show_temp_2014()

# 2015
north_2015 = north.loc[north.loc[:, 'Year'] == 2015, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
east_2015 = east.loc[east.loc[:, 'Year'] == 2015, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
north_east_2015 = north_east.loc[north_east.loc[:, 'Year'] == 2015, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
central_2015 = central.loc[central.loc[:, 'Year'] == 2015, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
west_2015 = west.loc[west.loc[:, 'Year'] == 2015, :].loc[:, ['Week No.', 'Mean Temperature (C)']]

def show_temp_2015():
    plt.plot(north_2015.iloc[:, 0], north_2015.iloc[:, 1], label = 'North')
    plt.plot(east_2015.iloc[:, 0], east_2015.iloc[:, 1], label = 'East')
    plt.plot(north_east_2015.iloc[:, 0], north_east_2015.iloc[:, 1], label = 'North-East')
    plt.plot(central_2015.iloc[:, 0], central_2015.iloc[:, 1], label = 'Central')
    plt.plot(west_2015.iloc[:, 0], west_2015.iloc[:, 1], label = 'West')
    
    plt.title('Temperature over the Regions [2015]'); plt.legend()
    plt.xlabel('Week'); plt.ylabel('Temperature (C)')
    plt.show()
show_temp_2015()

# 2016
north_2016 = north.loc[north.loc[:, 'Year'] == 2016, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
east_2016 = east.loc[east.loc[:, 'Year'] == 2016, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
north_east_2016 = north_east.loc[north_east.loc[:, 'Year'] == 2016, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
central_2016 = central.loc[central.loc[:, 'Year'] == 2016, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
west_2016 = west.loc[west.loc[:, 'Year'] == 2016, :].loc[:, ['Week No.', 'Mean Temperature (C)']]

def show_temp_2016():
    plt.plot(north_2016.iloc[:, 0], north_2016.iloc[:, 1], label = 'North')
    plt.plot(east_2016.iloc[:, 0], east_2016.iloc[:, 1], label = 'East')
    plt.plot(north_east_2016.iloc[:, 0], north_east_2016.iloc[:, 1], label = 'North-East')
    plt.plot(central_2016.iloc[:, 0], central_2016.iloc[:, 1], label = 'Central')
    plt.plot(west_2016.iloc[:, 0], west_2016.iloc[:, 1], label = 'West')
    
    plt.title('Temperature over the Regions [2016]'); plt.legend()
    plt.xlabel('Week'); plt.ylabel('Temperature (C)')
    plt.show()
show_temp_2016()

# 2017
north_2017 = north.loc[north.loc[:, 'Year'] == 2017, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
east_2017 = east.loc[east.loc[:, 'Year'] == 2017, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
north_east_2017 = north_east.loc[north_east.loc[:, 'Year'] == 2017, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
central_2017 = central.loc[central.loc[:, 'Year'] == 2017, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
west_2017 = west.loc[west.loc[:, 'Year'] == 2017, :].loc[:, ['Week No.', 'Mean Temperature (C)']]

def show_temp_2017():
    plt.plot(north_2017.iloc[:, 0], north_2017.iloc[:, 1], label = 'North')
    plt.plot(east_2017.iloc[:, 0], east_2017.iloc[:, 1], label = 'East')
    plt.plot(north_east_2017.iloc[:, 0], north_east_2017.iloc[:, 1], label = 'North-East')
    plt.plot(central_2017.iloc[:, 0], central_2017.iloc[:, 1], label = 'Central')
    plt.plot(west_2017.iloc[:, 0], west_2017.iloc[:, 1], label = 'West')
    
    plt.title('Temperature over the Regions [2017]'); plt.legend()
    plt.xlabel('Week'); plt.ylabel('Temperature (C)')
    plt.show()
show_temp_2017()

# 2018
north_2018 = north.loc[north.loc[:, 'Year'] == 2018, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
east_2018 = east.loc[east.loc[:, 'Year'] == 2018, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
north_east_2018 = north_east.loc[north_east.loc[:, 'Year'] == 2018, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
central_2018 = central.loc[central.loc[:, 'Year'] == 2018, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
west_2018 = west.loc[west.loc[:, 'Year'] == 2018, :].loc[:, ['Week No.', 'Mean Temperature (C)']]

def show_temp_2018():
    plt.plot(north_2018.iloc[:, 0], north_2018.iloc[:, 1], label = 'North')
    plt.plot(east_2018.iloc[:, 0], east_2018.iloc[:, 1], label = 'East')
    plt.plot(north_east_2018.iloc[:, 0], north_east_2018.iloc[:, 1], label = 'North-East')
    plt.plot(central_2018.iloc[:, 0], central_2018.iloc[:, 1], label = 'Central')
    plt.plot(west_2018.iloc[:, 0], west_2018.iloc[:, 1], label = 'West')
    
    plt.title('Temperature over the Regions [2018]'); plt.legend()
    plt.xlabel('Week'); plt.ylabel('Temperature (C)')
    plt.show()
show_temp_2018()

# 2019
north_2019 = north.loc[north.loc[:, 'Year'] == 2019, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
east_2019 = east.loc[east.loc[:, 'Year'] == 2019, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
north_east_2019 = north_east.loc[north_east.loc[:, 'Year'] == 2019, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
central_2019 = central.loc[central.loc[:, 'Year'] == 2019, :].loc[:, ['Week No.', 'Mean Temperature (C)']]
west_2019 = west.loc[west.loc[:, 'Year'] == 2019, :].loc[:, ['Week No.', 'Mean Temperature (C)']]

def show_temp_2019():
    plt.plot(north_2019.iloc[:, 0], north_2019.iloc[:, 1], label = 'North')
    plt.plot(east_2019.iloc[:, 0], east_2019.iloc[:, 1], label = 'East')
    plt.plot(north_east_2019.iloc[:, 0], north_east_2019.iloc[:, 1], label = 'North-East')
    plt.plot(central_2019.iloc[:, 0], central_2019.iloc[:, 1], label = 'Central')
    plt.plot(west_2019.iloc[:, 0], west_2019.iloc[:, 1], label = 'West')
    
    plt.title('Temperature over the Regions [2019]'); plt.legend()
    plt.xlabel('Week'); plt.ylabel('Temperature (C)')
    plt.show()
show_temp_2019()








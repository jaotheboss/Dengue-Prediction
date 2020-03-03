# Dengue-Prediction
These codes are specific to Singapore. Given a dataset about dengue occurrences in Singapore, alongside data of a particular region's temperature and rainfall, we are to attempt to train a model that could predict dengue occurrences in the future, given just the rainfall and temperature as well.

# Contents in this Repo:
    1. Cleaning.py
    Bulk of it is codes just to clean the dataset. As explained in the methodology.
    
    2. Data Visualization.py
    To visualise the data. This is simply for data exploration. There're a ton of ways to visualise the data.
    
    3. Models.py
    The models that were used to predict whether or not a new region/location would have dengue, solely based on the temperature and the rainfall.

# Conclusion:
    1. There is simply not enough data to conclude anything (We need either more observations or more variable to play around with)
    2. Time Series models are not the same as the conventional models that i have used in this project. 
    3. Veracity of the dataset would have been the key to success
    
# Methodology:
    1. We started by cleaning the dataset
    Most of the data were separated into different folders and contain different kinds of data. In their individual years, only in certain regions, only containing rainfall and the weeks of the year, etc.
    This was the most troublesome part of the project. 
    
    2. Decided to visualise the data, just to see if there were any kinds of conclusions that could be deduced
    Most of the visualizations are just simple graphs. There's a chance i might revisit this project after learning new visualization tools just to play around with it.
    
    3. Modelling
    I've tried out a few kinds of models, but didn't get into the tweaking of parameters as much.
    Models that i've tried are as follows: k-Nearest Neighbours, Logistic Regression, Decision Trees and XGBoost (Ensemble Method)

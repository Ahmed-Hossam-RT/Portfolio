import pandas as pd 
import numpy as np 


import warnings
warnings.filterwarnings('ignore',category=FutureWarning) # Display all warnings

# reading the file 

file_path="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
headers= ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
data=pd.read_csv(file_path,names=headers)
print(data.head())

# data cleaning 
# 1- dealing with the missing nan values 

data.replace('?',np.nan,inplace=True)


# checking for missing values in columns
missing_data=data.isnull()


for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print('')

# replacing missing values with mean 

# normalized losses
average_norm=data['normalized-losses'].astype('float').mean(axis=0)
data["normalized-losses"].replace(np.nan,average_norm,inplace=True)

# stroke column
avg_stroke=data['stroke'].astype('float').mean(axis=0)
data["stroke"]=data["stroke"].replace(np.nan,avg_stroke,inplace=True)

# bore column
avg_bore=data['bore'].astype('float').mean(axis=0)
data["bore"].replace(np.nan,avg_bore,inplace=True)

# horse power 
avg_horsepower=data['horsepower'].astype('float').mean(axis=0)
data["horsepower"].replace(np.nan,avg_horsepower,inplace=True)

# peak-rpm column
avg_peak_rpm=data['peak-rpm'].astype('float').mean(axis=0)
data["peak-rpm"].replace(np.nan,avg_peak_rpm,inplace=True)


# num-of-doors column -------> replace by most frequent as it's categorical
most_fruequent_door=data['num-of-doors'].value_counts().idxmax()
data["num-of-doors"].replace(np.nan,most_fruequent_door,inplace=True)

# dropping rows with nan values in price column 
data.dropna(subset=['price'],inplace=True)
data.reset_index(drop=True,inplace=True)

# convert data types to porper ones 
data[["bore", "stroke"]] = data[["bore", "stroke"]].astype("float")
data[["normalized-losses"]] = data[["normalized-losses"]].astype("int")
data[["price"]] = data[["price"]].astype("float")
data[["peak-rpm"]] = data[["peak-rpm"]].astype("float")


# ----- Data formatting -----
# changing the highway and city mpg to l/100

data['highway-mpg']=235/data["highway-mpg"]
data.rename(columns={"highway-mpg":'highway-L/100'},inplace=True)

data['city-mpg']=235/data['city-mpg']
data.rename(columns={'city-mpg':'city-L/100'},inplace=True)

# Data binning 
data["horsepower"]=data["horsepower"].astype(int, copy=True)
bins=np.linspace(data['horsepower'].min(),data['horsepower'].max(),4)
group_names = ['Low', 'Medium', 'High']
data['horsepower_binned']=pd.cut(data['horsepower'],bins,labels=group_names,include_lowest=True)
print(data['horsepower_binned'].value_counts())
# ----------------------------------------------------------------------------------------------------------


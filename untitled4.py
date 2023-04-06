# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 23:27:21 2023

@author: User
"""

import pandas as pds
import numpy as npy
import matplotlib.pyplot as mplt
import scipy.stats as stats

def file(Name):
    """
    Parameters
    ----------
    Name : Name indicates the given file name to acess the data in order to
           run code with using function

    Returns
    -------
    None.

    """
    data = pds.read_csv(Name)
    data_1 = data
    data_1 = data_1.drop(columns=["Series Code", "Country Code"], axis=1)
    data_1 = data.transpose()
    #data_1 = data_1.set_index("Series Name", inplace=True)
    return data, data_1

Name = "C:/Users/User/Downloads/ADS 2 (World Data Bank).csv"
data,data_1 = file(Name)
print("1111111")
print(data.head())
print("22222")
print(data_1.head())

"""
Getting information about given data and data1
"""
print(data.info())
print(data_1.info())

def clean(x):

    # count the number of missing values in each column of the DataFrame
    x.isnull().sum()
    # fill any missing values with 0 and update the DataFrame in place
    x.fillna(0, inplace=True)

    return

clean(data)

data = data.drop(columns=["Series Code", "Country Code"], axis=1)
print("3333333")

gdata_1 = data.loc[data["Series Name"] == "Population, total"]
gdata_1 = gdata_1.drop(["Series Name"], axis=1)

# drop the value of not given in data
gdata_1.dropna()

gdata_1 = gdata_1.iloc[[0,3,8,7,14,16,17,18],
                       [0,1,6,11,16]].reset_index(drop=True)
gdata_1 = gdata_1.sort_values("2015 [YR2015]", 
                              ascending=True, ignore_index=True)
print(gdata_1.iloc[0,1])

def barplot1():
    """
    plotting barplot using different parameters

    Returns
    -------
    None.

    """
    mplt.figure(figsize=(20, 10))
    N = 8
    ind = npy.arange(N)
    width = 0.20
    
    """
    plot 4 barplot e.g. bar1, bar2, bar3 and bar4
    """
    
    wvals = x["2000 [YR2000]"]
    bar1 = mplt.bar(ind, wvals, width, color='g')
    
    xvals = x["2005 [YR2005]"]
    bar2 = mplt.bar(ind+width, xvals, width, color = 'y')

    yvals = x["2010 [YR2010]"]
    bar3 = mplt.bar(ind+width*2, yvals, width, color = 'b')
    
    zvals = x["2015 [YR2015]"]
    bar4 = mplt.bar(ind+width*3, zvals, width, color = 'r')
    
    """plot the labels, title and different parameters for given barplot
    """

    mplt.xlabel("country Name", size = 30)
    mplt.ylabel("Population", size = 25)
    mplt.title("Population of countries in different year", 
              size = 50)
    
    mplt.xticks(ind+width, x["Country Name"])
    mplt.xticks(minor = False, ha = "right")
    mplt.tick_params(axis='x', labelsize = 20, labelrotation = 35)
    mplt.tick_params(axis='y', labelsize = 30, )
    mplt.legend((bar1, bar2, bar3, bar4), ('2000', '2005','2010','2015'),
               prop = {"size":25})
    mplt.show()
    mplt.savefig("barplot1.png")
    
""" Example for barplot
"""
x = gdata_1
barplot1()



print(gdata_1)
gdata_1_mean = gdata_1.groupby(["Country Name"]).mean()
print(gdata_1_mean)
gdata_1_describe = gdata_1_mean.describe()
print(print(gdata_1_describe))

print ("skewness", stats.skew(gdata_1_mean))
print ("kurtosis", stats.kurtosis(gdata_1_mean))


gdata_2 = data.loc[data["Series Name"] ==
                   "CO2 emissions (metric tons per capita)"]
gdata_2 = gdata_2.drop(["Series Name"], axis=1)
print(gdata_2)

# drop the value of not given in data
gdata_2.dropna()

gdata_2 = gdata_2.iloc[[0,3,8,7,14,16,17,18],
                       [0,1,6,11,16]].reset_index(drop=True)




def barplot2():
    """
    plotting barplot using different parameters

    Returns
    -------
    None.

    """
    mplt.figure(figsize=(20, 10))
    N = 8
    ind = npy.arange(N)
    width = 0.20
    
    """
    plot 4 barplot e.g. bar1, bar2, bar3 and bar4
    """
    
    wvals1 = y["2000 [YR2000]"]
    bar1 = mplt.bar(ind, wvals1, width, color='g')
    
    xvals1 = y["2005 [YR2005]"]
    bar2 = mplt.bar(ind+width, xvals1, width, color = 'y')

    yvals1 = y["2010 [YR2010]"]
    bar3 = mplt.bar(ind+width*2, yvals1, width, color = 'b')
    
    zvals1 = y["2015 [YR2015]"]
    bar4 = mplt.bar(ind+width*3, zvals1, width, color = 'r')
    
    """plot the labels, title and different parameters for given barplot
    """

    mplt.xlabel("country Name", size = 30)
    mplt.ylabel("CO2 emissions (metric tons per capita)", size = 25)
    mplt.title("CO2 emissions (metric tons per capita) in different year", 
               size = 50)
    mplt.tick_params(axis='x', labelsize = 20, labelrotation = 35)
    mplt.tick_params(axis='y', labelsize = 30)
    mplt.legend((bar1, bar2, bar3, bar4), ('2000', '2005','2010','2015'),
               prop = {"size":25})
    mplt.xticks(ind+width, x["Country Name"])
    mplt.xticks(minor = False, ha = "right")
    mplt.legend((bar1, bar2, bar3, bar4), ('2000', '2005','2010','2015'),
               prop = {"size":25})
    
    mplt.savefig("barplot2.png")
    
""" Example for barplot
"""
y = gdata_2
barplot2()


print(gdata_2)
gdata_2_mean = gdata_2.groupby(["Country Name"]).mean()
print(gdata_2_mean)
gdata_2_describe = gdata_2_mean.describe()
print(print(gdata_2_describe))

print ("skewness", stats.skew(gdata_2_mean))
print ("kurtosis", stats.kurtosis(gdata_2_mean))













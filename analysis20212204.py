#Filename:  analysis.py
#Author:    Mark Parry
#Created:   23/03/2021
#Purpose:   An analysis of the Iris data set

#https://datascience-enthusiast.com/R/pandas_datatable.html  comparison of pandas and R
#http://www.cse.msu.edu/~ptan/dmbook/tutorials/tutorial3/tutorial3.html
#https://pandas.pydata.org/docs/reference/frame.html

import matplotlib.pyplot as mpl 
import numpy as np
import pandas as pd

#read in the csv file of values
data = pd.read_csv('iris.data',header=None)

#give the values a header column as there was no header in the csv file
data.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']

#me messing
#measures = data.columns[:-1]
#print(measures)
#input("press any key")
#print(data.head())
#print(data.tail())
#print(data.describe())

#print(type(data))
#print(list(data))
#print(data.dtypes)
#print(data["class"].drop_duplicates())

#get the unique values in the classes column
classes = data["class"].unique()

#loop through the dataframe for each class
for iclass in classes:
     print(iclass)
     #loop through the measurements excluding the class column
     for measure in data.columns[:-1]:
          print(data[data['class']==iclass][[measure]])
          mpl_data = data[data['class']==iclass][[measure]]
          mpl.hist(mpl_data)
          #Give the histograms a title,change the numbering on the x axis,label both axes, display the legend to note which plot is which(rgb)
          mpl.title(iclass + " Histogram") 
          #mpl.xticks([0,1,2,3,4])
          mpl.xlabel(measure) 
          #mpl.ylabel("y Axis") 
          #mpl.legend() 
          mpl.show()

#add scatterdiagrams for each pair ([sepal length,width][petal length,width] for each class (6 diagrams in all)


#print(data['sepal length'])
#setosa_sl = data.loc[0:49, ['sepal length']]
#print(data.query('class =="Iris-setosa"'))  #returning error
#print(data[data['class']=="Iris-setosa"])
#print(data[data['class']=="Iris-setosa"][['sepal length']])
#mpl.hist(setosa_sl)
#mpl.show()

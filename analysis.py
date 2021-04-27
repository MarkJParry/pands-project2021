#Filename:  analysis.py
#Author:    Mark Parry
#Created:   23/03/2021
#Modified:  26/04/2021   by Mark Parry
#Purpose:   An analysis of the Iris data set

#https://datascience-enthusiast.com/R/pandas_datatable.html  comparison of pandas and R
#http://www.cse.msu.edu/~ptan/dmbook/tutorials/tutorial3/tutorial3.html
#https://pandas.pydata.org/docs/reference/frame.html

import matplotlib.pyplot as mpl 
#import numpy as np
import pandas as pd

def initialise():
     #read in the csv file of values
     data = pd.read_csv('iris.data',header=None)

     #give the values a header column as there was no header in the csv file
     data.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

     #set up an array of measures only exclude the species column
     measures = data.columns[:-1]

     #get the unique values in the species column
     iris_species = data["species"].unique()
     #print(iris_species)

     #assign a colour to each species
     colors = {iris_species[0]:"purple",iris_species[1]:"red",iris_species[2]:"blue"}

     return(data,measures,colors,iris_species)

def output_textfiles(data):
     #save the output of the describe function of the dataframe to a text file 
     with open('describe.txt', 'w') as outfile:
          print('\nOutput from the data describe function', file=outfile)
          print(data.describe(),file=outfile)

     #save the output of the correlation function to a text file
     with open('correlation.txt', 'w') as outfile:
          print('\nOutput from the data correlation function', file=outfile)
          print(data.corr(),file=outfile)



''' not used in this program but useful to get info on data set
#input("pause")
#print(type(data))
#print(list(data))
#print(data.dtypes)
#have a look at the top of the dataframe
#print(data.head())

#have a look a the bottom
#print(data.tail())
'''




#function to print box plots  for the data set
#this will loop through the species and within that loop, loop through the measures
#plot the measure for each species on one graph and save that to a file
def plot_box():
     #loop through the dataframe for each species
     for species in iris_species:
          #print(species)
          #initialise a list to be used when plotting
          mpl_dataset = []
          for measure in measures:
               #print(measure)
               #initilise an array for each subset
               mpl_data = []
               mpl_data = data[data['species']==species][measure]
               #add the subset to the plot set
               mpl_dataset.append(mpl_data)
               #mpl.xlabel(species) 
               mpl.ylabel("count") 
          mpl.title("Boxplots for "+ species + " measures")
          mpl.boxplot(mpl_dataset,labels=measures)
          #save the plots to file
          mpl.savefig(species + ".png")
          #display the plots
          mpl.show()


#function to print scatter plots for the data set
#this is called by a routine that passes in the combination of measures to be plotted(x,y)
#plot the measure for each species on one graph and save that to a file
def plot_scatter(measure1,measure2):
     #loop throuh the species
     for species in iris_species:

          x = data[data['species']==species][measure1]
          y = data[data['species']==species][measure2]

          mpl.scatter(x,y,color=colors[species],label=species,alpha=.5)

          mpl.xlabel(measure1)
          mpl.ylabel(measure2)
          mpl.title('Iris Dataset (' + measure1 + " vs  " + measure2 + ")")
          mpl.legend()
     #save the plots to disk
     mpl.savefig(measure1 + "_" + measure2 + ".png")
     #display the plots
     mpl.show()


if __name__ == "__main__":
     #import data, set up the four measurements,three species,colours for plots
     data,measures,colors,iris_species = initialise()

     #output the describe and correlation data to textfiles
     output_textfiles(data)

     #call the histrogram function
     plot_hist()

     #call function to plot scatterplots for possible unique combinations of two measures(4 measures pick two = 4*3/2*1 = 6)
     for i in range (0,4):
          for j in range(i+1,4):
               plot_scatter(measures[i],measures[j])

     #call the box plot function
     plot_box()




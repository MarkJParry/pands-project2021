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
data.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
measures = data.columns[:-1]
#get the unique values in the species column
iris_species = data["species"].unique()
print(iris_species)
#assign a colour to each species
colors = {iris_species[0]:"purple",iris_species[1]:"red",iris_species[2]:"blue"}
#input(colors)
#input(data)
#me messing
#measures = data.columns[:-1]
#print(measures)
#input("press any key")
#print(data.head())
#print(data.tail())
with open('describe.txt', 'a') as outfile:
     print('\nOutput from the data describe function', file=outfile)
     print(data.describe(),file=outfile)
#input("pause")
with open('correlation.txt', 'a') as outfile:
     print('\nOutput from the data correlation function', file=outfile)
     print(data.corr(),file=outfile)
#
# input("pause")


#mpl.hist(data['sepal_length'],bins=8)
#mpl.show()
#input("pause")

#mpl.hist(data[data['species']=='Iris-setosa'][['sepal_length']])
#a = []
#a.append(data[data['species']=='Iris-setosa'][['sepal_length']])
#ris_df[iris_df['species_name'] == 'Setosa']['petal_length']
a = data[data['species']=='Iris-setosa']['sepal_length']
#print(a)
input("pause")
#print(a.shape)

b = data[data['species']=='Iris-versicolor']['sepal_length']
#print(b)
#input("pause")
c = data[data['species']=='Iris-virginica']['sepal_length']
mpl_dataset = [a,b,c]
fig, ax = mpl.subplots(figsize=(12, 7))
ax.yaxis.set_ticks_position('none')
# Add major gridlines in the y-axis
ax.grid(color='grey', axis='y', linestyle='-', linewidth=0.25, alpha=0.5)
# Set plot title
ax.set_title('Distribution of sepal_length by species')
ax.boxplot(mpl_dataset,labels=iris_species)

mpl.show()
#input("pause")
#print(type(data))
#print(list(data))
#print(data.dtypes)
#print(data["class"].drop_duplicates())


def plot_hist():
     #loop through the measurements excluding the species column
     for measure in measures:
          #print(measure)
          
          #loop through the dataframe for each species
          for species in iris_species:
               #print(data[data['class']==iclass][[measure]])
               mpl_data = data[data['species']==species][measure]
               mpl.hist(mpl_data,color=colors[species],label=species,alpha=.5,histtype="step")
               #Give the histograms a title,change the numbering on the x axis,label both axes, display the legend to note which plot is which(rgb)                    mpl.title("Iris Dataset " + measure + " Histogram") 
               #mpl.xticks([0,1,2,3,4])
               mpl.xlabel(measure) 
               mpl.ylabel("count") 
               mpl.legend() 
               mpl.title("Title")
               #mpl.savefig(measure + ".png")
          mpl.show()
#boxplot
#mpl.figure(figsize = (10, 7))
#mpl_data = data[data.columns[:-1]] whole set
#mpl.boxplot(mpl_data)
def plot_box():
     #loop through the dataframe for each species

     
     for species in iris_species:
          print(species)
          mpl_dataset = []
          for measure in measures:
               print(measure)
               mpl_data = []
               #print(data[data['species']==species][[measure]])
               #input ("pause")
               mpl_data = data[data['species']==species][measure]
               mpl_dataset.append(mpl_data)
               #print(mpl_dataset)
               #input ("pause")
               #mpl.xlabel(species) 
               mpl.ylabel("count") 
               #mpl.boxplot(mpl_dataset,labels=data.columns[:-1])
          mpl.title("Boxplots for "+ species + " measures")
          mpl.boxplot(mpl_dataset,labels=data.columns[:-1])
          mpl.savefig(species + ".png")
          mpl.show()

def plot_scatter(measure1,measure2):
     for species in iris_species:

          x = data[data['species']==species][measure1]
          y = data[data['species']==species][measure2]

          mpl.scatter(x,y,color=colors[species],label=species,alpha=.5)

          mpl.xlabel(measure1)
          mpl.ylabel(measure2)
          mpl.title('Iris Dataset (' + measure1 + " vs  " + measure2 + ")")
          mpl.legend()
     mpl.savefig(measure1 + "_" + measure2 + ".png")
     mpl.show()
'''
fig, axs = plt.subplots(2, 3)
axs[0, 0].plot(x, y)
axs[0, 0].set_title('Axis [0, 0]')
axs[0, 1].plot(x, y, 'tab:orange')
axs[0, 1].set_title('Axis [0, 1]')
axs[1, 0].plot(x, -y, 'tab:green')
axs[1, 0].set_title('Axis [1, 0]')
axs[1, 1].plot(x, -y, 'tab:red')
axs[1, 1].set_title('Axis [1, 1]')
'''

#call function to plot scatterplots for possible unique combinations of two measures(4 measures pick two = 4*3/2*1 = 6)
for i in range (0,4):
     for j in range(i+1,4):
          plot_scatter(measures[i],measures[j])



             
#plot_hist()
#add scatterdiagrams for each pair ([sepal_length,width][petal length,width] for each class (6 diagrams in all)
plot_box()

#print(data['sepal_length'])
#setosa_sl = data.loc[0:49, ['sepal_length']]
#print(data.query('class =="Iris-setosa"'))  #returning error
#print(data[data['class']=="Iris-setosa"])
#print(data[data['class']=="Iris-setosa"][['sepal_length']])
#mpl.hist(setosa_sl)
#mpl.show()

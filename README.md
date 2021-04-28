# pands-project2021
Repository for the Programming and Scripting Module of the GMIT HDip in Data Analytics  Project 2021

Student: Mark Parry G00398271

Project is based on an analysis of the Iris Data Set. The documents include the code, text outputs and plots, a breakdown of the code,analysis of the data and the references used whilst researching the project. 


Contents:

|Document       |Description                                                                                                       |Date Added|
|---------------|------------------------------------------------------------------------------------------------------------------|----------|
|Project Plan|Outline of timeframe and steps needed to complete project|22/03/2021
|Code|analysis.py|23/03/3021
|The Project|The project itself - introduction, methods, findings, conclusion|23/04/2021

# The Project

## Table of contents
* [Introduction](#Introduction)	
	* [Project Brief](#Project-Brief)
 	* [Project Background](#Project-Background)
	* [Project Plan](#Project-Plan)
* [The Code](#The-Code)
	* [Initialisation](#Initialisation)
		* [Libraries](#Libraries)
		* [Import Data Set and Set Up](#Import-Data)
	* [Main Body](#Main-Body)
	* [Plots](#Plots)
		* [Plot Histogram](#PlotHist)
		* [Plot Scatter](#PlotScatter)
		* [Plot Box](#PlotBox)
	* [Outputs](#Outputs)
		* [Save Text Output to File](#Save-To-File)
		* [Save Plots to Portable Graphics Format(png)](#Save-To-Png)
* [Analysis Outputs](#Analysis-Outputs)
	* [Data Set Measurements Summary](#Measurements-Summary)
	* [Data Set Correlation](#Correlation)
	* [Histograms](#Histograms)
	* [Scatter Plots](#Scatter-Plots)
	* [Box Plots](#Box-Plots)
* [Conclusion](#Conclusion)
* [References](#References)
* [Bibliography](#Bibliography)
* [Glossary](#Glossary)
	* [Boxplot](#Boxplot)
	* [Histogram](#Histogram)
	* [Scatterplot](#Scatterplot) 



# **Introduction**

## **Project Brief**
"Research Fishers Iris data set and write documentation and code in Python to invetsigate it, write a summary of the research in the readme file and have the code output a summary of each measure to a textfile, output and save histograms of the data and produce scatter plots"(A.Beatty "PANDS Project Description")

For the purpose of this exercise I have used the python language to produce this report using the pandas and matplotlib modules to analyse the raw data and output statistics on the data such as the mean, median, standard deviation and produce tables and visualisations of the data. 


## **Project Background**

The Iris Data Set first appeared in the publication by R.A.Fisher of his paper "The Use Of Multiple Measurements In Taxonomic  Problems” in the journal “Annals of Eugenics” - many universities allow access to this paper purely for academic research and preface it with the following:

 “The work of eugenicists was often pervaded by prejudice against racial, ethnic and disabled groups. Publication of this material online is for scholarly research purposes is not an endorsement or promotion of the views expressed in any of these articles or eugenics in general”. (https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x n.d.)[01]
 
Fischer published his paper in the late 1930’s and as such would have had to presumably use a slide rule and pen and paper which would have meant that this would have been a long and laborious task, the advent of calculators would have speeded this up for him in the 70’s and the personal computer in the early 80’s even further. The advent of statistical analysis packagess such as R ,SPSS and SAS would have given him an even better turnaround time. Today there are many packages in existence that are based specifically around statistical analysis and can be imported or used by many modern computer languages such as python. Within the python world there are a number of importable utilities such as pandas which is used to generate and manipulate dataframes, matplotlib which is used for graphical representations of the data and various others such as  Seaborn and Gleam.

## **Project Plan**

Or the "best laid plans of mice and men"(Robert Burns)

<img src = "https://github.com/MarkJParry/pands-project2021/blob/main/projectplan.PNG" alt = "Project Plan">


# **The Code**
## **Initialisation**

### **Libraries**

    import matplotlib.pyplot as mpl
    import pandas as pd


### **Import Data**

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

## **Main Body**

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
	 
## **Plots**
	 
### **Plot Histogram**

	#function to plot and display histograms for the data set
	#this will loop through the measures and within that loop, loop through the species
	#plot the measure for each species on one graph and save that to a file
	def plot_hist():
	     #loop through the measurements excluding the species column
	     for measure in measures:
		  #loop through the dataframe for each species
		  for species in iris_species:
		       mpl_data = data[data['species']==species][measure]
		       mpl.hist(mpl_data,color=colors[species],label=species,alpha=.5,histtype="step")
		       #Give the histograms a title,label both axes, display the legend to note which plot is which(prb)                    
		       mpl.title("Iris Dataset " + measure + " Histogram") 
		       mpl.xlabel(measure) 
		       mpl.ylabel("count") 
		       mpl.legend() 
		       #this will save the plot to file
		       mpl.savefig(measure + ".png")
		  mpl.show()
		  
### **Plot Scatter**	

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

### **Plot Box**

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


## **Outputs**
### **Save To File**

    #save the output of the describe function of the dataframe to a text file 
    with open('describe.txt', 'w') as outfile:
       print('\nOutput from the data describe function', file=outfile)
       print(data.describe(),file=outfile)

    #save the output of the correlation function to a text file
    with open('correlation.txt', 'w') as outfile:
       print('\nOutput from the data correlation function', file=outfile)
       print(data.corr(),file=outfile)

### **Save To Png**   

    #save the plots to file
    mpl.savefig(measure + ".png")
    mpl.savefig(species + ".png")
    mpl.savefig(measure1 + "_" + measure2 + ".png")



# **Analysis Outputs**
## **Measurements Summary**

    Output from the data describe function
           sepal_length  sepal_width  petal_length  petal_width
    count    150.000000   150.000000    150.000000   150.000000
    mean       5.843333     3.054000      3.758667     1.198667
    std        0.828066     0.433594      1.764420     0.763161
    min        4.300000     2.000000      1.000000     0.100000
    25%        5.100000     2.800000      1.600000     0.300000
    50%        5.800000     3.000000      4.350000     1.300000
    75%        6.400000     3.300000      5.100000     1.800000
    max        7.900000     4.400000      6.900000     2.500000
    
## **Correlation**

    Output from the data correlation function
                  sepal_length  sepal_width  petal_length  petal_width
    sepal_length      1.000000    -0.109369      0.871754     0.817954
    sepal_width      -0.109369     1.000000     -0.420516    -0.356544
    petal_length      0.871754    -0.420516      1.000000     0.962757
    petal_width       0.817954    -0.356544      0.962757     1.000000

## **Histograms**

<img src="https://github.com/MarkJParry/pands-project2021/blob/main/petal length.png" alt="Petal Length histogram" width=450 height=300 align=left>
<img src="https://github.com/MarkJParry/pands-project2021/blob/main/petal width.png" alt="Petal Width histogram" width=450 height=300>
	
<img src = "https://github.com/MarkJParry/pands-project2021/blob/main/sepal length.png" alt = "Sepal Length histogram" width=450 height=300 align=left>
<img src = "https://github.com/MarkJParry/pands-project2021/blob/main/sepal width.png" alt = "Sepal Width histogram" width=450 height=300>


## **Scatter Plots**
<img src="https://github.com/MarkJParry/pands-project2021/blob/main/sepal_length_sepal_width.png" alt="Iris Dataset Scatter Plot 1" width=290 height=290 align=left>
<img src="https://github.com/MarkJParry/pands-project2021/blob/main/sepal_length_petal_length.png" alt="Iris Dataset Scatter Plot 2" width=290 height=290 align=left>
<img src="https://github.com/MarkJParry/pands-project2021/blob/main/sepal_length_petal_width.png" alt="Iris Dataset Scatter Plot 3" width=290 height=290>

<img src="https://github.com/MarkJParry/pands-project2021/blob/main/sepal_width_petal_length.png" alt="Iris Dataset Scatter Plot 4" width=290 height=290 align=left>
<img src="https://github.com/MarkJParry/pands-project2021/blob/main/sepal_width_petal_width.png" alt="Iris Dataset Scatter Plot 5" width=290 height=290 align=left>
<img src="https://github.com/MarkJParry/pands-project2021/blob/main/petal_length_petal_width.png" alt="Iris Dataset Scatter Plot 6" width=290 height=290>

## **Box Plots**
<img src="https://github.com/MarkJParry/pands-project2021/blob/main/Iris-setosa.png" alt="Iris Setosa boxplot" width=290 height=290 align=left>
<img src="https://github.com/MarkJParry/pands-project2021/blob/main/Iris-versicolor.png" alt="Iris Versicolor boxplot" width=290 height=290 align=left>
<img src="https://github.com/MarkJParry/pands-project2021/blob/main/Iris-virginica.png" alt="Iris Virginica boxplot" width=290 height=290>

# **Conclusion**

The purpose of analysing any set of  data is to see if one can gain insights into the data, firstly is there anything meaningful in the data, can anything be extrapolated from the data, as such this particular data set lends itself to the “machine learning” branch of computing as it is a small, compact data set and there appears to be some correlation between the petal length and petal width between the species enabling a model to categorise a plant given the pairs of data (sepal width and length, petal width and length) into its particular species with a relatively low degree of error.


# **References**
[01][The Use Of Multiple Measurements In Taxonomic Problems] https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x
[02][Statistics Glossary v1.1] http://www.stats.gla.ac.uk/steps/glossary/

# **Bibliography**
|Title|Link|
|-----|----|
|Iris flower data set|https://en.wikipedia.org/wiki/Iris_flower_data_set
|ScienceDirect - Iris Data|https://www.sciencedirect.com/topics/mathematics/iris-data
|towardsdatascience - scikit|https://towardsdatascience.com/exploring-classifiers-with-python-scikit-learn-iris-dataset-2bcb490d2e1b
|scipy-lectures - the Pandas Dataframe|https://scipy-lectures.org/packages/statistics/index.html#the-pandas-data-frame
|Matplotlib - Gallery|https://matplotlib.org/stable/gallery/index.html
|UCI Machine Learning Repository|https://archive.ics.uci.edu/ml/datasets/Iris
|Mastering Markdown Github|https://guides.github.com/features/mastering-markdown/#examples
|Data Manipulation with Python Pandas and R Data.Table|https://datascience-enthusiast.com/R/pandas_datatable.html  comparison of pandas and R
|Module 3: Data Exploration|http://www.cse.msu.edu/~ptan/dmbook/tutorials/tutorial3/tutorial3.html
|Pandas API Reference - Dataframe Constructor|https://pandas.pydata.org/docs/reference/frame.html 
|GitHub Docs - Writing on GitHub|https://docs.github.com/en/github/writing-on-github
|MatPlotLib - Creating multiple subplots using plt.subplots|https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
|Python Tutorials - MatPlotLib Scatterplot|https://pythonspot.com/matplotlib-scatterplot/
|The Use Of Multiple Measurements In Taxonomic Problems|https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x
|Boxplots - Matplotlib 3.4.1. documentation|https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html#sphx-glr-gallery-statistics-boxplot-demo-py
|Histograms - Matplotlib 3.4.1. documentation|https://matplotlib.org/stable/gallery/statistics/hist.html
|Scatter Plots - Matplotlib 3.4.1 documentation|https://matplotlib.org/stable/gallery/shapes_and_collections/scatter.html
|Statistics Glossary v1.1|http://www.stats.gla.ac.uk/steps/glossary/
|Python Print Function|https://www.tutorialgateway.org/python-print-function/

# **Glossary**  
The following definitions are taken from Easton, V. J. and McColl, J. H.  (1997) Statistics Glossary v1.1 
## **Boxplot**
A box and whisker plot is a way of summarising a set of data measured on an interval scale. It is often used in exploratory data analysis. It is a type of graph which is used to show the shape of the distribution, its central value, and variability. The picture produced consists of the most extreme values in the data set (maximum and minimum values), the lower and upper quartiles, and the median.

A box plot (as it is often called) is especially helpful for indicating whether a distribution is skewed and whether there are any unusual observations (outliers) in the data set.

Box and whisker plots are also very useful when large numbers of observations are involved and when two or more data sets are being compared.

## **Histogram**
A histogram is a way of summarising data that are measured on an interval scale (either discrete or continuous). It is often used in exploratory data analysis to illustrate the major features of the distribution of the data in a convenient form. It divides up the range of possible values in a data set into classes or groups. For each group, a rectangle is constructed with a base length equal to the range of values in that specific group, and an area proportional to the number of observations falling into that group. This means that the rectangles might be drawn of non-uniform height.

The histogram is only appropriate for variables whose values are numerical and measured on an interval scale. It is generally used when dealing with large data sets (>100 observations), when stem and leaf plots become tedious to construct. A histogram can also help detect any unusual observations (outliers), or any gaps in the data set.

## **Scatterplot**
A scatterplot is a useful summary of a set of bivariate data (two variables), usually drawn before working out a linear correlation coefficient or fitting a regression line. It gives a good visual picture of the relationship between the two variables, and aids the interpretation of the correlation coefficient or regression model.

Each unit contributes one point to the scatterplot, on which points are plotted but not joined. The resulting pattern indicates the type and strength of the relationship between the two variables.

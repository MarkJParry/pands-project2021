# pands-project2021
Repository for the Programming and Scripting Module of the GMIT HDip in Data Analytics  Project 2021

Student: Mark Parry G00398271

Project is based on an analysis of the Iris Data Set. The various documents to be added include the code, txt outputs and graphs, and the analysis of the data. References used when researching and any others(##look at project brief to update properly). 


Contents:

|Document       |Description                                                                                                       |Date Added|
|---------------|------------------------------------------------------------------------------------------------------------------|----------|
|Project Plan|Outline of timeframe and steps needed to complete project|22/03/2021
|Code|analysis.py|23/03/3021
|The Project|The project itself - introduction,methods,findings,conclusion|23/04/2021

# The Project

## Table of contents
* [Introduction](#Introduction)	
	* [Project Brief](#Project-Brief)
 	* [Project Background](#Project-Background)
	* [Project Plan](#Project-Plan)
* [The Code](#The-Code)
	* [Libraries](#Libraries)
	* [Data Import](#Data-Import)
	* [Main](#Main)
	* [Outputs](#Outputs)
		* [Save Text Output to File](#Save-To-File)
		* [Save Plots to Portable Graphics Format(png)](#Save-To-Png)
* [Analysis Outputs](#Analysis-Outputs)
	* [Data Set Summary](#Summary)
	* [Histograms](#Histograms)
	* [Scatter Plots](#Scatter-Plots)
	* [Box Plots](#Box-Plots)
* [Conclusion](#Conclusion)
* [References](#References)
* [Bibliography](#Bibliography)



# **Introduction**

## **Project Brief**
"Research Fishers Iris data set and write documentation and code in Python to invetsigate it, write a summary of the research in the readme file and have the code output a summary of ech measure to a textfile, output and save histograms of the data and produce scatter plots"(A.Beatty "PANDS Project Description")

For the purpose of this exercise I have used the python language to produce this report using the pandas and matplotlib modules to analyse the raw data and output statistics on the data such as the mean, median, standard deviation and produce tables and visualisations of the data. 

The purpose of analysing any set of  data is to see if one can gain insights into the data, firstly is there anything meaningful in the data, can anything be extrapolated from the data, as such this particular data set lends itself to the “machine learning” branch of computing as it is a small, compact data set and there appears to be some correlation between the petal length and petal width between the species enabling a model to categorise a plant given the pairs of data (sepal width and length, petal width and length) into its particular species with a relatively low degree of error.

## **Project Background**

The Iris Data Set first appeared in the publication by R.A.Fisher of his paper "THE USE OF MULTIPLE MEASUREMENTS IN TAXONOMIC  PROBLEMS” in the journal “Annals of Eugenics” - many universities allow access to this paper purely for academic research and preface it with the following:

 “The work of eugenicists was often pervaded by prejudice against racial, ethnic and disabled groups. Publication of this material online is for scholarly research purposes is not an endorsement or promotion of the views expressed in any of these articles or eugenics in general”. (https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x n.d.)
 
Fischer published his paper in the late 1930’s and as such would have had to presumably use a slide rule and pen and paper which would have meant that this would have been a long and laborious task, the advent of calculators would have speeded this up for him in the 70’s and the personal computer in the early 80’s even further. The advent of statistical analysis packagess such as R ,SPSS and SAS would have given him an even better turnaround time . Today there are many packages in existence that are based specifically around statistical analysis and can be imported or used by many modern computer languages such as python, java, etc. Within the python world there are a number of importable utilities such as pandas which is used to generate and manipulate dataframes, matplotlib which is used for graphical representations of the data and various others such as  Seaborn and Gleam.

## **Project Plan**

Or the "best laid plans of mice and men"(Robert Burns)

<img src = "https://github.com/MarkJParry/pands-project2021/blob/main/projectplan.PNG" alt = "Project Plan">


# **The Code**
## **Libraries**


    import matplotlib.pyplot as mpl
    import numpy as np
    import pandas as pd

## **Data Import**


    #read in the csv file of values
    data = pd.read_csv('iris.data',header=None)

    #give the values a header column as there was no header in the csv file
    data.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

'''
## **Main**
## **Outputs**
### **Save To File**

    #save the output of the describe function of the dataframe to a text file 
    with open('describe.txt', 'a') as outfile:
       print('\nOutput from the data describe function', file=outfile)
       print(data.describe(),file=outfile)

    #save the output of the correlation function to a text file
    with open('correlation.txt', 'a') as outfile:
       print('\nOutput from the data correlation function', file=outfile)
       print(data.corr(),file=outfile)

### **Save To Png**   

    #save the plots to file
    mpl.savefig(measure + ".png")
    mpl.savefig(species + ".png")
    mpl.savefig(measure1 + "_" + measure2 + ".png")



# **Analysis Outputs**
## **Summary**

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
# **References**
[01][THE USE OF MULTIPLE MEASUREMENTS IN TAXONOMIC  PROBLEMS] https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x

# **Bibliography**
|Title|Link
|Towards data science. The Iris dataset - A little bit of history and biology|https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5

|Iris flower data set|https://en.wikipedia.org/wiki/Iris_flower_data_set

|addtitle|https://www.sciencedirect.com/topics/mathematics/iris-data

|addtitle| https://towardsdatascience.com/exploring-classifiers-with-python-scikit-learn-iris-dataset-2bcb490d2e1b

|addtitle| https://scipy-lectures.org/packages/statistics/index.html#the-pandas-data-frame

|dataset available here:| https://gist.github.com/curran/a08a1080b88344b0c8a7#file-readme-md

|addtitle| https://matplotlib.org/stable/gallery/index.html

|NumPy| https://numpy.org

|addtitle| https://archive.ics.uci.edu/ml/datasets/Iris



|Mastering Markdown Github| https://guides.github.com/features/mastering-markdown/#examples


|addtitle|https://datascience-enthusiast.com/R/pandas_datatable.html  comparison of pandas and R
|addtitle|http://www.cse.msu.edu/~ptan/dmbook/tutorials/tutorial3/tutorial3.html
|addtitle|https://pandas.pydata.org/docs/reference/frame.html 
|addtitle|https://docs.github.com/en/github/writing-on-github
|addtitle|https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
|addtitle|https://pythonspot.com/matplotlib-scatterplot/
--->


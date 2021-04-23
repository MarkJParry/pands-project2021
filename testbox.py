import numpy as np
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt
# Load Iris dataset
iris = datasets.load_iris()
print(iris)
input("pause")
# Preparing Iris dataset
iris_data = pd.DataFrame(data=iris.data, columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
print(iris_data)
input("pause")
iris_target = pd.DataFrame(data=iris.target, columns=['species'])
print(iris_target)
input("pause")
iris_df = pd.concat([iris_data, iris_target], axis=1)
input("pause")
print(iris_df)
# Add species name
input("pause")
iris_df['species_name'] = np.where(iris_df['species'] == 0, 'Setosa', None)
iris_df['species_name'] = np.where(iris_df['species'] == 1, 'Versicolor', iris_df['species_name'])
iris_df['species_name'] = np.where(iris_df['species'] == 2, 'Virginica', iris_df['species_name'])
print(iris_df)
input("pause")
# Prepare petal length by species datasets
setosa_petal_length = iris_df[iris_df['species_name'] == 'Setosa']['petal_length']
print(setosa_petal_length)
input("pause")
versicolor_petal_length = iris_df[iris_df['species_name'] == 'Versicolor']['petal_length']
virginica_petal_length = iris_df[iris_df['species_name'] == 'Virginica']['petal_length']

# Visualize petal length distribution for all species
fig, ax = plt.subplots(figsize=(12, 7))
input(ax)
# Remove top and right border
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
# Remove y-axis tick marks
ax.yaxis.set_ticks_position('none')
# Add major gridlines in the y-axis
ax.grid(color='grey', axis='y', linestyle='-', linewidth=0.25, alpha=0.5)
# Set plot title
ax.set_title('Distribution of petal length by species')
# Set species names as labels for the boxplot
dataset = [setosa_petal_length, versicolor_petal_length, virginica_petal_length]
print(setosa_petal_length)
#print(dataset)
labels = iris_df['species_name'].unique()
ax.boxplot(dataset, labels=labels)
plt.show()
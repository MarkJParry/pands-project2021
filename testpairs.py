columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
measures = columns[:-1]




for i in range (0,4):
     for j in range(i+1,4):
          print(measures[i],measures[j])

n_features = 4
pairs = [(i, j) for i in range(n_features) for j in range(i+1, n_features)]

for (f1, f2) in pairs:
    print(f1, f2)
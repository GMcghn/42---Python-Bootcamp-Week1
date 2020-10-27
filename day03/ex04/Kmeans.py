
# In our case the data we have to process is composed of 3 values (height, weight and bone_density). Thus, each
# data point is a vector of 3 values.

# hyperparameter tuning:
# The L1 norm that is calculated as the sum of the absolute values of the vector.
# The L2 norm that is calculated as the square root of the sum of the squared vector values.
# Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space that measures the cosine of the angle between them.


# code derrière fit et predict de KMEANS : https://github.com/scikit-learn/scikit-learn/blob/483cd3eaa/sklearn/cluster/_kmeans.py#L933
# animation : https://i.ibb.co/bKFVVx2/ezgif-com-gif-maker.gif

# centers display de la meme couleur. eng ros si on fait dans le mme ordre il prend la meme couleur.
#   https://stackoverflow.com/questions/28256882/plotting-the-center-of-a-k-means-cluster-to-be-the-same-color-as-its-cluster-poi


# d'après les indices la solution ou les espaces entre centers est + marquée : Venus vert terre mauve mars bleu belt jaune
# j'ai pas trop suivi l'énoncé j'ai pas bien compris si je devais reconstruire tout le code derrière alogo Kmean ça me semblait 
# très laborieux du coup j'ai juste appliqué le modèle comme d'hab

# bon lien : https://jakevdp.github.io/PythonDataScienceHandbook/05.11-k-means.html


# en fait en suivant le très bon lien ci-dessous, y aurait quand meme eu moyen je pense: (à voir pour plus tard pê)
    # théorie : https://bigdata-madesimple.com/possibly-the-simplest-way-to-explain-k-means-algorithm/

import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

url = 'https://raw.githubusercontent.com/42-AI/bootcamp_python/master/day03/resources/solar_system_census.csv'

# pd.set_option('display.max_rows', None) # display toutes les lignes dans jupyerNB
df = pd.read_csv(url, index_col=0)
# X = df.to_numpy() #ndarray

model = KMeans(n_clusters=4)
model.fit(df)
labels = model.predict(df)
df["label"]=labels

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = df['height']
Y = df['weight']
Z = df['bone_density']
C = df['label']
D = list(set(df['label']))
centers = model.cluster_centers_
print(centers)

ax.scatter(X, Y, Z, marker ='o', c = C)
ax.scatter(centers[:, 0], centers[:, 1], centers[:, 2],  c=D, s=200, alpha=0.5, marker ='x')

ax.set_xlabel('height')
ax.set_ylabel('weight')
ax.set_zlabel('bone_density')

plt.show()
# points les + foncés les + près

class KmeansClustering:

    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
        None.
        Raises:
        This function should not raise any Exception.
        """
        pass        


    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
        the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        This function should not raise any Exception.
        """
        pass
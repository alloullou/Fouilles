from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import pandas as pd
import numpy as np

def clustering_model_score(clustering_value, n_cluster):

    df = pd.read_csv('CSV\Prix_Arrondissement.csv', encoding='utf-8-sig')

    newdf=df['Arrondissement','Hopitaux','metro','bus','rer',
                          'stationautolib','stationvelib','etablissement',
                          'Prixmetrecarree'].values

    clf = KMeans(n_cluster, n_jobs=1)
    return clf.fit_predict(clustering_value)


def clustering_dataset_score(dataset, score):
    """Return the dataset assigned with the cluster score

    Args:
        dataset   dataframe object containing datas used for the cluster
        score     cluster score

    Returns:
        object: pandas dataframe of the dataset assigned with the cluster score
    """

    return dataset.assign(**{'cluster_id': score})


def try_kmeans(X):
    best_k = 1
    best_score = -1

    for k in range(2, 30+1):
        model = KMeans(n_clusters=k)
        model.fit(X)
        labels = model.predict(X)
        score = silhouette_score(model.transform(X), labels)

        if score > best_score:
            best_k = k
            best_score = score

    print("the best k is", best_k)
    return best_k



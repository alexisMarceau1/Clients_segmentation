import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import preprocessing, manifold, decomposition
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import MinMaxScaler

#------------------------------------------
def algo_score(algorithm, data):
    
    df_algo = pd.DataFrame(columns=["algorithme", "silhouette", "nb_clusters", "time_sec"])

    for algoname, algo in algorithm.items():
        start_time = time.time()
        cluster_labels = algo.fit_predict(data)
        elapsed_time = str(round(time.time() - start_time,2))

        df_algo.loc[len(df_algo)] = [algoname, silhouette_score(data,
                                                                cluster_labels,
                                                                metric="euclidean"),
                                                                len(set(cluster_labels)),
                                                                elapsed_time]
    
    return df_algo  
#------------------------------------------
def plotTSNE(X_scaled, kmeans_labels):
    
    TITLE_SIZE = 40
    TITLE_PAD = 1.05
    LABEL_SIZE = 30
    LABEL_PAD = 20
    
    tsne = manifold.TSNE(n_components=2, verbose=1, perplexity=40, n_iter=300)
    tsne_results = tsne.fit_transform(X_scaled)

    data_to_plot = pd.DataFrame()
    
    data_to_plot["tsne-2d-one"] = tsne_results[:,0]
    data_to_plot["tsne-2d-two"] = tsne_results[:,1]
    data_to_plot["kmeans_label"] = kmeans_labels
    
    fig = plt.figure(figsize=(10, 10))
    
    plt.title("Mise en évidence des clusters t-SNE", fontsize=TITLE_SIZE)

    ax = sns.scatterplot(x="tsne-2d-one", y="tsne-2d-two",
                                    data=data_to_plot,
                                    hue="kmeans_label",
                                    palette=sns\
                                      .color_palette("hls",
                                                           data_to_plot["kmeans_label"].nunique()),
                                    legend="full")

    ax.set_xlabel("t-SNE 1",
                             fontsize=LABEL_SIZE,
                             labelpad=LABEL_PAD,
                             fontweight="bold")

    ax.set_ylabel("t-SNE 2",
                             fontsize=LABEL_SIZE,
                             labelpad=LABEL_PAD,
                             fontweight="bold")
#------------------------------------------
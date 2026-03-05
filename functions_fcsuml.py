# Import packages
import numpy as np
import pandas as pd
import hdbscan
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model, metrics
from sklearn.linear_model import LinearRegression


def remove_non_numbers(data):
    """Remove colums with data which are not numbers and return the matrix, without the columns, and the indexes of the removed rows."""
    del_data = data.copy()
    del_idx = {}

    # Removing all non int or float type features looping from the end.
    iterate = len(del_data[0,:])-1
    for i in range(iterate+1):
        if type(del_data[0,iterate-i]) != float and type(del_data[0,iterate-i]) != int:
            del_data = np.delete(del_data, obj=iterate-i, axis=1)
            del_idx[iterate-i] = iterate-i

    return del_data, del_idx


def normalize_feature(feature):
    """Min-max normalization. This retains the relative position of the data points."""
    return (feature-np.min(feature)) / (np.max(feature)-np.min(feature)), np.max(feature), np.min(feature)


def normalize(data, axis=1):
    """Using the normalize_feature function on an np.array along a chosen axis."""
    norm_data = np.zeros_like(data)
    normalization_variables = np.zeros((2, np.shape(data)[1])) # row 1: max value, row 2: min value

    for i in range(data.shape[axis]):
        norm_data[:,i], normalization_variables[0, i], normalization_variables[1, i] = normalize_feature(data[:,i])
    return norm_data, normalization_variables


def clustering(data, cluster_size=10, min_samples=10, distance_type='euclidean'):
    """Takes data, minimum cluster size, distance metric and returns an array of the data with an added column at index 0 with the cluster label and the number of clusters."""
    clusterer = hdbscan.HDBSCAN(min_cluster_size=cluster_size, min_samples=min_samples ,  metric=distance_type)    # , approx_min_span_tree=True, algorithm='boruvka_balltree'
    print('shape:', data.shape)
    clusterer.fit(data)
    return clusterer.labels_.max()+1 , np.insert(data, 0, clusterer.labels_.flatten(), axis=1)





def reduce_dimension(vector,clusters):
    """Takes a vector and a set of clusters and reduces the vectors dimension to the number of clusters using the clusters as a basis."""
    # Vector projection
    transformation_matrix = np.zeros([len(clusters), len(vector)])

    for i in clusters:
        transformation_matrix[i] = center_of_mass(clusters[i])

    reduced_vector = transformation_matrix * vector
    return reduced_vector


def get_cmap(n, name='hsv'):
    '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
    RGB color; the keyword argument name must be a standard mpl colormap name.'''
    return plt.cm.get_cmap(name, n)


def compare_Euclidean(reference, comparables, k=3):
    """Takes a reference point and a matrix of comparable points and returns the first column of the comparable points (ID) and
    the Euclidean distances sorted by distance from low to high."""

    sq_compare = np.square(comparables[:,1:] - reference[1:])
    sum_compare = np.sum(sq_compare, axis=1)
    Euc_compare = np.sqrt(sum_compare)
    Euc_compare = np.vstack((comparables[:, 0], Euc_compare)).T

    sorted_dis = Euc_compare[Euc_compare[:, 1].argsort()]   # Sort Euc_compare

    return sorted_dis[0:k, :]

def show_clusters_in_latlon(data, sorted_clusters, number_of_clusters, clusterspan, lat_index=2, lon_index=3):
    """Creates a 3D plot of the clusters and their center of mass."""

    fig = plt.figure(figsize = (10,10))
    ax = plt.axes()
    ax.grid()

    cmap = get_cmap((number_of_clusters+1)*2)

    for i in range(1,number_of_clusters+1):
        x1 = sorted_clusters[int(clusterspan[i]):int(clusterspan[i+1]), lat_index]
        y1 = sorted_clusters[int(clusterspan[i]):int(clusterspan[i+1]), lon_index]
        ax.scatter(x1, y1, c = cmap(i), s = 1)

    ax.set_title('Scatter Plot')

    # Set axes label
    ax.set_xlabel('x', labelpad=20)
    ax.set_ylabel('y', labelpad=20)


def dataframe_to_numpy(dataframe):
    dataframe = dataframe.fillna(0)
    data = dataframe.to_numpy()


    data, removed_indices = remove_non_numbers(data)
    print("Removed indices:", removed_indices)



    data = data.astype(float) # Changing from type object to float so that numpy functions work properly.
    return data

def create_clusterspan(sorted_clusters, number_of_clusters):
    clusterspan = np.zeros(number_of_clusters+2)

    for i in range(0, number_of_clusters+1):
        clusterspan[i+1] = clusterspan[i] + np.shape(sorted_clusters[np.where(sorted_clusters[:,0] == i)])[0]

    clusterspan[-1] = np.shape(sorted_clusters)[0]
    return clusterspan


def silhouette(SC, NC):
    labels = SC[:, 0]
    silhouettes = metrics.silhouette_samples(SC[:, 1:], labels)
    cluster_silhouettes = np.zeros((NC, 2))
    
    for i in range(1, NC+1):
        # print(i, NC)
        cluster_silhouettes[i-1,:] = i, np.mean(silhouettes[np.where(SC[:, 0] == i)])

    return np.mean(silhouettes), cluster_silhouettes
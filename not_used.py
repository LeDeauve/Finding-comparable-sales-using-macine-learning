import numpy as np

def z_score_norm(feature):
    """Standardization (Z-score Normalization)"""
    return (feature - np.average(feature)) / np.sqrt(np.var(feature))


def softmax(feature):
    """Softmax normalization of the data."""
    softnormalize = feature / np.average(feature, axis=0) # If the values of a feature get too large the softmax function can't handle it properly
    return np.exp(softnormalize) / np.sum(np.exp(softnormalize), axis=0)

def euclidian_distance(vector_1,vector_2):
    try:
        distance = vector_1-vector_2
        return np.sqrt(np.dot(distance,distance))
    except TypeError("Vectors not same length.") as e:
        print(e)


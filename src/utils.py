import math

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def generate_matrix(dim, var):
    """
    Take in a dimension dim, and a variance var.
    Generate a dim x dim random symmetric matrix A according to the procedure
    outlined in the project handout (using variance Var for the normally
    distributed random variables).
    """
    m = np.random.normal(0, math.sqrt(var), (dim, dim))
    a = (m + np.transpose(m)) / 2
    return a

def plot_kde(data):
    sns.kdeplot(data)
    plt.show()

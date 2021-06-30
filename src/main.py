import numpy as np

import utils

np.random.seed(123)

# Dimension for the square random symmetric matrix
_DIMENSION = 3

# Variance for the normal random var
_VARIANCE = 1

# Number of matrices to generate and analyze
_NUM_MATRICES = 10000


def main():
    all_eigenvalues = np.empty((0,))
    for _ in range(_NUM_MATRICES):
        m = utils.generate_matrix(_DIMENSION, _VARIANCE)
        eigenvalues, eigenvectors = np.linalg.eig(m)
        all_eigenvalues = np.concatenate((all_eigenvalues, eigenvalues))
    utils.plot_kde(eigenvalues)

if __name__ == '__main__':
    main()

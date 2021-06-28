import math
import numpy as np

np.random.seed(123)

# Dimension for the square random symmetric matrix
_DIMENSION = 3

# Variance for the normal random var
_VARIANCE = 1

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


def main():
    m = generate_matrix(_DIMENSION, _VARIANCE)
    eigenvalues, eigenvectors = np.linalg.eig(m)
    print(eigenvalues)

if __name__ == '__main__':
    main()

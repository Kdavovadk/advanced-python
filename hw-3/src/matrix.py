import numpy as np


class Matrix:
    """Matrix representation"""

    def __init__(self, data: list[list[int]]) -> None:
        """Inits class entity
        
        Args:
            data: matrix filling
        """
        self.data = np.array(data)
        self.shape = (len(data), len(data[0]))

    def __add__(self, other):
        """Sums current matrix with other
        
        Args:
            other: other matrix
        Returns:
            sum of two matrices
        Raises:
            ValueError: if matrices shapes not match
        """
        if self.shape != other.shape:
            raise ValueError("Matrices shapes must match")
        
        sum_data = [[
            self.data[i][j] + other.data[i][j] for j in range(self.shape[1])
        ] for i in range(self.shape[0])]

        return Matrix(sum_data)

    def __mul__(self, other):
        """Muls (elemenwise) current matrix with other
        
        Args:
            other: other matrix
        Returns:
            mul (elementwise) of two matrices
        Raises:
            ValueError: if matrices shapes not match
        """
        if self.shape != other.shape:
            raise ValueError("Matrices shape must match")
        
        mul_data = [[
            self.data[i][j] * other.data[i][j] for j in range(self.shape[1])
        ] for i in range(self.shape[0])]

        return Matrix(mul_data)

    def __matmul__(self, other):
        """Muls (matrix) current matrix with other
        
        Args:
            other: other matrix
        Returns:
            mul (matrix) of two matrices
        Raises:
            ValueError: if this matrix cols count not equals to other lines count
        """
        if self.shape[1] != other.shape[0]:
            raise ValueError("This matrix cols count must equals to other lines count")
        
        matmul_data = [[0 for _ in range(other.shape[1])] for _ in range(self.shape[0])]
        for i in range(self.shape[0]):
            for j in range(other.shape[1]):
                for k in range(self.shape[1]):
                    matmul_data[i][j] += self.data[i][k] * other.data[k][j]
            
        return Matrix(matmul_data)

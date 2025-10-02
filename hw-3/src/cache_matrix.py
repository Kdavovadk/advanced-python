import numpy as np

from .mixin_matrix import MixinMatrix


class HashMixin:
    def __hash__(self) -> int:
        """Hash function

        Algorithm:
        1) mul all values in each row
        2) sum all received numbers
        3) xor to diagon values
        """
        hash_value = 0
        for line in self.data:
            line_value = 1
            for item in line:
                line_value *= item
            hash_value += line_value
        
        min_shape = min(self.shape)
        xor = 0
        for i in range(min_shape):
            xor ^= self.data[i][i]
        
        return hash_value


class CacheMatrix(HashMixin, MixinMatrix):
    """Matrix with matmul caching"""

    _cache = {}

    def __matmul__(self, other):
        """Muls (matrix) current matrix with other with cache check
        
        Args:
            other: other matrix
        Returns:
            mul (matrix) of two matrices
        """
        cache_key = (hash(self), hash(other))
        if cache_key in self._cache:
            #pass
            return self._cache[cache_key]
        
        matmul_matrix = super().__matmul__(other)
        self._cache[cache_key] = matmul_matrix

        return matmul_matrix

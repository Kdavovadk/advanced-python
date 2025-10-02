import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin


class FileMixin:
    """Files interaction"""
    
    def write_file(self, name: str):
        """Writes data to file with given filename"""
        with open(f'artifacts/{name}', 'w') as f:
            f.writelines(self.__str__())


class StringMixin:
    """String convertion"""
    
    def __str__(self):
        """Converts data to string"""
        str_data = ''
        for line in self._data:
            str_data += f'{line}\n'
        
        return str_data


class FieldMixin:
    """Fields manipulation"""

    @property
    def data(self) -> list[list[int]]:
        """Gets data field value"""
        return self._data.tolist() if isinstance(self._data, np.ndarray) else self._data

    @data.setter
    def data(self, value: list[list[int]]):
        """Sets data field value"""
        self._data = value


class MixinMatrix(NDArrayOperatorsMixin, FieldMixin, StringMixin, FileMixin):
    """Matrix implemented by mixins"""

    def __init__(self, data: list[list[int]]):
        """Inits class entity
        
        Args:
            data: matrix filling
        """
        self._data = data
        self.shape = (len(data), len(data[0]))
    
    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        """Calls base magic methods"""
        inputs = tuple(x.data for x in inputs)
        result = getattr(ufunc, method)(*inputs, **kwargs)
        
        return type(self)(result)

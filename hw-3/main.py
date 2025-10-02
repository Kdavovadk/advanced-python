import numpy as np

from src import CacheMatrix, Matrix, MixinMatrix


def write_file(name: str, data: list[list[int]]) -> None:
    """Writes data to file
    
    Args:
        name: name of file
        data: data
    """
    with open(f'artifacts/{name}', 'w') as f:
        for line in data:
            f.write(str(line))
            f.write('\n')


def main():
    print('Task 3.1 started')
    np.random.seed(0)
    A1 = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
    B1 = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
    print(A1.data)
    print()
    print(B1.data)

    write_file('matrix1+.txt', (A1 + B1).data)
    write_file('matrix1*.txt', (A1 * B1).data)
    write_file('matrix1@.txt', (A1 @ B1).data)
    print('Task 3.1 finished')
    
    print('Task 3.2 started')
    np.random.seed(0)
    A2 = MixinMatrix(np.random.randint(0, 10, (10, 10)))
    B2 = MixinMatrix(np.random.randint(0, 10, (10, 10)))
    print(A2)
    print(B2)

    (A2 + B2).write_file('matrix2+.txt')
    (A2 * B2).write_file('matrix2*.txt')
    (A2 @ B2).write_file('matrix2@.txt')
    print('Task 3.2 finished')

    print('Task 3.3 started')
    A3 = CacheMatrix([
        [2, 3],
        [3, 2]
    ])
    B3 = CacheMatrix([
        [1, 0],
        [0, 1]
    ])
    C3 = CacheMatrix([
        [4, 1],
        [2, 4]
    ])
    D3 = CacheMatrix([
        [1, 0],
        [0, 1]
    ])

    print(hash(A3), hash(C3))
    print((hash(A3) == hash(C3)) and (A3.data != C3.data) and (B3.data == D3.data) and ((A3 @ B3).data != (C3 @ D3).data))

    A3.write_file('A.txt')
    B3.write_file('B.txt')
    C3.write_file('C.txt')
    D3.write_file('D.txt')
    (A3 @ B3).write_file('AB.txt')
    (C3 @ D3).write_file('CD.txt')
    with open('artifacts/hash.txt', 'w') as f:
        f.write(f'hash(AB)={hash(A3 @ B3)}, hash(CD)={hash(C3 @ D3)}')
    print('Task 3.3 finished')


if __name__ == '__main__':
    main()

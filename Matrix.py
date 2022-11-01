class Matrix:
    def __init__(self, renglones, columnas, nombre):
        self.renglones = renglones
        self.columnas = columnas
        self.nombre = nombre
        self.inner = []

    def __str__(self):
        return f'Matriz {self.nombre} {self.renglones}x{self.columnas}';

    def productoViable(self, b):
        return self.columnas == b.renglones

    # renglon por columna
    def fill(self):
        rel_start = 0
        print(f'Ingresa los valores de la matriz {self.nombre}')
        for ren in range(0, self.renglones):
            ren_list = []
            for col in range(0, self.columnas):
                entrada = int(input(f'{ren + 1}_{col + 1}: '))
                ren_list.append(entrada)
            self.inner.append(ren_list)
        pass

    def print(self):
        print(f"Matriz {self.nombre} =>")
        for ren in range(0, self.renglones):
            print('|', end=' ')
            for col in range(0, self.columnas):
                print(f'{ren + 1}_{col + 1}: {self.inner[ren][col]}', end=" ")
            print("|\n")
        pass

    # combinacion lineal
    def __mul__(self, other):
        m = self.renglones
        n = other.columnas
        return Matrix(m, n, "c")

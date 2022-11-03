class Matrix:
    def __init__(self, renglones, columnas, nombre, data=None):
        self.renglones = renglones
        self.columnas = columnas
        self.nombre = nombre
        self.inner = []
        if data is not None:
            self.inner = data
        else:
            # autollenamos nuestra matriz, como una matrix cero, para tener los indeces o memoria ya reservada
            for ren in range(0, self.renglones):
                ren_list = []
                for col in range(0, self.columnas):
                    ren_list.append(0)
                self.inner.append(ren_list)
            pass
        pass


    def __str__(self):
        return f'Matriz {self.nombre} {self.renglones}x{self.columnas}';

    def productoViable(self, b):
        return self.columnas == b.renglones

    # renglon por columna
    def fill(self):
        print(f'Ingresa los valores de la matriz {self.nombre}')
        for ren in range(0, self.renglones):
            for col in range(0, self.columnas):
                self[ren][col] = int(input(f'{ren + 1}_{col + 1}: '))
        pass

    def toString(self):
        str = ''
        print(f"{self} =>")
        for ren in range(0, self.renglones):
            str = str + '|'
            # print('|', end=' ')
            for col in range(0, self.columnas):
                str = str + f'{ren + 1}_{col + 1}: {self[ren][col]}'
                # print(f'{ren + 1}_{col + 1}: {self[ren][col]}', end=" ")
            #print("|\n")
            str = str + '|\n'
        pass
        return str

    def toLatex(self):
        str = '\\begin{bmatrix}\n'
        for ren in range(0, self.renglones):
            for col in range(0, self.columnas):
                str = str + f'{self.nombre}_{{{ren + 1}{col + 1}}} =  {self[ren][col]} & '
            str = str + '\\\\'
        pass
        str = str + '\n\\end{bmatrix}'
        return str

    def __getitem__(self, index):
        return self.inner[index]

    # combinacion lineal
    def __mul__(self, other):
        if self.columnas != other.renglones:
            return None
        m = self.renglones
        n = other.columnas
        c = Matrix(m, n, "C")
        # recorremos para llenas c
        # nota, la contante es el renglon de la resultante
        for ren in range(0, c.renglones):
            for col in range(c.columnas):
                # usando notacion sigma, obtenemos las componentes de c
                c[ren][col] = 0
                # recorremos a y b
                # recorremos renglones de a (self)
                for i in range(0, self.columnas):
                    c[ren][col] = c[ren][col] + self[ren][i] * other[i][ren]
            pass
        return c

    def __add__(self, other):
        if self.renglones != other.renglones or self.columnas != other.columnas:
            return None
        pass

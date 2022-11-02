from Matrix import Matrix


def pedirMatrix(name):
    print("Ingresa la dimesion de la matriz " + name)
    m = int(input("No renglones de " + name + ': '))
    n = int(input("No columnas de " + name + ': '))
    return Matrix(m, n, name)


a = pedirMatrix('A')
b = pedirMatrix('B')

if not a.productoViable(b):
    print("\n --- PRODUCTO NO COMPATIBLE ---\n")
    print(f'la matriz {a.nombre} no tiene producto viable con {b.nombre}')
    print(f'Recuerda que el numero de renglones de {a.nombre} debe ser igual al numero de columnas de {b.nombre}')
    print(a)
    print(b)
    exit(1)

# si son compatibles llenamos matrices


a.fill()
a.print()
b.fill()
b.print()

c = a * b

c.print()
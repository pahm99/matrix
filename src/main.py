from Matrix import Matrix
import json
import js


def calcular():
    matrixjson = Element('matrix-json').element.innerHTML
    matrices = json.loads(matrixjson)
    a = matrices['a']
    b = matrices['b']

    mA = Matrix(a['ren'], a['col'], 'A', a['matrix'])
    mB = Matrix(b['ren'], b['col'], 'B', b['matrix'])
    mC = mA * mB

    if mC is None:
        print('Producto no viable')
        exit(1)

    Element('ma').element.innerHTML = mA.toLatex()
    Element('mb').element.innerHTML = mB.toLatex()
    Element('mc').element.innerHTML = mC.toLatex()

    js.renderMatriz()

    pass

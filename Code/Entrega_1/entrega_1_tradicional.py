from simpleai.search import breadth_first, SearchProblem, astar, greedy
from simpleai.search.viewers import WebViewer

#Code#

INICIAL = (
    (2, 0, 5),
    (3, 7, 8),
    (4, 1, 6),
)

META = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
)

def donde_esta(state, numero):
    for indice_fila, fila in enumerate(state):
        for indice_columna, numero_actual in enumerate(fila):
            if numero_actual == numero:
                return indice_fila, indice_columna

# TupleToList
def t2l(t):
    return list(list(r) for r in t)

#ListToTuple
def l2t(l):
    return tuple(tuple(r) for r in l)

class PuzzleProblem(SearchProblem):
    def cost(self, ):
        pass

    def is_goal(self, state):
        pass

    def actions(self, state):
        pass

    def result(self, state, action):
        pass

    def heuristic(self, state):
        pass

#Probar#
if __name__ == '__main__':
    problema = PuzzleProblem(INICIAL)

    # resultado = astar(problema, viewer=WebViewer())
    resultado = astar(problema)

    print 'Estado meta:'
    print resultado.state
    print 'Camino:'
    print len(resultado.path())
    for accion, estado in resultado.path():
        print 'Movi', accion
        print 'Llegue a', estado
import estructura

# Diseno de la estructura
# lista : valor (any = cualquier tipo) siguiente (lista)
estructura.crear("lista", "valor siguiente")

# identificador para listas vacias
listaVacia = None

# crearLista: any lista -> lista
# devuelve una lista cuya cabeza es valor
# y la cola es resto
def crearLista(valor, resto):
        return lista(valor, resto)

# cabeza: lista -> any
# devuelve la cabeza de una lista (un valor)
def cabeza(L): 
	return L.valor

# cola: lista -> lista
# devuelve la cola de una lista (una lista)
def cola(lista):
	return lista.siguiente

# vacia: lista -> bool
# devuelve True si la lista esta vacia
def vacia(lista):
	return lista == listaVacia

#esLista: lista -> bool
#True si L es una lista
#ej: esLista(crearLista(1,listaVacia))->True
def esLista(L):
  return (type(L)==lista) or vacia(L)

assert esLista(crearLista(1,listaVacia))

# enLista: lista(str) str -> bool
# Evalua si un cierto amigo esta en la lista
# Ejemplo: enLista(crearLista("Pedro", listaVacia), "Pedro") devuelve verdadero
#    enLista(listaVacia, "Pedro") devuelve falso
# Plantilla:
# def enLista(l, nombre):
#        ...cabeza(l)....
#       ... cola(l).....
#       .... nombre ...

def enLista(nombre,l):
    if vacia(l):
        return False
    elif (cabeza(l) == nombre):
        return True
    else:
        return enLista(nombre,cola(l))

assert enLista("Pedro",crearLista("Pedro", listaVacia))
assert enLista("Pedro",crearLista("Pedro", crearLista("Juan",listaVacia)))

# Tests

test_lista = lista(1, lista (2, lista(3, listaVacia)))

assert cabeza(test_lista) == 1
assert cabeza(cola(test_lista)) == 2
assert cabeza(cola(cola(test_lista))) == 3
assert cola(cola(test_lista)) == lista(3, listaVacia)

assert vacia(listaVacia)
assert not vacia(test_lista)
assert vacia(cola(cola(cola(test_lista))))


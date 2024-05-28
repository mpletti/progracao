lista = [7, 4]

 

if lista[0] > lista[1]:

    aux = lista[1]

    lista[1] = lista[0]

    lista[0] = aux

 

print(lista)


def executar_selection_sort_2(lista):

    lista_ordenada = []

    while lista:

        minimo = min(lista)

        lista_ordenada.append(minimo)

        lista.remove(minimo)

    return lista_ordenada

 

 

lista = [10, 9, 5, 8, 11, -1, 3]

executar_selection_sort_2(lista)
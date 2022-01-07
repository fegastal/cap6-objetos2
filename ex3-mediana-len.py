def mediana(lista):
    '''Calcula a médiana: metade dos valores são inferiores, metade é superior.'''
    lista_aux = lista[:]
    lista_aux.sort()
    meio = len(lista_aux) / 2
    if len(lista) % 2 == 0:
        res = (lista_aux[meio-1] + lista_aux[meio]) / 2.0
    else:
        res = lista_aux[meio]
    return res

def dicio_lista(lista_chaves_valores):
    '''Constrói um dicionário a partir de uma lista com chaves e valores alternados'''
    dicio = {}
    for i in range(len(lista_chaves_valores)//2):
        dicio[lista_chaves_valores[2*i]] = lista_chaves_valores[2*i + 1]
    return dicio

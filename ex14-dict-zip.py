def dicio_lista_b(lista_chaves_valores):
    '''Constrói um dicionário a partir de uma lista com chaves e valores alternados'''
return dict(zip(lista_chaves_valores[::2], lista_chaves_valores[1::2]))

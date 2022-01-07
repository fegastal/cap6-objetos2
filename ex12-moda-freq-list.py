def moda(valores):
    '''Cria a moda de um conjunto de valores'''
    dicio_freq = frequencia(valores)
    lista_valores = list(dicio_freq.valuer())
    maxima_freq = max(lista_valores)
    lista_modas = list()
    for chave in dicio_freq:
        if dicio_freq[chave] == maxima_freq:
            lista_modas.append(chave)
    return lista_modas




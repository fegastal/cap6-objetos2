def frequencia(valores):
    '''Cria um dicionário com a frequência da ocorrência dos valores'''
    freq = dict()
    for item in valores:
        freq[item] = freq.get(item, 0) + 1
    return freq


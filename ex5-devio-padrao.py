def desvio_padrao(lista):
    '''Calcula o desvio-padrao.'''
    a_media = media(lista)
    soma = 0
    for elem in lista:
        soma = soma + (elem - a_media) ** 2
    desvio = math.sqrt(float(soma) / (len(lista) - 1))
    return desvio

def media(lista):
    '''Calcula a média dos valores contidos na lista.'''

    soma = 0
    for num in lista:
        soma = soma + num

    med = soma / len(lista)
    return med

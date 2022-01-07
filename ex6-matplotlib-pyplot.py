import matplotlib.pyplot
plt = matplotlib.pyplot

def mostra(lista):
    '''Gráfico simples de uma lista de valores.'''
    plt.xlabel('Dias')
    plt.ylabel('Quantidade')
    plt.title('Baleias')
    plt.plot(lista)
    plt.show()

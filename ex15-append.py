def add_palavra_triv(indice, palavra, pagina):
    if palavra in indice:
        indice[palavra].append(pagina)
    else:
        indice[palavra] = [pagina]
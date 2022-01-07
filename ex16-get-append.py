def add_palavra_get(indice, palavra, pagina):
    indice.get(palavra, []).append(pagina)
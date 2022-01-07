def add_palavra_get(indice, palavra, pagina):
    indice.setdefault(palavra, []).append(pagina)
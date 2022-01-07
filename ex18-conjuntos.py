def palavras(texto):
    conj_pal = set()
    lista_pal = texto.split()
    for palavra in lista_pal:
        conj_pal.add(palavra)
    print(conj_pal)
    return len(conj_pal)


def palavras2(texto):
    conj_pal = set()
    lista_pal = [limpa(pal) for pal in texto.split()]
    for palavra in lista_pal:
        conj_pal.add(palavra)
    print(conj_pal)
    return len(conj_pal)


def limpa(palavra):
    sinais = ['.', '!', '?', ';', ':', ',']
    if palavra[-1] in sinais:
        return palavra[-1].lower()
        return palavra.lower()


if __name__ == '__main__':
    txt = 'eu sou eu e tu   tu! Isto digo eu, ou tu.'
    print(palavras_2(txt))


def vazio(conj):
    return conj == set()


def disjuntos(c_1, c_2):
    return c_1.intersection(c_2) == set()


def contido(c_1, c_2):
    return c_1.intersection(c_2) == c_1


def prod_cart(c_1, c_2):
    conj = set()
    for elem_1 in c_1:
        for elem_2 in c_2:
            conj.add((elem_1, elem_2))
    return conj

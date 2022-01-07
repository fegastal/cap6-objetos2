def palavra_chave(nome_utilizador, segredo):
    '''Verifica a palavra chave de um utilizador'''
    codigos = {'ernesto': 'toto', 'patrícia': 'hello31', 'ana': 'gato56'}
    if nome_utiliador not in codigos:
        return 'Não o conheço'


    codigo_correto = codigos[nome_utilizador]
    if segredo == codigo_correto:
        return 'Bem-vindo(a)!'
    else:
        return 'Enganou-se.'

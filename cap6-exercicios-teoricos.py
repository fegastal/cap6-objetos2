'''Exercícios teóricos | Capítulo 6


1) O que distingue as listas dos dicionários?

a) LISTAS

Lista é uma coleção de pares de valores de índice como a matriz em c ++.
A lista é criada colocando os elementos entre [] separados por vírgulas “,“
Os índices da lista são inteiros começando em 0.
Os elementos são acessados por meio de índices.
A ordem dos elementos inseridos é mantida.

As listas são como os arrays, declarados em outras linguagens. As listas não precisam ser sempre homogêneas,
o que o torna uma ferramenta muito poderosa em Python. Uma única lista pode conter DataTypes como Integers,
Strings, bem como Objects. As listas são mutáveis e, portanto, podem ser alteradas mesmo após sua criação.
List = ["Geeks", "For", "Geeks"]

b) DICIONÁRIOS

O dicionário é uma estrutura em hash de pares de chave e valor .
O dicionário é criado colocando elementos em {} como “chave”: ”valor”, cada par de valor-chave é separado por vírgulas “,”
As chaves do dicionário podem ser de qualquer tipo de dados.
Os elementos são acessados por meio de valores-chave.
Não há garantia de manutenção da ordem.

O dicionário em Python, por outro lado, é uma coleção não ordenada de valores de dados, usada para
armazenar valores de dados como um mapa, que, ao contrário de outros tipos de dados, que mantêm apenas
um único valor como elemento, o dicionário mantém key:valuepar. O valor-chave é fornecido no dicionário
para torná-lo mais otimizado. Cada par de valores-chave em um Dicionário é separado por dois pontos :,
enquanto cada chave é separada por uma 'vírgula'.
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}

Obs: É mais eficiente usar um dicionário para a pesquisa de elementos
porque leva menos tempo para percorrer o dicionário do que uma lista.


2) A operação de fatiamento das listas distingue-se da mesma operação para cadeia de caracteres?

Sim. Podemos decompor uma cadeia de caracteres numa lista de cadeias de caracteres recorrendo ao método split.
A divisão da cadeia permite indicar qual é o elemento separador.
ex: lista = frase.split(' ')

Nesse exemplo, usamos o espaço em branco como elemento que separa a frase (fatiamento no caso de cadeia de
caracteres). Do mesmo modo, podemos transformar uma lista de cadeias de caracteres numa cadeia de caracteres única,
usando o método 'join'. A nova cadeia obtém-se justapondo ordenadamente as anteriores e separando-as eventualmente
por um caráter.
ex: nova_frase = ' '.join(lista)

É possível escolher o elemento separador, sendo que no exemplo acima usamos o espaço em branco. A listagem
seguinte mostra outros exemplos de conversão entre listas e cadeias de caracteres.
ex:
lista = frase.split('a')
frase_2 = 'zz'.join(lista)


3) Que tipo de objetos pode ser usado como chave de um dicionário? Quais são suas razões para haver restrições?

Um dicionário é uma coleção não ordenada de pares ordenados de objetos, de comprimento VARIÁVEL, HETEROGÊNEA
e MUTÁVEL. A primeira componente do par designa-se por chave e a segunda por valor. O acesso a cada elemento (cada
par) faz-se por chave e não por posição (como acontece nas sequências). As chaves têm de ser todas DISTINTAS
e de um tipo IMUTÁVEL. Já os valores podem ser de qualquer tipo. Um dos exemplos mais simples:

bases = {'A': 'Adenina', 'C': 'Citosina', 'T': 'Timina', 'G': 'Guanina'}

Marcas sintáticas do dicionário: {}. Como nas listas, as vírgulas separam os elementos. Cada elemento tem,
como já dissemos, duas componentes, sendo que a 1º é a chave e a 2º é o valor.

O construtor do tipo dicionário chama-se dict. Pode ser usado sem argumentos, criando um dicionário vazio,
ou com argumentos. Operações mais comuns: [< chave >] = indexação; in ou not in = pertença; len = quantifica;
del dict[key] = retira o item associado a key.

4) Como podemos saber o tipo do dicionário?

contatos = {'Yan': '1234-5678'}
print(type(contatos))

<class 'dict'>

print(contatos['Ana'])
8765-4321

5) E se não encontramos uma determinada chave, o que acontece?

print(contatos['João'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'João'

Hum… uma exceção de tipo KeyError indicando que a chave 'João' não foi encontrada.
Mas é um pouco estranho imprimir toda essa mensagem para o usuário, não é? Pode ser confuso...
Será que não podemos substituir isso?

6) Qual é o método específico para busca de valores no dicionário?

Os dicionários possuem um método específico para busca de valores, o get(),
no qual podemos passar como parâmetros a chave que queremos e um valor padrão para retornar
caso essa chave não seja encontrada:

print(contatos.get('Yan', 'Contato não encontrado'))
print(contatos.get('João', 'Contato não encontrado'))

1234-5678
Contato não encontrado

Também podemos verificar se um contato está em nosso dicionário através da palavra chave in:

print('Yan' in contatos)
True

print('9999-9999' in contatos)
False
Ué! Mas esse número está sim na agenda, é o número do Pedro! Por que será que o resultado foi False, então?
Acontece que o in, usado dessa forma, verifica apenas as chaves do dicionário, não os valores.
Para obtermos valores, podemos usar o método values():

print('9999-9999' in contatos.values())
True

7) Como adicionar um número novo ao meu dicionário?

Encontrei meu amigo João e, finalmente, decidi adicionar o número dele na minha agenda. Mas… como posso
fazer isso com nosso dicionário de contatos? Fui tentar usar um método append(), como nas listas,
e olha o que apareceu:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'append'

Esse método não existe… Ainda tentei criar um outro dicionário e fazer uma soma, mas o resultado foi esse:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

Também não funciona! A sintaxe de adicionar um item em um dicionário é um pouco diferente
de que em outros tipos do Python, mas também bastante objetiva. Por exemplo, se queremos adicionar
o João no nosso dicionário de contatos, basta atribuir seu telefone na chave 'João':

contatos['João'] = '8887-7778'
print(contatos)

{'Yan': '1234-5678', 'Pedro': '9999-9999', 'Ana': '8765-4321',
  'Marina': '8877-7788', 'João': '8887-7778'}

8) Como apagar um item no dicionário?

Infelizmente, minha amiga Marina perdeu o celular e, consequentemente, não era mais dona do número salvo em meu
dicionário de contatos. Precisamos, agora, apagar o item que corresponde a ela. Mas como?

Uma maneira simples é usando o statement del, dessa forma:

del contatos['Marina']
print(contatos)

{'Yan': '1234-5678', 'Pedro': '9999-9999', 'Ana': '8765-4321',
  'João': '8887-7778'}

del contatos['Catarina']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Catarina'

Um KeyError, como aquele que obtivemos ao tentar pegar um item que não existia! Para evitar
essa exceção, também temos um método de dicionário que pode nos ajudar - o pop().
O método pop(), além de remover o elemento com a chave especificada do dicionário, nos retorna o valor
desse elemento. Também podemos definir um valor padrão de retorno, para caso a chave não seja encontrada:

contatos = {'Yan': '1234-5678', 'Pedro': '9999-9999', 'Ana': '8765-4321',
            'Marina': '8877-7788', 'João': '8887-7778'}

print(contatos.pop('Marina', 'Contato não encontrado'))
print(contatos.pop('Catarina', 'Contato não encontrado'))
print()
print(contatos)

E o resultado:

8877-7788
Contato não encontrado

{'Yan': '1234-5678', 'Pedro': '9999-9999', 'Ana': '8765-4321',
  'João': '8887-7778'}

Tudo certo, agora! Uma pena que tenho poucos contatos na agenda...

9) Como adicionar contatos de outras pessoas no meu dicionário?

Pedi para meu amigo Pedro me ajudar a aumentar minha agenda, adicionando mais alguns amigos como contatos.
Ele me passou a agenda dele:

contatos_do_pedro = {'Yan': '1234-5678', 'Fernando':'4345-5434',
                        'Luiza':'4567-7654'}

Mas e aí? Como adicionamos todos esses contatos em minha agenda? Podemos tentar fazer um loop passando
pelos contatos do Pedro e os adicionando um a um:

meus_contatos = {'Yan': '1234-5678', 'Pedro': '9999-9999',
                    'Ana': '8765-4321', 'João': '8887-7778'}

contatos_do_pedro = {'Yan': '1234-5678', 'Fernando': '4345-5434',
                        'Luiza': '4567-7654'}

for nome in contatos_do_pedro:
    meus_contatos[nome] = contatos_do_pedro[nome]

print(meus_contatos)

Agora vamos ver meu dicionário:

{'Yan': '1234-5678', 'Pedro': '9999-9999', 'Ana': '8765-4321',
  'João': '8887-7778', 'Fernando': '4345-5434', 'Luiza': '4567-7654'}

Certo, funcionou! Mas será que não tem um jeito mais simples de fazermos isso, evitando o laço for?
Repare que queremos juntar nossos dois dicionários em um só - o primeiro. Queremos atualizar o
primeiro dicionário para que contenha também os valores do segundo. Para isso, temos um método
róprio - o update(). Podemos substituir o loop pela chamada do método:

meus_contatos.update(contatos_pedro)
print(meus_contatos)

E o resultado continua certo, com um código mais sucinto!


10) Como adicionar um elemento em todos os números do meu dicionário?

E para adicionar o '9' antes de cada número? uma ideia é fazer isso com um for, o que deve funcionar,
mas será que não tem forma mais simples?
Mais sintático e elegante que um loop for tradicional, entretanto, é o que podemos fazer com
o que já conhecemos da sintaxe de compreensão de lista, mas dessa vez aplicado aos dicionários
compreensão de dicionário. A ideia é a mesma e a sintaxe parecida:

meus_contatos_novo = {nome: '9' + meus_contatos[nome] for nome in meus_contatos}
print(meus_contatos_novo)

{'Yan': '91234-5678', 'Pedro': '99999-9999', 'Ana': '98765-4321',
  'João': '98887-7778', 'Fernando': '94345-5434', 'Luiza': '94567-7654'}

Conseguimos! Agora já conseguimos manipular bem nossa agenda!


11) Porque é que não existe operação de fatiamento em dicionários?

Fatiamento trabalha com objetos mutáveis, sendo que dicionários funcionam melhor com objetos imutáveis.

Não encontrei uma boa resposta. Mas, para dicionários, uma operação semelhante é split.
Fatiamento significa extrair apenas uma parte (subconjunto) da Lista, String ou Tupla.
Essa operação permite delimitar os limites inferior e superior do pedaço da lista que queremos acessar.

Lista[Lim.inf:Lim.sup]
Obs: O limite superior não é incluído no resultado.


12) Que implicações existem pelo facto de os objetos desses tipos serem mutáveis?

CHAVE:
Objeto que aparece em um dicionário como a primeira parte de um par chave-valor.

VALOR:
Objeto que aparece em um dicionário como a segunda parte de um par chave-valor.
Isso é mais específico que o nosso uso anterior da palavra “valor”.

Qualquer tipo imutável pode ser uma CHAVE, como por exemplo uma string, um int, floats e
até mesmo tuplas, desde que esses não contenham objetos mutáveis dentro delas.

Um dicionário é implementado usando uma hashtable e isso significa que é preciso que as CHAVES
possam ser hashable (que seja possível computar seu hash, e que este valor de hash seja IMUTÁVEL).

Hash é uma função que recebe um valor (de qualquer tipo) e devolve um número inteiro.
Dicionários usam esses números inteiros, chamados valores hash, para guardar e buscar pares chave-valor.

Este sistema funciona perfeitamente se as chaves forem imutáveis. Porém, se as chaves são mutáveis,
como listas, coisas ruins acontecem. Por exemplo, quando você cria um par chave-valor, o Python guarda
a chave na posição correspondente. Se você modificar a chave e então guardá-la novamente, ela iria para
uma posição diferente. Nesse caso, você poderia ter duas entradas para a mesma chave, ou pode não conseguir
encontrar uma chave. De qualquer forma, o dicionário não funcionaria corretamente.

É por isso que as chaves têm de ser hashable, e tipos MUTÁVEIS como LISTAS, não são.
A forma mais simples de resolver esta limitação é usar tuplas, que serão vistas no próximo capítulo.

Como os dicionários são mutáveis, eles não podem ser usados como chaves, mas podem ser usados como valores.


13) O que entende por cópia profunda de uma estrutura? Em que situações é útil?

As instruções de atribuição no Python não copiam objetos, elas criam LIGAÇÕES entre um destino e um objeto.
Para coleções que são mutáveis ou contêm itens mutáveis, às vezes é necessária uma cópia para que
seja possível alterar uma cópia sem alterar a outra. Este módulo fornece operações genéricas de cópia
profunda e rasa (explicadas abaixo).

copy.copy(x)
Retorna uma cópia RASA de x.

copy.deepcopy(x[, memo])
Retorna uma cópia PROFUNDA de x.

exception copy.Error
Levantada para erros específicos do módulo.

A diferença entre cópia profunda e rasa é relevante apenas para OBJETOS COMPOSTOS
(objetos que contêm outros objetos, como listas ou instâncias de classe):

Uma cópia rasa constrói um novo objeto composto e então (na medida do possível)
insere nele REFERÊNCIAS aos objetos encontrados no original.

Uma cópia profunda constrói um novo objeto composto e então, recursivamente,
insere nele CÓPIAS dos objetos encontrados no original.

Frequentemente, existem dois problemas com operações de cópia profunda que não existem com operações de cópia rasa:

Objetos recursivos (objetos compostos que, direta ou indiretamente, contêm uma referência a si mesmos)
podem causar um laço recursivo.

Como a cópia profunda copia tudo, ela pode copiar muito, como dados que devem ser compartilhados entre as cópias.

A função deepcopy() evita esses problemas:

mantendo um dicionário memo de objetos já copiados durante a passagem de cópia atual; e
permitindo que as classes definidas pelo usuário substituam a operação de cópia ou o conjunto de componentes copiados.

Cópias rasas de dicionários podem ser feitas usando dict.copy(), e de listas atribuindo uma fatia de toda a lista,
por exemplo, lista_copiada = lista_original[:].


14) Existem métodos que modificam e que não modificam os objetos. O que os distingue?

Os que modificam os objetos, alteram-os, como retirar, adicionar e atualizar. Já os que não modificam,
em nada interferem neles


15) O que são listas por compreensão?

Permitem escrever programas mais compactos e legíveis.
[ <expressão> for <item> in <iterável>]
ex:
def gera_lista_b(n):
    return [randon.randint(1, 100) for i in range(n)]


16) O que permite o uso de enumerate num ciclo?

Devolve um objeto ENUMERADO. "iterable" deve ser uma sequência, um iterador ou algum outro objeto
que suporte a iteração. O método __next__() do iterador retornado por enumerate() devolve uma tupla
contendo uma contagem (a partir de start, cujo padrão é 0) e os valores obtidos na iteração sobre iterable.

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
list(enumerate(seasons, start=1))
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

equivalente a esse programa em um ciclo:
def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1


17) O que permite a função zip?

>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> for t in zip(x, y):
...   print(t)
...
(1, 4)
(2, 5)
(3, 6)

A função retorna uma sequência de tuplas.
Na verdade se olharmos para a função veremos que ela aponta para o objeto instanciado, veja abaixo.

>>>zip(x, y)
<zip object at 0x7faded7b3608>

Para vermos a lista devemos passá-la para a função interna list().

>>> list(zip(x, y))
[(1, 4), (2, 5), (3, 6)]


18) Dê um exemplo de uso de zip.

Imagine que você queira inverter os valores e chaves de um dicionário.
Você tem um dicionário com os valores de ações e seus preços como o exemplo abaixo.

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75,
}

Para inverter o dicionário acima fazemos…

>>> prices_invertido = list(zip(prices.values(), prices.keys()))
>>> for t in prices_invertido:
...   print(t)
...
(45.23, 'ACME')
(205.55, 'IBM')
(37.2, 'HPQ')
(10.75, 'FB')
(612.78, 'AAPL')
>>>

Mas repare que o retorno é uma lista (e não um dicionário).

>>> list(zip(prices.values(), prices.keys()))
[(45.23, 'ACME'), (205.55, 'IBM'), (37.2, 'HPQ'), (10.75, 'FB'), (612.78, 'AAPL')]


19) E se as listas tiverem tamanhos difernetes?

Lista de tamanhos diferentes serão equiparadas e a diferença entre elas será desconsiderado.

list_a = [6, 7, 8, 9]
list_b = [1, 2, 3, 4, 5]

for x in zip(list_a, list_b):
    print(x)
"""
(6, 1)
(7, 2)
(8, 3)
(9, 4)
"""


'''
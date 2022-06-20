## LISTAS
### Descrição simplificada
As listas são uma coleção **ordenada** de valores, que são separados por vírgulas e ficam dentro de colchetes []. Elas têm a função de armazenar itens em uma variável.

### Descrição detalhada

Para criar uma lista vazia:

~~~~ python
lista = []
~~~~

Para criar uma lista com valores, que podem ser de tipos diferentes:

~~~~ python
lista = [‘abacaxi’, ‘pêra’, 2022]
~~~~

A string ‘abacaxi’ encontra-se no índice 0, já ‘2022’ encontra-se no índice 2.

Para percorrer a lista:

~~~~ python

lista = ['abacaxi', 'pêra', 2022]

contador = 0
while contador < len(lista): #Enquanto contador for menor que o tamanho da lista
	print(lista[contador])
	contador += 1

~~~~

Ou também a função “range” pode ser utilizada:

~~~~ python
for i in range (len(lista)):
	print (lista[i])
~~~~

Diferentemente das tuplas, as listas são mutáveis. Para substituir um item da lista:

~~~~ python
lista = ['abacaxi', 'pêra', 2022]
lista[0] = 'morango' #Substitui o abacaxi
~~~~

Slicing: Para extrair apenas uma parte da lista. A forma geral é: lista[ValorDeInicio:ValorDeFim:ValorDoPasso]

Exemplo:
~~~~ python
lista = ['abacaxi', 'banana', 'maçã', 'pêra', 'uva', 'pêssego', 'morango']
print(lista[1:5:2]) #Retorna ['banana', 'pera'].
~~~~

O valor de início é incluso, entretanto o valor de fim é excluso.


**Operadores de listas:**

Concatenação e multiplicação: usando um operador + e multiplicar por inteiros, gerando cópias de itens.

Exemplo concatenação: 
~~~~ python
lista1 = ['banana', 'maçã']
lista2 = ['abacaxi', 'uva']

concatenacao = lista1 + lista2 
~~~~

Exemplo multiplicação:
~~~~ python
lista1 = ['banana', 'maçã']

multiplicacao = lista1 * 3
~~~~~


## MÉTODOS DA CLASSE LISTA:
### Descrição simplificada:
É um método que está contido na lista

### Descrição detalhada:

Incluir itens ao final da lista: nesse caso é usado o **.append(valor)**, em que valor é o novo valor.
Exemplo:
~~~~ python
lista1 = ['banana', 'maçã']

lista1.append('kiwi')
~~~~

Remover itens na lista: é usado **.remove(valor)**. Esse método remove a primeira ocorrência do valor.
Exemplo:
~~~~ python
lista1 = ['banana', 'maçã', 'kiwi']

lista1.remove('kiwi')
~~~~

Também, é possível remover o último item da lista
Exemplo:
~~~~ python
lista1 = ['banana', 'maçã', 'kiwi']

lista1.pop()
~~~~


Incluir vários valores na lista:  é usado **extend()**, estendendo a lista e adicionando os novos itens ao final, também é usado o **.insert(posição, valor)** para ser incluído em uma posição específica da lista.
Exemplo:
~~~~ python
lista1 = ['banana', 'maçã', 'kiwi']

novalista = ['pera', 'melancia', 'abacaxi']

lista1.extend(novalista)
~~~~

ou
~~~~ python
lista1 = ['banana', 'maçã', 'kiwi']

lista1.insert(0, 'abacaxi')
~~~~

Descobrir qual a posição de um item: usando o método** index()**, é retornada a posição de um item na lista.

Exemplo: 
~~~~ python
lista1 = ['banana', 'maçã', 'kiwi']

lista1.index('banana')
~~~~

Ordenando elementos da lista: para ordenar elementos se usa o método **sort()**.
Exemplo: 
~~~~ 
python 
lista1 = ['banana', 'maçã', 'kiwi']

lista1.sort()
~~~~

## LIST COMPREHENSION: 
### Descrição simplificada: 
Cria e manipula listas para otimizar o código.

### Descrição detalhada:
Exemplo sem list comprehension:

~~~~ python
lista = []
for x in range (10):
    lista.append(x*3+2)
~~~~
Exemplo com list comprehension:
~~~~ python
lista = [3*x+2 for x in range(10)]
~~~~

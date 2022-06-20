##MÉTODOS DA CLASSE LISTA:
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

##LIST COMPREHENSION: 
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


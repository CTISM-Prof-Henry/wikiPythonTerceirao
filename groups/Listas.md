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
lista = ['abacaxi', 'pêra', 2022]
~~~~

A string ‘abacaxi’ encontra-se no índice 0, já ‘2022’ encontra-se no índice 2.

Para transformar uma tupla ou conjunto em uma lista aplica-se a função **list()**:

~~~~python
tupla = ('morango', 'pêra', 'damasco')
lista = list(tupla)
~~~~

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


## MÉTODOS DA CLASSE LISTA
### Descrição simplificada
É um método que está contido na lista

### Descrição detalhada

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

Descobrir qual a posição de um item: usando o método **index()**, é retornada a posição de um item na lista.

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

## LIST COMPREHENSION
### Descrição simplificada
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

##OPERADORES AND, OR, IN, NOT IN PARA LISTAS
### Descrição simplificada
São operadores para verificar se um determinado objeto está contido ou não em uma lista. 

##Descrição Detalhada

**IN** - Usado para verificar se há um determinado valor contido na lista, consequentemente aparecerá true ou false.

~~~~ python
lista1 = [‘maçã’, ‘abacaxi’, ‘kiwi’]

print [‘abacaxi’ in lista]
#True
print[‘Morango’ in lista]
#False
~~~~

**NOT IN** -  Usado para verificar se um determinado valor não está contido na lista. Serve ao contrário do IN.


~~~~ python
lista1 = [‘maçã’, ‘abacaxi’, ‘kiwi’]

print[‘morango’ not in lista1]
#True
print[‘maçã’ not in lista1]
#False
~~~~

**AND** -  Operador que irá unir uma ou mais sentenças para que possa operar. Ambas as sentenças precisam ser verdadeiras para retornar True.

~~~~ pyton
lista1 = [‘ maçã’, ‘abacaxi’, ‘kiwi’]

print['abacaxi' in lista1 and 'morango' not in lista1]
#True
print['maçã' in lista1 and 'kiwi’ not in lista1]
#False
~~~~

**OR** - Apenas uma das sentenças precisa de ser verdadeira para que o valor retorne como verdadeiro, e só retornará falso caso ambas sentenças sejam falsas.

~~~~ pyton 
lista1 = [‘maçã’, ‘abacaxi’, ‘kiwi’]

print [‘morango’ in lista1 or ‘kiwi’ in lista1]
#True
print [‘pêra’ in lista1 or ‘uva’ in lista1]
#False


## EXERCÍCIOS
### Exercício 1

Considere a seguinte lista:

disciplinas = ['história', 'geografia', 'português', 'matemática', 'biologia', 'física', 'química', 'literatura', 'filosofia']

Faça um programa que: 
- Substitua ‘português’ por ‘sociologia’;
- Remova o último item da lista;
- Retorne apenas uma lista com ‘sociologia’, ‘biologia’ e ‘química’.

**Resolução**

~~~~python
disciplinas = ['história', 'geografia', 'português', 'matemática', 'biologia', 'física', 'química', 'literatura', 'filosofia']

disciplinas[2] = 'sociologia'
disciplinas.pop()
print(disciplinas[2::2])
~~~~

### Exercício 2

Dez lutadoras de Muay Thai inscreveram-se na categoria Peso Pena (Featherweight) - até 65kg -. Caso o peso ultrapasse o limite permitido na categoria, a lutadora é desclassificada da competição. Portanto, faça um programa que  verifique se há alguma lutadora desclassificada e indique a quantidade. 

lutadoras = ['Márcia', 'Rafaela', 'Eduarda', 'Gabriela', 'Larissa', 'Isabela', 'Natália', 'Maria', 'Helena', 'Patrícia']

pesos = [64.2, 74, 71.8, 57, 61, 54.3, 79, 42, 67, 55.6]

**Resolução**

~~~~python
lutadoras = ['Márcia', 'Rafaela', 'Eduarda', 'Gabriela', 'Larissa', 'Isabela', 'Natália', 'Maria', 'Helena', 'Patrícia']

pesos = [64.2, 74, 71.8, 57, 61, 54.3, 79, 42, 67, 55.6]

quantidadeLutadoras = 0
for i in range(0, len(lutadoras)):
    if pesos[i] > 65:
        quantidadeLutadoras = quantidadeLutadoras + 1

print('A quantidade de lutadoras que não poderão participar da competição pois estão acima do peso é:', quantidadeLutadoras)
~~~~



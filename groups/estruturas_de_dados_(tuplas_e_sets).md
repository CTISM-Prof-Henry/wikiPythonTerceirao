
# Estruturas de Dados

## Tuplas
#### Simplificando: 
* Tuplas são um tipo de estrutura de dados numerados e imutáveis. 
* Definidos por () e separados por “,”. 
* Valores duplicados são aceitos.

```python
tuplaDoGrupo = ('Bruno', 'Luize', 'Gianna')
print(tuplaDoGrupo)

('Bruno', 'Luize', 'Gianna')
```
#### Expandindo:
* Tuplas são um dos 4 tipos de estrutura de dados em Python, usadas para armazenar múltiplos dados em uma única variável. Semelhantes a listas, são numeradas, contudo se diferem das mesmas por serem imutáveis . São definidas por parênteses e separadas por vírgulas. Valores duplicados são aceitos em tuplas, além de diversos tipos de dados, como strings, números e até mesmo listas ou outras tuplas.
```python
tuplaDoGrupo = ('Bruno', 'Luize', 'Gianna')
print(tuplaDoGrupo)

('Bruno', 'Luize', 'Gianna')
```
* É possível pegar um item da tupla por sua posição (que seguindo a lógica presente na linguagem Python, sua contagem começa no [0]):

```python
tuplaDoGrupo = ('Bruno', 'Luize', 'Gianna')
print(tuplaDoGrupo[0])

Bruno
```
* Também é possível imprimir o tamanho da tupla a partir do comando len():
```python
tuplaDoGrupo = ('Bruno', 'Luize', 'Gianna')
print(len(tuplaDoGrupo))
```
* Outra forma de definir uma tupla é pelo função ‘tuple()’
```python
tuplaDoGrupo = tuple(('Bruno', 'Luize', 'Gianna'))
print(tuplaDoGrupo)

('Bruno', 'Luize', 'Gianna')
```
* Outra operação com tuplas é a união de duas tuplas, adicionando seus itens em uma nova tupla:
```python
meninasDoGrupo = tuple(('Luize', 'Gianna'))
meninosDoGrupo = ('Bruno',)
integrantesDoGrupo = meninasDoGrupo+meninosDoGrupo
print(integrantesDoGrupo)

('Bruno', 'Luize', 'Gianna')
```
* Existem dois métodos para tuplas, um para contar o número de vezes que um item se repete na tupla(.count()) e outro para retornar a posição em que um item se encontra na tupla(.index()).

```python
integrantesDoGrupo = ('Bruno', 'Bruno','Luize', 'Gianna')
print( integrantesDoGrupo.count('Bruno'))
print( integrantesDoGrupo.index('Luize'))

2
2
```

## Sets (Conjuntos) 
#### Simplificando:
* Dados inumerados, ou seja, não possui ordem fixa.
* Podem ser realizadas operações matemáticas como união, intersecção e diferença.
* Utilizações comuns:
  * Verificar existências de objetos dentro de conjuntos diferentes;
  * Eliminar objetos duplicados.

#### Expandindo: 
Os conjuntos são definições de uma coleção de dados que não possuem sequência pré definida e também são mutáveis, assim, podendo adicionar mais itens dentro da coleção ao longo do código python. Os sets também possibilitam operações matemáticas como a união, intersecção, diferença e diferença simétrica de conjuntos. Veja os exemplos:

### INTERSECÇÃO:
```python
sorvete = {'creme', 'chocolate', 'avela', 'chocomenta', 'blue ice'}  # definindo o primeiro conjunto
print('Conjunto Sorvete: ',sorvete)  # mostrando na tela
milk_shake = {'chocolate', 'morango', 'baunilha', 'flocos', 'avela'}  # definindo o segundo conjunto
print('Conjunto Milk Shake', milk_shake)  # mostrando na tela
sabores_em_comun = sorvete.intersection(milk_shake)  # realizando a intersecção dos conjuntos (itens em comun)
print('Sabores em Comum: ', sabores_em_comun)  # mostrando na tela o resultado da união
```
## Saída de tela:
```bash
Conjunto Sorvete:  {'avela', 'chocolate', 'blue ice', 'creme', 'chocomenta'}
Conjunto Milk Shake {'baunilha', 'flocos', 'avela', 'morango', 'chocolate'}
Sabores em Comum:  {'avela', 'chocolate
```
## UNIÃO:

```python
sorvete = {'creme', 'chocolate', 'avela', 'chocomenta', 'blue ice'}  # definindo o primeiro conjunto
print('Conjunto Sorvete: ',sorvete)  # mostrando na tela
milk_shake = {'chocolate', 'morango', 'baunilha', 'flocos', 'avela'}  # definindo o segundo conjunto
print('Conjunto Milk Shake', milk_shake)  # mostrando na tela
todos_os_sabores = sorvete.union(milk_shake)  # realizando a uniao dos conjuntos (juntando todos os itens sem repetir os que sao de ambos)
print('Sabores em Comum: ', todos_os_sabores)  # mostrando na tela o resultado da união
```
## SAÍDA: 
```bash
Conjunto Sorvete:  {'chocomenta', 'chocolate', 'creme', 'blue ice', 'avela'}
Conjunto Milk Shake {'flocos', 'baunilha', 'chocolate', 'morango', 'avela'}
Sabores em Comum:  {'chocomenta', 'flocos', 'creme', 'baunilha', 'chocolate', 'morango', 'blue ice', 'avela'}
```
## DIFERENÇA:
```python
sorvete = {'creme', 'chocolate', 'avela', 'chocomenta', 'blue ice'}  # definindo o primeiro conjunto
print('Conjunto Sorvete: ', sorvete)  # mostrando na tela
milk_shake = {'chocolate', 'morango', 'baunilha', 'flocos', 'avela'}  # definindo o segundo conjunto
print('Conjunto Milk Shake', milk_shake)  # mostrando na tela
diferença = sorvete.difference(milk_shake)  # realizando a diferença dos conjuntos
print('Diferença: ', diferença)  # mostrando na tela o resultado da união
```
## Saída de tela: 
```bash
Conjunto Sorvete:  {'chocomenta', 'blue ice', 'avela', 'creme', 'chocolate'}
Conjunto Milk Shake {'morango', 'avela', 'baunilha', 'flocos', 'chocolate'}
Diferença:  {'chocomenta', 'blue ice', 'creme'}
```
## Adicionando ou removendo itens:
```python
sorvete = {'creme', 'chocolate', 'avela', 'chocomenta', 'blue ice'}  # definindo o primeiro conjunto
print('Conjunto Sorvete: ', sorvete)  # mostrando na tela
milk_shake = {'chocolate', 'morango', 'baunilha', 'flocos', 'avela'}  # definindo o segundo conjunto
print('Conjunto Milk Shake', milk_shake)  # mostrando na tela
sorvete.add('napolitano')  # Adicionando o novo sabor com o comando add
print('Com o sabor novo: ', sorvete)  # mostrando na tela
sorvete.remove('creme')  # removendo um sabor com o comando remove
print('Sem o sabor creme', sorvete
```
## saída de tela: 
```bash
Conjunto Sorvete:  {'blue ice', 'chocomenta', 'avela', 'chocolate', 'creme'}
Conjunto Milk Shake {'morango', 'flocos', 'baunilha', 'avela', 'chocolate'}
Com o sabor novo:  {'blue ice', 'napolitano', 'chocomenta', 'avela', 'chocolate', 'creme'}
Sem o sabor creme {'blue ice', 'napolitano', 'chocomenta', 'avela', 'chocolate'}
```
## Operadores IN, NOT IN, AND e OR:

* IN: operador que serve para identificar se um valor faz parte da estrutura de dados, retornando um valor booleano como resultado:
```python
tuplaDoGrupo = ('Bruno','Luize', 'Gianna')
print('Gianna' in tuplaDoGrupo)
print('Henry' in tuplaDoGrupo)

True
False
```

* NOT IN: operador que serve para identificar se um valor não faz parte da estrutura de dados, retornando também um valor booleano como resultado:
```python
tuplaDoGrupo = ('Bruno','Luize', 'Gianna')
print('Bruno' not in tuplaDoGrupo)
print('Henry' not in tuplaDoGrupo)

False
True
```

* AND: operador que serve para unir duas ou mais sentenças ao operar a estrutura de dados, onde ambas as sentenças terão de ser verdadeiras para que o valor retorne como verdadeiro:
```python
tuplaDoGrupo = ('Bruno','Luize', 'Gianna')
print('Gianna' in tuplaDoGrupo and 'Henry' not in tuplaDoGrupo)
print('Henry' in tuplaDoGrupo and 'Luize' in tuplaDoGrupo)

True
False
```

* OR: operador que serve para unir duas ou mais sentenças ao operar a estrutura de dados, onde apenas uma das sentenças precisa de ser verdadeira para que o valor retorne como verdadeiro, e só retornará falso casos ambas sentenças sejam falsas: 
```python
tuplaDoGrupo = ('Bruno','Luize', 'Gianna')
print('Henry' in tuplaDoGrupo or 'Bruno' in tuplaDoGrupo)
print('Gianna' not in tuplaDoGrupo or 'Luize' not in tuplaDoGrupo)

True
False
```
## Exercicios

* 1: Crie um programa que mostre quantas vezes o primeiro número da tupla se repete.
- `entrada`
```python
tupla = 5,6,3,6,5,7,9
print(tupla)
conta = tupla.count(tupla[0])
print('O primeiro numero se repete:',conta)
```
- `saída`
```bash
(5, 6, 3, 6, 5, 7, 9)
O primeiro numero se repete: 2
```
* 2: Escreva um programa que mostre dois conjuntos e depois mostre a intersecção deles. 

- `entrada`
```python
conjA = set(["amarelo", "azul","vermelho"])
conjB = set(["verde", "amarelo", "roxo"])
print("Conjuntos:")
print(conjA)
print(conjB)
print("\nIntersecção dos conjuntos:")
conjC = conjA & conjB
print(conjC)
```bash
- `saída`
``` 
Conjuntos:
{'azul', 'amarelo', 'vermelho'}
{'amarelo', 'roxo', 'verde'}

Intersecção dos conjuntos:
{'amarelo'}
```
* 3: Crie um programa que encontre as diferenças entre os conjuntos. 

- `entrada`
```python
def conjuntos(A , B):   
    conjunto_B = set({})
    for x in A:
        if x not in B:
            conjunto_B.add(x)           
    return conjunto_B
A = {'8', '4', '1', '6', '7', '2', '4', '9'} 
B = { '2', '3', '9','6','4', '1', '6'}
print('Conjunto A:', A)
print('Conjunto B:', B)
print("Diferença: " , conjuntos(A , B))
```


- `saída`
```bash
Conjunto A: {'2', '1', '9', '7', '8', '4', '6'}
Conjunto B: {'2', '3', '1', '9', '4', '6'}
Diferença:  {'7', '8'}
```

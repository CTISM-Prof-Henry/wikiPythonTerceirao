# Laços de Repetição 

## Explicação Simplificada:
-
-
-

## Explicação Detalhada:

### While:
-
-
-

### For:
-
-
-

### Função Range:

#### Explicação:
A função range tem como objetivo retornar um iterador, que também podemos explicar comparando range com if, pois ambas são funções que têm suas ordens a serem executadas.

```python

for i in range(7):
    print(i)

```
```
Retorna: 0  1  2  3  4  5  6
```

No exemplo acima podemos ver que o 7 define até onde a função range deverá ir, e i seria o responsável por receber um número correspondente ao iterador de função range.

#### Manipulação: 
A função range tem maneira de ser usada para diferentes retornos, range tem 3 maneiras de ser manipulada. 
##### Situação 1:
```python

for i in range(0, 9, 1):
    print(i)

```
```
Retorna: 0 1 2 3 4 5 6 7 8
```
##### Situação 2:
```python

for i in range(7, 10, 1):
    print(i)

```
```
Retorna: 7 8 9
```
##### Situação 3:
```python

for i in range(0, -15, -2):
    print(i)

```
```
Retorna: 0 -2 -4 -6 -8 -10 -12 -14
```

Na Situação 1, somente dizemos a função até onde ela vai, e o 0 e 1 presentes na situação representa como normalmente a função seria lida se ela só tivesse o 9 como parâmetro.
Na Situação 2, como primeiro parâmetro colocamos o 7 e nele representamos onde a função rance deva começar a contar.
Na Situação 3, agora colocamos o terceiro parâmetro e assim dizemos a função que queremos pular alguns números.    

#### Funções com range:

##### Situação 1:
```python

a = list(range(15))
print(a)

```
```
Retorna: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
```
A função list() faz com que os iteradores da função range se tornem uma lista.

##### Situação 2:
```python

profs = ['Henry', 'Zolin', 'Suzi', 'Rosicleia']
for i in range(len(profs)):
    print(i, profs[i])

```
```
Retorna: 
0 Henry
1 Zolin
2 Susi
3 Rosicleia
```
A função len() transforma as posições de uma lista em números que correspondem às suas posições. 

##### Situação 3:
```python

a = sum(range(8))
print(a)

```
```
Retorna: 28
```
A função sum() somas os interadores da range. 

### Break:

O comando break é usado para interromper um laço de repetição, fazendo com que se saia dele. Exemplo no código abaixo:

```python

a = 0
for i in range(1, 5):
    for j in range(1, 5):
        if j % 2 == 0:
            a = a + j
            print(a)
            break
        else:
            a = a + i
            print(a)

```
```
Retorna: 1 3 5 7 10 12 16 18
```
No código acima, o break sai do laço em que ele está e vai para o for anterior, assim dando sequência ao código. Mas no código abaixo, podemos ver que se usarmos break em laço de um único for o código parará de rodar:

```python

for i in range(1, 10):
        if i % 4 == 0:
            print(i, 'é múltiplo de 4')
            break
        else:
            print(i, 'não é múltiplo de 4')

```
```
Retorna: 
1 não é múltiplo de 4
2 não é múltiplo de 4
3 não é múltiplo de 4
4 é múltiplo de 4
```
Nesse caso somente o primeiro número múltiplo de 4 seria printado, pois logo após dele printar um múltiplo de 4 a função break seria executada, assim parando o código. 

### Continue: 

Ao invés de sair do laço que já está, a função continue
somente pula para o próximo parâmetro de execução.

```python

for i in range(10):
    if i % 3 == 0:
        print(i)
        continue
    else:
        print(i, "esse número não presta")

```
```
Retorna: 
2 esse número não presta
3
4 esse número não presta
5 esse número não presta
6
7 esse número não presta
8 esse número não presta
9
```

## Exercícios:

### Exercício 1:
-
-
-

### Resolução: 
-
-
-


### Exercício 2:
- A)Vamos supor que tenhamos uma lista a, que contém todos os números inteiros entre 0 e 99 (por exemplo, a = [0, 1, 2, 3, ..., 99]). Usando laços de repetição, e NÃO USANDO listas, faça um código que imprime
a[:50](50 à 99) na tela.
- B)Faça outro código que imprime a[50:](0 à 49) na tela

### Resolução2 a):
~~~Python
for i in range(99):
    if i < 50:
        continue
    print(i)
~~~~
### Resolução: 
~~~python
for i in range(99):
    print(i)
    if i >= 50: 
        break
~~~

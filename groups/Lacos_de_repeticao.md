# Laços de Repetição 

1. [While](#Funções-Range)
1. [For](#Funções-Range)
1. [Função Range](#Função-Range)
1. [Break](#Break)
1. [Continue](#Continue)
1. [Exercícios](#Exercícios)

## Explicação Simplificada:

- While e For são estrturas de repetição, que servem para fazer com que uma certa parte do algoritmo se repita nela mesma.
- Range é uma função que serve para criar uma sequência de números iteráveis.
- Break serve para "quebrar" um laço de repetição. É utilizado para parar um laço.
- Continue tem a função de acabar com a iteração atual do loop do laço e passar para a próxima, pulando qualquer coisa que estiver após, no laço.

## Explicação Detalhada:

### While:

#### Explicação:
O While é uma estrutura de repetição usada para que determinado comando seja realizado enquanto uma determinada condição for satisfeita. 

#### Exemplo 1: 

```python
num = 1
while (num != 0):
	print(num)
	num = int(input('Digite um número: '))
```
```python
Retorna:
1
Digite um número: 2
2
Digite um número: 10
10
Digite um número: 0
Process finished with exit code 0
```
Neste exemplo o laço irá se repetir enquanto a variável num for diferente de 0. Quando ela for 0, o laço irá parar.

#### Exemplo 2:

```python
ratinho = input('Digite um efeito sonoro do ratinho: ')
while ratinho:
	input('Digite um efeito sonoro do ratinho: ')
```
```python
Retorna:
Digite um efeito sonoro do ratinho: UEEPAAAAA
Digite um efeito sonoro do ratinho: RAPAIZZZZ
Digite um efeito sonoro do ratinho: PARE!
Digite um efeito sonoro do ratinho:
```
Neste exemplo o while será infinito, pois o input não está colocando o que é digitado na variável. O mesmo poderia acontecer no exemplo 1, caso não houvesse "num = int(input('Digite um número: '))", o programa iria imprimir 1 infinitamente. Assim:
```python
num = 1
while (num != 0):
	print(num)
```
```python
Retorna: 1 1 1 1 1 1 1 1 1 1 1 1 ...
```

### For:
#### Explicação
O for é uma estrutura de repetição usada para fazer repetições controladas, determinando quando começa e quando termina. Aceita listas e strings.

#### Exemplo 1.1:

```python
for i in range(10):
	print(i)
```
```python
Saída: 0 1 2 3 4 5 6 7 8 9
```
Neste caso foi pedido que ocorram 10 interações e, por padrão, o python começa pelo 0 e irá até o 9.

#### Exemplo 1.2:

```python
for i in range(4, 10)
	print(i)
```
```python
Saída: 4 5 6 7 8 9
```

O primeiro parâmetro do range determina onde irá começar e o segunda onde ele irá terminar. Aqui, ele irá até 9, pois, em python, ele não inclui o último valor. 

#### Exemplo 1.3:

```python
for i in range(4, 10, 2)
	print(i)
```
```python
Saída: 4 6 8
```
O terceiro parâmetro irá determinar o "passo" que ele dará, neste caso, ele irá "pular" de 2 em 2. 

#### Exemplo 2:
```python
ratinho = ['UEPA', 'RAPAIZ', 'PARE!']
for audio in ratinho:
	print(audio)
```
```python
Saída: UEPA RAPAIZ PARE!
```
O for também funciona para interagir com os elementos dentro de uma lista, neste caso ele apenas exibe cada elemento na tela.

### Função Range:

#### Explicação:
A função range tem como objetivo retornar um iterador, que também podemos explicar a comparar range com if, pois ambas são funções que têm as suas ordens a serem executadas.

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

Escolha um número, então faça com que o código peça um número até que o usuário acerte o número escolhido. Utilize While.
#### Exemplo de saída:
~~~Python
Digite um número: 1
Digite um número: 7
Digite um número: 12
Digite um número: 0
ACERTOU!!!
~~~
### Resolução: 
~~~Python
num = 1
while (num != 0):
    num = int(input('Digite um número: '))

print('ACERTOU!!!!')
~~~
### Exercício 2:
- a)Vamos supor que tenhamos uma lista a, que contém todos os números inteiros entre 0 e 99 (por exemplo, a = [0, 1, 2, 3, ..., 99]). Usando laços de repetição, e NÃO USANDO listas, faça um código que imprime
a[:50] na tela.
- b)Faça outro código que imprime a[50:] na tela

### Resolução a):
~~~Python
for i in range(99):
    if i < 50:
        continue
    print(i)
~~~~
### Resolução b): 
~~~python
for i in range(99):
    print(i)
    if i >= 50: 
        break
~~~

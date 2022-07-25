# Números e expressões aritméticas

Os dois tipos numéricos mais comuns em Python são int e float, usados para 
representar, respectivamente, números inteiros e reais (também chamados de ponto
flutuante). Utilizando operadores aritméticos, conseguimos expressar operações 
matemáticas em Python.
 
## Sumário

* do
* it
* later

### Usando Python como calculadora

Por ser capaz de realizar diversas expressões aritméticas o interpretador Python
pode ser utilizado como uma calculadora. Dessa forma, é possível inserir 
variáveis numéricas e utilizá-las como bem entender. Esses números podem ser 
apresentados como: 

* **int**: números **sem parte decimal ou fracionada**, com a possibilidade de 
           serem negativos ou positivos.
  * exemplos: 5.0; -24.0; 37
* **float**: números **com parte decimal**, com a possibilidade de serem 
  negativos ou positivos.
  * exemplos: 3.5; -45.68; 12.35

## Números inteiros (int)

```python
idade = int(input('digite sua idade:')) 
ano_nascimento = int(input('digite o ano em que nasceu:')) 

print('Você tem',idade, 'anos e nasceu em', ano_nascimento)
```

Caso for inserido um número float no lugar de um int, aparecerá a confirmação de erro:

```
ValueError: invalid literal for int() with base 10: '(número errado adicionado)'
```

## Números de ponto flutuante (float)

```python
raio = float(input('Digite o valor do raio: '))

circunferencia = 2 * 3.14 * raio

print("A circuferência do círculo é:", circunferencia)
```

## Conversão de tipos

* Usando as funções **float()** e **int()** (que também são conhecidas como
cast), é possível converter o tipo da variável numérica:

```python
i = 10 # int
f = 5.1 # float

i = float(i) # passando i para float
f = int(f) # passando f para int

print('a conversão de i é:', i)
print('a conversão de f é:', f)
```

Saída:

```
a conversão de i é: 10.0
a conversão de f é: 5
```

Repare que o i ganhou .0 ao final e que f não possuí mais parte decimal.

## Verificação de tipos

* As funções **isinstance()** e **type()** podem ser usadas para verificar o 
tipo de uma variável.

```python
i = 10 # int
f = 5.1 # float

print('o tipo da variável i é:', type(i))
print('o tipo da variável f é:', type(f))
print('i é int?', isinstance(i, int))
print('f é float?', isinstance(f, float))
```

Saída:

```
o tipo da variável i é: <class 'int'>
o tipo da variável f é: <class 'float'>
```

## Expressões aritméticas

As expressões aritméticas possuem operandos (números ou variáveis) e operadores.
Com eles podemos realizar operações matemáticas.

|  Operador    | Função           | Exemplo          |
|:------------:|:-----------------|:-----------------|
|      +       | Soma             | `30 + 45 = 75`   |
|      -       | Diferença        | `120 - 15 = 105` |
|      *       | Multiplicação    | `43 * 5 = 215`   |
|      **      | Potenciação      | `43 ** 2 = 1849` |
|      /       | Divisão          | `42 / 5 = 8`.6   |
|      //      | Divisão inteira  | `42 // 5 = 8`    |
|      %       | Resto de divisão | `42 % 5 = 3`     |

Os operadores + e - servem tanto para soma e diferença, quanto para demonstrar 
se o número é positivo ou negativo.

```python
a = -4 + 10
print('a será:', a)

b = -4 + (-10)
print('b será:', b)
```

Saída:

```
a será: 6
b será: -14
```

### Exercícios

1. Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

```python
num = int(input('digite um número:'))
print(
  'analisando o número', num, 'o número sucessor é', (num+1), 
  'e o antecessor é', (num-1)
)
```

Saída:

```
digite um número:10
analisando o número 10 o número sucessor é 11 e o antecessor é 9
```

2. Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz 
quadrada.

```python
num = int(input('digite um número:'))
print('o dobro do número é:', (num * 2), 'o triplo é:', (num * 3), 'e a raiz quadrada é:', (num ** 0.5))
```

Saída:

```
digite um número:25
o dobro do número é: 50 o triplo é: 75 e a raiz quadrada é: 5.0
```


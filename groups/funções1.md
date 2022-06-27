# RESUMO SIMPLIFICADO


### Argumentos Nomeados

* Argumentos posicionais são os parametros que passados por posição para a função.
* Arguementos nomeados são os parametros que passamos por nome para a função.


### Docstrings
* comentários
* sintaxe:
~~~~python
	"""Termina com ponto final e inicia com letra maiúscula.
	
	Identação abaixo nas aspas.
	
	Se tiver mais de uma linha, falhar uma entre elas.
	
	Serve para explicar o que uma função esta fazendo. 
	
	"""

~~~~



### ARGUMENTOS NOMEADOS:

#### Argumento posicional
é um argumento passado para a função por posição. 
~~~~python
def funcao(a, b):
	print(a, b)

funcao(1, 2)
~~~~
Na função são passados dois parâmetros, a e b e os valores foram passados em *funcao(1, 2)*, então a = 1 e b = 2. Eles são argumentos posicionais.

#### Argumento nomeado 
são argumentos que passamos por nome para a função. 
~~~~python
def funcao(a, b):
	print(a, b)
	
	
funcao(a='hello', b=' world') 
~~~~
Foi atribuido o valor de ' world' para b e 'hello' para a.
 
### STRINGS DE DOCUMENTAÇÃO OU DOCSTRINGS:

É basicamente os comentários, eles são utilizados para mostrar como que o algoritmo funciona, facilitando a vida da pessoa que esta vendo o código e não esta entendendo.
O interpretador python ele não reconhece esses comentários como um comando executável, então ele simplismente o ignora.  

#### Sintaxe:

* Em python é utlizado as """ (três aspas duplas) para comentar um bloco de código, porém não se esqueça de fecha-las. 
* Deve iniciar com letra maiúscula e terminar com ponto final.
* Falhar uma linha se a explicação tiver mais de uma, e o inicio da frase deve ser iniciada em baixo da identação das aspas. 

Ex:
~~~~python
def soma(a, b):
    print (a + b)
    """A função vai atribuir os valores passados por a e b .
       
    Vai somar eles e mostrar o resultado.
    """

soma(5, 2) 
~~~~

### Exercícios 👾
1- Faça um programa que tenha uma função com argumentos padrão que mostre o resta da divisão de dois números e exiba na tela.
Você pode escolher quais vão ser eles. E faça um comentário utilizando as regrinhas das docstrings mostrando qual o nome, parametro, retorno e corpo da sua função.  
* Resolução
~~~~python
def resto_divisao(numero1=5, numero2=2):
	resto = numero1 % numero2
	return  resto
	
	""" Nome: resto_divisão.
	Parametro: numero1 e numero2.
	Retorno: resto.
	Corpo: linhas 2 e 3.
	"""

print("Resto da divisão é: ", resto_divisao())
~~~~

2 - O xaropinho não frequentou o ensino fundamental e não sabe fazer cálculos matemáticos, e ele quer sua ajuda! Ele pediu para você fazer uma calculadora em python que peça dois números e mostre a soma, divisão, subtração, quadrado do primeiro e do segundo e multiplicação. Ele quer que você sofra, então quer que seja feita uma função para cada cálculo, e exiba na tela os resultados. 
*Resolução
~~~~python
def soma(n1, n2):
	return n1 + n2

def subtr(n1, n2):
	return n1 -n2

def vezes(n1, n2):
	return n1 * n2

def divisao(n1, n2):
	return n1 / n2

def quadrado1(n1):
	return n1 ** 2

def quadrado2(n2):
	return n2 **2


n1 = float(input("Digite um numero:"))
n2 = float(input("Digite um numero:"))

print("A soma é:", soma(n1, n2))
print("A subtração é:", subtr(n1, n2))
print("A divisão é:", divisao(n1, n2))
print("A multiplicaçao é", vezes(n1, n2))
print("o quadrado do numero ", n1 , "é", quadrado1(n1))
print("o quadrado do numero ", n2 , "é", quadrado1(n2))
~~~~

3- Escreva uma função que recebe dois parâmetros, `texto` e `caixa_alta`. O parâmetro `texto` **não possui** valor padrão, porém o parâmetro `caixa_alta` possui o valor padrão `False`. Esta função deve imprimir o texto `texto` na tela. Quando `caixa_alta = True`, o texto impresso deve ser em MAIÚSCULAS. Quando `caixa_alta = False`, o texto deve ser impresso (todo ele) em minúsculas (independente do usuário tê-lo digitado em minúsculas ou não). Observe os exemplos:

```python
imprime('olá mundo!')  # vai imprimir 'olá mundo!'
imprime('OLÁ MUNDO!')  # vai imprimir 'olá mundo!'
imprime('olá mundo!', caixa_alta=False)  # vai imprimir 'olá mundo!'
imprime('Olá Mundo!', caixa_alta=False)  # vai imprimir 'olá mundo!'
imprime('olá mundo!', caixa_alta=True)  # vai imprimir 'OLÁ MUNDO!'
```
*Resolução
```python
def imprime(texto, caixa_alta=False):
	if caixa_alta == False:
		print(texto.upper())

	else:
		print(texto.low())
	
	
imprime(texto='hello', caixa_alta=False)
```

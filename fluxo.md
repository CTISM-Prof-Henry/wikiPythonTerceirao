### Fluxo

#### if 

O if é uma estrutura de condição que permite avaliar uma expressão e, de acordo com seu resultado, executar uma determinada ação.
Sua estrutura é:

~~~~python
def func():
	a = int(input('insira valor de A')) # capta um valor para A
	b = int(input('insira valor de B')) #capta um valor para B

	if b > a: # SE b for maior que A executa o comando
		print('B é maior que A') 

~~~~

#### elif

Utiliza-se o elif com mesmo intuito do if, porem ele significa uma segunda exceção.
Sua estrutura é:

~~~~python
def func():
	a = int(input('insira valor de A'))
	b = int(input('insira valor de B'))

	if b > a:
		print('B é maior que A')

	elif a > b: # OU SE a for maior que b executa o comando
		print('A é maior que B')

~~~~

#### else

Quando nenhum comportamento específico foi definido para o caso de a condição não ser satisfeita, utiliza-se a estrutura else.
Sua estrutura é:

~~~~python
def func():
	a = int(input('insira valor de A'))
	b = int(input('insira valor de B'))

	if b > a:
		print('B é maior que A')

	elif a > b:
		print('A é maior que B')

	else: # SENAO executar nenhum comando acima, executar o seguinte
		print('A é igual a B') #igual pois if e elif analisa os valores diferentes

~~~~

#### exercicios 

1. faça um programa o qual peça o valor de três números e mostre o menor deles

##### resolução:

~~~~python

~~~~

2. faça um programa que peça um número, depois mostre se ele é positivo ou negativo, caso nao seja nenhuma das duas opções (seja 0), mostre a mensagem "o numero digitado é (numero digitado)" (utilize else)

##### resolução:

~~~~python

~~~~

3. faça um programa que peça o numero de episodios que o usuario assistiu do programa do ratinho. Se o usuario tiver assistido até 25 episódios, mostre na tela a mensagem "RAPAIZ", se assistiu ate 50, mostre a mensagem "UEPAA", se assistiu mais que 50, exiba a mensagem "RATINHOO"

##### resolução:

~~~~python

~~~~

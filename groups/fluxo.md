### Fluxo

#### Resumo simplificado: 

Em python o programa deve ser capaz de tomar decisões baseadas em comandos anteriores, a estrutura de decisão vai checar uma condição. Se a mesma for dada como verdadeira,  executa-se o comando dado, o código que está dentro dela. Existem 3 tipos, if, else e elif

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

O elif apenas é checado caso o anterior for dado como falso, porém trabalha como o mesmo
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

Se nenhuma das condições anteriores constadas em if ou elif forem satisfeitas, o else executa o comando dado em sua estrutura
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

#### exercícios 

1. Faça um programa o qual peça o valor de três números e mostre o menor deles

##### resolução:

~~~~python
def func():
	a=int (input("insira o valor de a"))
	b=int (input("insira o valor de b"))
	c=int (input("insira o valor de c"))

	if a<b and c:
		print("o menor valor é %d" %a)
	elif b<a and c:
		print ("o menor valor é %d" %b)
	else:
		print ("o menor valor é %d" %c)

func()


~~~~

2. Faça um programa que peça um número, depois mostre se ele é positivo ou negativo, caso não seja nenhuma das duas opções (seja 0), mostre a mensagem "o número digitado é (numero digitado)" (utilize else)

##### resolução:

~~~~python

def func():
	numero=int (input ("insira um numero"))

	if numero>0:
		print("o numero é positivo")
	elif numero<0:
		print("o numero é negativo")
	else:
		print("o numero digitado é %d " %numero)

func()

~~~~

3. Faça um programa que peça o número de episódios que o usuário assistiu do programa do ratinho. Se o usuário tiver assistido até 25 episódios, mostre na tela a mensagem "RAPAIZ", se assistiu até 50, mostre a mensagem "UEPAA", se assistiu mais que 50, exiba a mensagem "RATINHOO"

##### resolução:

~~~~python
def func():
	ep=int (input ("insira o numero de episodios assistidos"))

	if ep <=25:
		print("RAPAIZ")
	elif ep<=50:
		print("UEPAA")
	else:
		print("RATINHOO")

func()
~~~~

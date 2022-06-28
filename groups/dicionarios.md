# Introdução 
Dicionários são um conjunto, não-ordenado, de chave:valor. É demilitado por chaves.

# Dicionario 
Também chamado de "memoria associativa" ou vetor associativo em outras linguagens. São indexados por keys, podendo ser de tipo mutavel(strings e inteiros). É um conjunto não-ordenado de chave:valor, é delimitado por chaves, onde seus elementos são separados por virgula.

# Construção de dicionarios 
Através da funcão dict() é possivel produzir dicionarios de forma direta 
ex: 
~~~~~python
dict([('espada', 7), ('paus', 3), ('ouro', 3)]) 
dict(espada=7, paus=3) 
truco= {'espada': '7', 'paus':'3'}
~~~~~
# Iteração 
Usando o metodo items
~~~~~python
print('\n\nos pares CHAVE/VALOR são:')
for chave, valor in dicio1.items():	
	print(chave, ' = ', valor)			#mostra os pares CHAVE/VALOR
~~~~~
Usando o metodo keys
~~~~~python
print('\n\nas chaves são:')
for chave in dicio2.keys():
	print(chave)						#mostra as chaves
~~~~~~
Usando o metodo values
~~~~~python
print('\n\nos valores são:')
for valor in dicio3.values():								
	print(valor)						#mostra os valores
~~~~~~
# Operadores and, or, in, not in para dicionários 
not e or not é o operador de maior prioridade e or o de menor e or o de menor. Logo na expressão Truco and not Uno or Pife é semelhante a expressão (Truco and (not Uno)) or Pife.

~~~~~python
if 'espada' in dicio1.keys():							
	print('\n\n', dicio1['espada'])						

if 'copas' not in dicio2.keys():
	print('copas não é chave de dicio2')

if 'espada' and 'ouro' in dicio2.keys():				
	print('espada e ouro são chaves de dicio2')			

if '1' or '3' in dicio3.values():
	print('1 ou 3 são valores de dicio3')				
~~~~~~

in e not in são operadores de menor prioridade em comparação aos operadores numéricos

# Exercícios
1 - Construa um dicionário e percorra-o a procura de uma chave de valor 'ele gosta', caso não haja este valor exiba na tela cavalo:

2 - Crie um dicionário utilizando 3 cartas de um baralho espanhol, onde o naipe é o valor, e verifique se o jogador possui uma flor:

3 - Crie 2 dicionarios e faça a união e mostre na tela 



# Resolução
1.
~~~~~python
def main():
	dicio = {'reais':'0', 'espadas': '7', 'espadas': '4', 'paus': '7'}

	for valor in dicio.values():
		if 'ele gosta' in dicio.values():
			print('cavalo')

if __name__=='__main__':
	main()
~~~~~


2.  
~~~~~python
def main():

	mao = {'carta_1': 'copas', 'carta_2': 'copas', 'carta_3': 'copas'}

	contador = 0
	for valores in mao.values():
		if valores == valores:
			contador += 1  
	

	if contador == 3:
		print("FLOR")



if __name__ == '__main__':
	main()
~~~~~

3.
~~~~~python
def main():

	dicio = {'a': 1, 'b': 2}
	dicio2 = {'c': 3, 'd': 4, 'e': 5}

	dicio.update(dicio2)
	print(dicio)


if __name__ == '__main__':
	main()
~~~~~ 


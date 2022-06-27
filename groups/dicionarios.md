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

-->dicionario
também chamado de "memoria associativa" ou vetor associativo em outras linguagens. São indexados por keys, 
podendo ser de tipo mutavel(strings e inteiros). é um conjunto não-ordenado de chave:valor, é delimitado por chaves, 
onde seus elementos são separados por virgula.

-->construção de dicionarios
através da funcão dict() é possivel produzir dicionarios de forma direta
ex: dict([('espada', 7), ('paus', 3), ('ouro', 3)])
ou também 
dict(espada=7, paus=3)
ou também 
truco= {'espada': '7', 'paus':'3'}

-->iteração
usando o metodo items
truco= {'espada': '7', 'paus':'3'}
for k,v in truco.items():
	print(k,v)

-->operadores and, or, in, not in para dicionários
--not e or
not é o operador de maior prioridade e or o de menor e or o de menor.
Logo na expressão Truco and not Uno or Pife é semelhante a expressão (Truco and (not Uno)) or Pife

-- in e not in
são operadores de menor prioridade em comparação aos operadores numéricos

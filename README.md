# wikiPythonTerceirao
Wiki de Python do terceiro ano de Técnico em Informática para Internet Integrado ao Ensino Médio do Colégio Técnico Industrial de Santa Maria. Turma de 2022.

## Do terceirão pra vida!

![terceirao](images/terceirao.jpg)

# Descrição do trabalho

https://ead06.proj.ufsm.br/mod/assign/view.php?id=1649675

# Problemas resolvendo conflitos no git? 🤠

Tente este repositório: https://github.com/CTISM-Prof-Henry/gitEssentials

## Grupos & tópicos

| Grupo | Tópico |
|:------|:-------|
| Ana, Camille, Luísa | Números, expressões aritméticas, formatação de strings, comando pass |
| Karyna, Maria Eduarda Desconci, Thiaiane | Controle de fluxo: if, else, elif |
| Diogo, João Pedro, Thaylor | Laços de repetição: while, for, função range, break, continue |
| Isadora, Nicole, Maria Luiza | Estrutura de dados: listas, list comprehension, métodos da classe lista, operadores and, or, in, not in para listas |
| Bruno, Luize, Gianna | Estrutura de dados: tuplas, sets, operadores and, or, in, not in para tuplas/sets |
| Pedro, Guilherme Fensterseifer | Estrutura de dados: dicionáros, construção de dicionários, iteração sobre dicionários, operadores and, or, in, not in para dicionários |
| Liza, Aline | Funções: definindo funções, funções com parâmetros padrão, argumentos nomeados, strings de documentação |
| Gabriel, Luiz Felipe, Kamilla | Funções: parâmetros especiais, funções anônimas, listas de argumentos arbitrárias |
| Maria Eduarda Lencina, Pâmela, Patrick | Leitura e escrita de arquivos, método with, biblioteca csv, Gravando dados estruturados com json | 
| Miguel Ávila, Nicolas, Tales | Exceções |
| Davi, Guilherme Einloft, Miguel Brondani | Classes: sintaxe de definição de calsses, objetos de class, objetos instância, objetos método, variáveis de classe e instância, observações aleatórias |

## Não-atribuídos

1. Classes: herança múltipla, variáveis privadas, geradores
2. Módulos
3. Pacotes

## Exemplo de Wiki

### Sumário

1. [Introdução](#introdução)
2. [Fluxo](groups/fluxo.md)
3. [Exceções](groups/excecoes.md)
4. [Classes](groups/classes.md)
5. [Listas](groups/Listas.md)
6. [Laços de Repetição](groups/Lacos_de_repeticao.md)
7. [Funções: Parâmetros especiais, Funções anônimas e Listas de argumentos arbitrárias](groups/uncoes-parametros-lambdas-argumentos.md)

### Introdução

#### Resumo simplificado

Python é 🔝

#### Resumo expandido

Sério, Python é muito 🔝

#### Exercícios

1. Abra o console do Python.
2. Rode um programa Python pelo console.
3. Rode um script Python pelo console.

#### Resolução

1. Menu Iniciar > prompt de comando > digite `python` e dê Enter
2. Menu Iniciar > prompt de comando > digite `python` e dê Enter. Digite `print('olá mundo!')`. Feito!
3. Menu Iniciar > prompt de comando. Digite `python <nome do script>`, e dê Enter.

## [Estrutura de dados (Tuplas e sets)](groups/estruturas_de_dados_(tuplas_e_sets).md)
### If-Else

#### Resumo simplificado

É if e é else.

#### Resumo expandido

Tem mais coisa, mas não tô afim de escrever agora.

#### Exercícios

Fiquei com preguiça de fazer.

#### Resolução

Depois eu faço.

<!-- comentario apenas para dividir do resto, atenção, area restrita -->

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

<!-- comentario apenas para dividir do resto, atenção, saindo da area restrita -->

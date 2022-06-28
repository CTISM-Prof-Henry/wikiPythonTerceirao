# **Funções: parâmetros especiais, funções anônimas, listas de argumentos arbitrárias**

### Sumário

1. [Parâmetros especiais](#Parâmetros-especiais)
2. [Funções anônimas λ](#Funções-anônimas)
3. [Listas de argumentos arbitrárias](#Listas-de-argumentos-arbitrárias)
4. [Exercícios](#Exercícios)
5. [Resolução](#Resolução)

***

## **Parâmetros especiais**

#### Resumo simplificado

Os parâmetros especiais são separados em 3 tipos, sendo eles: parâmetro posicional-ou-nomeado, somente-posicional e somente-nomeado. Usamos o somente-posicional quando os nomes não são necessariamente importantes, ou quando você quer mostrar a importância da ordem. Da mesma forma que usamos somente-nomeado quando os nomes tem sim relevância na função.  


#### Resumo expandido


### Relembrando Parâmetro: 
é uma variável declarada no cabeçalho da função e tem uso exclusivo dentro do bloco de instrução da mesma. A definição dos parâmetros que uma função deve receber obriga o envio dos valores todas as vezes em que a mesma for invocada, do contrário, a função não é invocada.

### Parâmetros especiais: 
Antes de vermos o que são os parâmetros especiais, teremos de saber que os argumentos podem ser passados para uma função Python tanto por posição quanto pelo nome. Para um melhor entendimento do desenvolvedor, faz sentido restringir a maneira pelo qual argumentos possam ser passados, já que assim ele precisará apenas olhar para a definição da função para assim determinar se os itens são passados por posição, por posição e nome, ou por nome.
Para indicar se um parâmetro é posicional-ou-nomeado, somente-posicional ou somente-nomeado, usamos os símbolos (/ e *). Eles irão indicar o tipo de parâmetro pelo qual os argumentos podem ser passados para as funções. Bom lembrar que em alguns lugares, podemos ver os parâmetros nomeados recebendo o nome de parâmetros da palavra-chave.





### Parâmetros posicional-ou-nomeados:
Se os símbolos “/” e “*" por algum motivo não estiverem presentes na função, argumentos podem ser passados para uma função por posição ou por nome como antes dito.


### Parâmetros somente-posicionais:
De fato é possível definir parâmetros como somente-posicional, e apenas nesse caso, a ordem dos parâmetros importa. 
	No caso dos parâmetros somente-posicional, eles são colocados anteriormente a /. Ela é usada para identificar onde um argumento somente-posicional se inicia e termina.

### Parâmetros somente-nomeados: 
Da mesma maneira que é possível ter parâmetros como somente-posicional, também é possível ter parâmetros como somente-nomeado, que indica, obviamente, que o mesmo deve ser passado por um argumento nomeado. Igual os parâmetros somente-posicionais, aqui colocamos um símbolo antes, no caso *, que deve ser colocado antes do primeiro parâmetro somente-nomeado.




***
## **Funções anônimas** 

![LAMBDA LAMBDA LAMBDA NERDS](https://static.wikia.nocookie.net/half-life/images/9/92/Lambdaspray_2a.png/revision/latest?cb=20120621181934&path-prefix=en)

#### Resumo simplificado

Funções anônimas, também chamadas de expressões lambdas realizam quase a mesmissima função da palavra reservada **def**, ou seja, ela declara uma função, porém com algumas peculiaridades diferenciando as duas.

Mas como é a estrutura base da expressão lambda?
~~~~python
lambda a, b: a + b
(3,4)
~~~~
Em outras palavras:
**lambda**  *parâmetro1*, *parâmetro2*: expressão que a função vai executar(comparável ao return)
(valorparaa,valorparab)
#### Resumo expandido
Quando uma função **lambda** é definida, ela vai ter uso único dentro do código, diferente de **def** que pode ser chamada quantas vezes forem necessárias.
O nome Funções anônimas, vem pelo fato de que diferentemente no uso de **def** onde se deve obrigatóriamente atribuir um nome a função criada, na expressão **lambda** isso não é necessário, logo é criada uma função sem nome, vulgo anônima.


Expressão Lambda atribuida a variável func:
~~~~python
func = lambda a, b: a + b
func(10,5)
~~~~

Exemplo de um código que retorna o menor número usando **def** e **lambda** para comparação:
~~~~python
menor = lambda x, y: x if x < y else y
print(menor(10,6))
~~~~
>6 


~~~~python
def menor(x,y):
    if x < y:
        return x
    return y

print(menor(6,3))
~~~~
>3


***
## **Listas de argumentos arbitrárias**


#### Argumentos de funções em Python
A função pode funcionar sem nenhum argumento, ou seja, apenas com variáveis já definidas, ou aquelas que vão ser criadas dentro do seu escopo. Estes seriam os “argumentos posicionais”, já que os números passados para a função vão ser representados pelas variáveis na posição em que forem declaradas.

~~~~python
def sem_argumentos():
	return 1
sem_sergumentos():
~~~~
>1

Ou

~~~~python
def dois_argumentos (i, j):
	return i + j

dois_argumentos (1, 2):
~~~~
>3

#### Argumentos com valor padrão
Se um argumento quase sempre receber o mesmo valor e ele não puder ser uma variável geral, definimos ele diretamente na declaração da função.

~~~~python
def argumentos_padrao (i, j=1):
	return i + j

argumentos_padrao (7)
~~~~
>8
~~~~python
argumentos_padrao(7, 2)
~~~~
>9

Dessa forma o primeiro argumento(posicional) vai ser representado pela variável “i”, o segundo(se houver segundo) vai ser por “j”, mas se for omitido, o valor 1 vai ser atribuído a ele. Assim a função fica mais “clean” e a manutenção acaba sendo mais fácil, pois o valor é registrado em um ponto só do código.

#### Argumentos com palavra chave
Para passar argumentos com valores até para os posicionais explicitando o nome da variável e até uma ordem diferente da definida originalmente.

~~~~python
def argumentos_padrao_2(i, j=0, k=0):
	return i + j + k

argumentos_padrao_2(1, k=2, j=1)
~~~~
>4
~~~~python
argumentos_padrao_2(k=1, i=2, j=3)
~~~~
>6

Você NÃO pode utilizar dos argumentos posicionais com uma palavra chave “(j=0, k=1, 10)” e também não pode repetir um valor definido nos argumentos posicionais “(10, i=10)”.

#### Lista arbitrária de argumentos

Na Lista arbitrária de argumentos, todos os argumentos posicionais de uma função, ou apenas uma parte deles, são empacotados e entregues à função dentro de uma tupla.

~~~~python
def todos_os_argumentos(*args):

return sum(args)

todos_os_argumentos(1, 2)
~~~~
>3

~~~~python
todos_os_argumentos(1, 2, 3, 4, 5)
~~~~
>15

Ou

~~~~python
def alguns_argumentos(1, *args):

return [i * j for j in args]

alguns_argumentos(10, 1, 2, 3, 4)
	[10, 20, 30, 40]
~~~~

Podemos usar os argumentos com valores padrão, porém, eles deverão ser declarados antes do uso do “*args” e utilizados no final da chamada. (Específico da versão 3.X do Python).

~~~~python
def alguns_argumentos_com_padrao(i, j=1, *args):

return[j + i * k for k in args]

alguns_argumentos_com_padrao(10, 1, 2, 3, 4, j=2)
	[12, 22, 32, 42]
~~~~

As funções os.path.join() e printf() são ótimos exemplos de listas arbitrárias. As duas são da biblioteca padrão da linguagem.

#### Lista arbitrária de argumentos com palavra chave

Os argumentos com palavras chaves podem ser dados(todos ou alguns) dentro de um dicionário.

~~~~python
def argumentos_em_dicionario(**kwargs):
	for k, v in kwargs.items():
		print(‘{} = {}’.format(k, v))

argumentos_em_dicionario(nome=’Jorge’, idade=50, ativo=False)
~~~~
>nome = Jorge
>idade = 50
>ativo = False

#### *args:

Passa uma lista de argumentos variáveis sem palavra-chave em forma de tupla. A função que vai o receber não terá a informação de quantos argumentos serão passados

#### **kargs:

Permite passar um dicionário com inúmeras chaves para a função.

~~~~python
def alguns_argumentos_com_padrao(i, *args, j=2):
    return [j + i * k for k in args]
~~~~
~~~~python
def argumentos_em_dicionario(**kargs):
    for k, v in kargs.items():
        print('{} = {}'.format(k, v))
~~~~
***


#### **Exercícios**

1. Faça uma função que recebe 3 palavras, cada uma por um parâmetro diferente. Faça com que cada um dos parâmetros seja passado EXCLUSIVAMENTE por posição.
2. Um professor de algortimos e programação de 2019/2020 precisa passar um trabalho para seus alunos e está sem criatividade, no fim ele pensa em algo inovador. Faça uma calculadora em Python utilizando funções anônimas e com escolha de operações.
3. Faça um código em listas que mostre na tela quantos animais existem no centro de cuidados fazendo a soma deles separando-os por sexo e depois mostre na tela uma lista com o nome, qual animal é, espécie e sexo de cada um.
#### **Resolução**
1.
~~~~python
def concatena(a, b, c, /):
	print(a, b, c)

	
concatena('dragon', 'ball', 'Z')

~~~~
2.
~~~~python
alg = float(input("Digite o primeiro algarismo da operação: "))
alg2 = float(input("\nDigite o segundo algarismo da operação:"))

print("Escolha a operação que irá ser realizada: ")
print("1 = soma \n2 = subtração \n3 = divisão \n4 = multiplicação")
choice = int(input("\n"))


if choice == 1:
    soma = lambda a, b: a + b
    print(soma(alg,alg2))
elif choice == 2:
    sub = lambda a, b: a - b
    print(sub(alg, alg2))
elif choice == 3:
    div = lambda a, b: a / b
    print(div(alg, alg2))
elif choice == 4:
    mult = lambda a, b: a * b
    print(mult(alg, alg2))
else:
    print("\nPor favor escolha uma opção válida")
~~~~
3.
~~~~python
def total(*sexo):
    soma = 0

    for n in sexo:
        soma = soma + n

    print('Soma total de animais: ', soma, '\n')

total(3, 7)

def info(**lista):

    for k, v in lista.items():
        print('{} é {}'.format(k,v))

info(Nome = 'Jorge', Animal = 'Macaco', Especie = 'Primata antropoide', Sexo = 'Masculino\n')
info(Nome = 'Lilia', Animal = 'Veado', Especie = 'Ozotoceros bezoarticus', Sexo = 'Feminino\n')
info(Nome = 'Damiani', Animal = 'Urso', Especie = 'Ursidae', Sexo = 'Masculino\n')
info(Nome = 'Cadu', Animal = 'Galo', Especie = 'Gallus gallus domesticus', Sexo = 'Masculino\n')
info(Nome = 'Roach', Animal = 'Égua', Especie = 'Equus ferus', Sexo = 'Feminino\n')
info(Nome = 'Mimi', Animal = 'Leoa', Especie = 'Felidae', Sexo = 'Feminino\n')
info(Nome = 'Seboso', Animal = 'Coala', Especie = 'Phascolarctidae', Sexo = 'Masculino\n')
info(Nome = 'Bichano', Animal = 'Leão', Especie = 'Felidae', Sexo = 'Masculino\n')
info(Nome = 'Banguela', Animal = 'Cavalo', Especie = 'Equus ferus', Sexo = 'Masculino\n')
info(Nome = 'Miranha', Animal = 'Hipopótamo', Especie = 'Hippopotamidae', Sexo = 'Masculino')


~~~~

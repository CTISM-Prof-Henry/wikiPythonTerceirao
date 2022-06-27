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

>Python é 🔝

#### Resumo expandido

>Sério, Python é muito 🔝


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

#### Resumo simplificado

Python é 🔝

#### Resumo expandido

Sério, Python é muito 🔝

***


#### **Exercícios**

1. Abra o console do Python.
2. Um professor de algortimos e programação de 2019/2020 precisa passar um trabalho para seus alunos e está sem criatividade, no fim ele pensa em algo inovador. Faça uma calculadora em Python utilizando funções anônimas e com escolha de operações.
3. Rode um script Python pelo console.

#### **Resolução**
1.
~~~~python


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


~~~~

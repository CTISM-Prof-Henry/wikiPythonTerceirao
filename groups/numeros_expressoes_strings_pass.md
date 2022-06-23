# **Números e expressões aritméticas**
### Descrição simplificada:
Os dados numéricos utilizados em códigos Python podem ser: int (inteiros) e float (ponto flutuante). Esses números junto de operadores aritméticos, são capazes de realizar operações matemáticas.
 

### Descrição detalhada:
Por ser capaz de realizar diversas expressões aritméticas o interpretador Python pode ser utilizado como uma calculadora para as necessidades impostas nele. Dessa forma, é possível inserir variáveis numéricas e utilizá-las como bem entender. Esses números podem ser apresentados como: 


**int** (inteiro), exemplo: 5.0; -24.0; 37 → números **sem parte decimal ou fracionada**, com a possibilidade de ser negativo ou positivo

**float** 3.5; -45.68; 12.35 → números **com parte decimal**, com a possibilidade de ser negativo ou positivo


#### 1. Int (inteiro)
~~~python
idade = int(input('digite sua idade:')) #pede a idade do usuário
ano_nascimento = int(input('digite o ano em que nasceu:')) #pede o ano de nascimento do usuário

print('Você tem',idade, 'anos e nasceu em', ano_nascimento)
~~~
* Caso for inserido um número float no lugar de um int, aparecerá a confirmação de erro:

~~~python
ValueError: invalid literal for int() with base 10: '(número errado adicionado)'
~~~~

#### 2. Float (ponto flutuante)
~~~python
raio = float(input('Digite o valor do raio: '))

circunferencia = 2 * 3.14 * raio

print("A circuferência do círculo é:", circunferencia)
~~~

#### 3. Conversão de tipos
* Usando os comandos **float()** e **int()** é possível converter o tipo da variável numérica:
~~~python
i = 10 #int
f = 5.1 #float

i = float(i) # passando i para float
f = int(f) # passando f para int

print(i, f)
~~~~
~~~python
saída = 10.0 5
~~~~
* Nota-se que o i ganhou .0 ao final e que f não possuí mais parte decimal.

#### 4. Verificação de tipos
* Usando o comando **type()** é possível verificar qual o tipo da variável.
~~~python
i = 10 #int
f = 5.1 #float

print('o tipo da variável i é:',type(i))
#saída = <class 'int'>

print('o tipo da variável f é:',type(f))
#saída = <class 'float'>
~~~~
#### 5. Expressões aritméticas
As expressões aritméticas possuem operandos (números utilizados) e operadores, e por meio deles, realizam operações matemáticas para resolver problemas. 

##### Operadores aritméticos:

|  Operadores  | Função            | Exemplo         |
|:------------:|:------------------|:----------------|
|      +       | Soma              | 30 + 45 = 75    |
|      -       | Diferença         | 120 - 15 = 105  |
|      *       | Multiplicação     | 43 * 5 = 215    |
|      **      | Exponenciação     | 43 ** 2 = 1849  |
|      /       | Divisão           | 42 / 5 = 8.6    |
|      //      | Divisão inteira   | 42 // 5 = 8     |
|      %       | Resto de divisão  | 42 % 5 = 8      |

* Os operadores + e - servem tanto para soma e diferença quanto para demonstrar se o número é positivo ou negativo.
~~~python
a = -4 + 10
print(a)
#saída = 6

b = -4 + (-10)
print(b)
#saída = -14
~~~~

##### Exemplos:
dps eu coloco

# **Comando Pass**
### Descrição simplificada:
O comando pass é um comando nulo. Basicamente, ele não realiza nenhuma operação.



### Descrição detalhada:

#### Uso

Como este comando não resulta em nenhuma operação ou alteração, ele é usado para "pular" alguma etapa do código.

**Exemplo:**
Abaixo, temos um trecho de código incompleto:

- `entrada`
~~~~~python
1   print('Vou contar até 4, olha só: ')
2   lista = [1, 2, 4]
3   for i in lista:
4       if i == 4:
5           ##print('3')
6       print(i)
7   print('Viu?')
~~~~~
Falta acrescentar o que acontece na linha 5. Tentar rodar um código com partes incompletas, como a do exemplo acima, pode resultar em vários erros, dependendo do caso. 
- `saída`
        
        File "C:/Users/exemplo.py", line 6
        print(i)
        ^
        IndentationError: expected an indented block

        Process finished with exit code 1
    
Por isso, utilizar o comando pass neste trecho seria o indicado, para que o as outras partes do código rodem, e a parte incompleta seja "passada".

- `entrada`
~~~~~python
1   print('Vou contar até 4, olha só: ')
2   lista = [1, 2, 4]
3   for i in lista:
4       if i == 4:
5       pass
6       print(i)
7   print('Viu?')
~~~~~
- `saída`

        "C:\Users\exemplo.py"
        Vou contar até 4, olha só: 
        1
        2
        4
        Viu?

Desta forma, ainda que falte o "print('3')" na linha 5, que faria com que a saída fosse 
    
    Vou contar até 4, olha só:
    1
    2
    3
    4
    Viu?
    
ainda obtemos uma saída, sem receber nenhuma mensagem de erro devido a um trecho ainda não implementado.







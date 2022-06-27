# **Números e expressões aritméticas**
### Descrição simplificada:
Os dados numéricos utilizados em códigos Python podem ser: int (inteiro) e float (ponto flutuante). Esses números junto de operadores aritméticos, são capazes de realizar operações matemáticas.
 

### Descrição detalhada:
Por ser capaz de realizar diversas expressões aritméticas o interpretador Python pode ser utilizado como uma calculadora. Dessa forma, é possível inserir variáveis numéricas e utilizá-las como bem entender. Esses números podem ser apresentados como: 


* **int** → números **sem parte decimal ou fracionada**, com a possibilidade de ser negativo ou positivo.
  * exemplos: 5.0; -24.0; 37
* **float** → números **com parte decimal**, com a possibilidade de ser negativo ou positivo.
  * exemplos: 3.5; -45.68; 12.35

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

  print('a conversão de i é:', i)
  print('a conversão de f é:', f)
  ~~~~
  ```
  a conversão de i é: 10.0
  a conversão de f é: 5

  Process finished with exit code 0
  ```
* Nota-se que o i ganhou .0 ao final e que f não possuí mais parte decimal.

#### 4. Verificação de tipos
* Usando o comando **type()** é possível verificar qual o tipo da variável.
  ~~~python
  i = 10 #int
  f = 5.1 #float
  
  print('o tipo da variável i é:',type(i))
  print('o tipo da variável f é:',type(f))
  ~~~~
  ```
  o tipo da variável i é: <class 'int'>
  o tipo da variável f é: <class 'float'>
  
  Process finished with exit code 0
  ```


#### 5. Expressões aritméticas
As expressões aritméticas possuem operandos (números utilizados) e operadores, e com eles realizam operações matemáticas para resolver problemas. 

**Operadores aritméticos:**

|  Operadores  | Função           | Exemplo        |
|:------------:|:-----------------|:---------------|
|      +       | Soma             | 30 + 45 = 75   |
|      -       | Diferença        | 120 - 15 = 105 |
|      *       | Multiplicação    | 43 * 5 = 215   |
|      **      | Potenciação      | 43 ** 2 = 1849 |
|      /       | Divisão          | 42 / 5 = 8.6   |
|      //      | Divisão inteira  | 42 // 5 = 8    |
|      %       | Resto de divisão | 42 % 5 = 3     |

Os operadores + e - servem tanto para soma e diferença, quanto para demonstrar se o número é positivo ou negativo.
  ~~~python
  a = -4 + 10
  print('a será:', a)
  
  b = -4 + (-10)
  print('b será:', b)
  ~~~~
  ```
  a será: 6
  b será: -14
  Process finished with exit code 0
  ```
#### Exemplos simples de uso:
1. Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor
    ~~~python
    num = int(input('digite um número:'))
    print('analisando o número', num, 'o número sucessor é', (num+1), 'e o antecessor é', (num-1))
    ~~~~
    ```
    digite um número:10
    analisando o número 10 o número sucessor é 11 e o antecessor é 9
    
    Process finished with exit code 0
     ```
2. Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
    ~~~python
    num = int(input('digite um número:'))
    print('o dobro do número é:', (num * 2), 'o triplo é:', (num * 3), 'e a raiz quadrada é:', (num ** 0.5))
    ~~~~~
    ```
    digite um número:25
    o dobro do número é: 50 o triplo é: 75 e a raiz quadrada é: 5.0
    
    Process finished with exit code 0
    ```
# **Formatação de Strigs**
### Descrição simplificada:
A formatação de strings é utilizada para organizar a maneira como os dados serão exibidos na saída.

### Descrição detalhada:
Às vezes, ao final de um código em que são usadas strings, desejamos visualizar a saída de dados contendo uma certa organização, buscando suprir o interesse final do algoritmo.
Com python, há 3 formas de formatar strings:

#### 1. Metódo format()

* Com argumentos numerados:
~~~python
>>> print('{0} e {1}'.format('dor', 'horror'))
dor e horror
~~~~

* Com argumentos nomeados
~~~python
>>>print('Nós, da {turma}, adoramos o {docente}!'.format(turma='433', docente='sor Henry'))
Nós, da 433, adoramos o sor Henry!
~~~

* Argumentos numerados e nomeados juntos
~~~python
>>> print('{0}, {1} e {other}'.format('Gestão', 'Redes', other='DSPI'))
Gestão, Redes e DSPI
~~~

* Com o uso de dicionários usando a notação **
~~~python
tabela = {'terceiro': 433, 'segundo': 423, 'primeiro': 413}
>>> print('Primeiro ano: {primeiro:d}; Segundo ano: {segundo:d}; Terceiro ano: {terceiro:d}'.format(**tabela))
Primeiro ano: 413; Segundo ano: 423; Terceiro ano: 433
~~~

#### 2. Formatação manual
~~~python
codigocodigocodigo
~~~

#### 3. Formatação de strings à moda antiga
~~~python
codigocodigocodigo
~~~

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

Desta forma, ainda que falte o "print('3')" na linha 5, que faria com que a saída fosse: 
    
    Vou contar até 4, olha só:
    1
    2
    3
    4
    Viu?
    
Ainda obtemos uma saída, sem receber nenhuma mensagem de erro devido a um trecho ainda não implementado.



#Exercícios:
1. (sobre números)
2. (sobre strings)
3. (sobre pass)



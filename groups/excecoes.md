## Exceções

### Resumo simplificado

Exceção ocorre quando algum erro, esperado ou não, ocorre, então ele é tratado. Esta prática é boa para evitar as temidas mensagens de erro genéricas.
Sua estrutura genérica é:<br>
~~~python
try:
    print("estamos tentando")
except:
    print("não deu, estamos tratando")
~~~

Exceções podem ser expecificadas (erro de sintaxe, valor, divisão por zero, etc...).<br>
O else serve para quando não entramos na exceção.<br>
O finally é excecutado sempre, independente se entramos na exceção ou não.<br>
Suas estruturas são:<br>
~~~python
try:
    numero1 = int(input("Digite um numero inteiro: "))
    numero2 = int(input("Digite outro numero inteiro: "))
    resultado_divisão = numero1/numero2
except ValueError:
    print("Valor do numero não é inteiro.")
except ZeroDivisionError:
    print("Divisão por zero é terminantemente contra as leis, os matemáticos vão te pegar na saída.")
else:
    print("Passou")
finally:
	print("Chegamos ao fim, volte mais tarde ou execute novamente o código")
~~~

Encadeamento de exceções serve para "criar" uma exceção de algum tipo, é bom para regras de negocio em que o caso não seria um erro mas, por fatores externos, se torna.
Sua estrutura é:<br>
~~~python
def retornaErroDeValor():
    raise ValueError
def retornaErroDeNome():
    raise NameError

try:
    retornaErroDeNome()
except NameError:
    print("Erro de nome")
except ValueError:
    print("Erro de valor")
~~~

### Resumo expandido

Depois eu faço.

### Exercícios

1. Crie um algoritmo para um banco, o mesmo só deve aceitar saques de números inteiros, mostre uma exceção para caso seja inserido um número decimal.

2. Como tentativa para tentar diminuir a inflação, foram cortadas de circulação as notas de R$2,00, R$20,00 e R$100,00. Crie um algoritmo para um banco, o mesmo só deve aceitar saques de npumeros inteiros, mostre uma exceção para caso seja inserido um número decimal. Mostre outra exceção para caso o usuário não insira um valor que se encaixe dentro das notas disponíveis (RS5,00, R$10,00 e R$50,00)

3. Crie um algoritmo para uma loja de tintas, o mesmo deve conter um dicionário, que tenha como chaves as seguintes cores: azul, amarelo, verde e vermelho e como valores os respectivos tons para cada cor: 6 tons, 3 tons, 4 tons e 3 tons. Mostre uma exceção para caso o usuário solicite uma cor que não esteja dentre as disponíveis e outra para caso seja pedido um tom diferente dos possíveis na cor em específico.

### Resolução

Depois eu faço.
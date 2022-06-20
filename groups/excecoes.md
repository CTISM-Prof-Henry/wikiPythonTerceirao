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

Depois eu faço.

### Resolução

Depois eu faço.
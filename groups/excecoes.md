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

2. Como tentativa para tentar diminuir a inflação, foram cortadas de circulação as notas de R$2,00, R$20,00 e R$100,00. Crie um algoritmo para um banco, o mesmo só deve aceitar saques de numeros inteiros, mostre uma exceção para caso seja inserido um número decimal. Mostre outra exceção para caso o usuário não insira um valor que se encaixe dentro das notas disponíveis (RS5,00, R$10,00 e R$50,00)

3. Crie um algoritmo para uma loja de tintas, o mesmo deve conter um dicionário, que tenha como chaves as seguintes cores: azul, amarelo, verde e vermelho e como valores os respectivos tons para cada cor: 6 tons, 3 tons, 4 tons e 3 tons. Mostre uma exceção para caso o usuário solicite uma cor que não esteja dentre as disponíveis e outra para caso seja pedido um tom diferente dos possíveis na cor em específico.

### Resolução

1.
~~~python
valor = input("Digite um número inteiro para ser sacado: ")
try:
    float(valor)
    try:
        int(valor)
    except ValueError:
        print("O número digitado deve ser inteiro")
    else:
        print("Obrigado, valor será sacado")
except ValueError:
    print("Digite um número da proxima vez...")
~~~
2.
~~~python
try:
    valor = int(input("Digite um número inteiro para ser sacado: "))
    if valor!=5 and valor!=10 and valor!=50:
        raise ConnectionRefusedError
except ValueError:
    print("O valor digitado deve ser um número inteiro")
except ConnectionRefusedError:
    print("O número digitado deve estar dentro das notas permitidas, 5, 10 ou 50")
else:
    print("Obrigado, valor será sacado")
~~~
3.
~~~python
estoqueCores = {
    "azul" : ['1','2','3','4','5','6'],
    "amarelo" : ['1','2','3'],
    "verde" : ['1','2','3','4'],
    "vermelho" : ['1','2','3'],
}
try:
    corSolicitada = str(input("Temos azul, amarelo, verde e vermelho no estoque\nDigite a cor desejada: "))
    if corSolicitada not in estoqueCores.keys():
        raise KeyError

    tomSolicitado = str(input("Esta cor possui os tons: %s \nDigite o tom desejado: " %estoqueCores[corSolicitada]))
    if tomSolicitado not in estoqueCores[corSolicitada]:
        raise NameError
        
except KeyError:
    print("a cor solicitada não está no estoque")
except NameError:
    print("o tom solicitado não está no estoque")
else:
    print("Obrigado, excelente escolha")
~~~
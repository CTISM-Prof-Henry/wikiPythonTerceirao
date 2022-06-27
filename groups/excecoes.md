## Exceções

### Resumo simplificado

Na hora da execução do programa, mesmo com ele estando sintaticamente correto, podem ocorrer erros de vários tipos e por diversos motivos. Esses erros são chamados de Exceções e eles não são necessariamente fatais, podendo ser tratados.<br>
O tratamento de exceções é muito importante por dois principais motivos: para evitar as temidas mensagens de erro genéricas e para terminar de rodar o programa em certos casos, mesmo após ocorrer um erro.

### Resumo expandido
Os comandos mais importantes para o tratamento de exceções são: `"Raise"`, `"Try"` e `"Except"`.<br>

Com o comando `"Raise"` é possível forçar uma exceção e deixar uma mensagem de erro personalizada para o usuário, facilitando o entendimento de onde ocorreu o erro e qual foi o tipo do erro.<br>

A estrutura para lançar uma Exceção é:<br>

~~~python
raise TipoExceção("Mensagem de Erro")
~~~

Já para capturar e tratar exceções, utilizamos os comandos `"Try"` e `"Except"` em conjunto, onde o "Try" tenta fazer algo e caso ocorra alguma exceção, ao invés de o programa fechar, o "Except" trata ela e diz o que fazer.<br>

A estrutura genérica para capturar Exceções é:<br>
~~~python
try:
    print("Estamos tentando...")
except:
    print("Ocorreu uma exceção, estamos tratando...")
~~~

Há outros comandos bastante usados também como o `Else` e o `Finally`.<br>
O "Else" é utilizado para quando o código não entra em nenhuma exceção, ele faz algo.<br>
O "Finally" é utilizado para rodar uma instrução não importa se o código entrou em uma exceção ou não.<br>

O melhor possível seria ter tratamentos personalizados para cada tipo de exceção. Segue um 
exemplo do uso de exceções utilizado na aula do ano passado:<br>

~~~python
def eh_melao(fruta: str) -> None:   #Cria uma função que recebe uma String de parâmetro

    if not isintance(fruta, str):   #Se o parâmetro não for String
        raise TypeError('Essa função só aceita strings!')   #Da uma exceção do tipo TypeError
    if not fruta == 'melão':    #Se o parâmetro for diferente de 'melão'
        raise ValueError('Não é melão!')    #Da uma exceção do tipo ValueError
    else:   #Se passar dos 'IFs' acima
        print('É melão!')   #É melão!!!

def main():

    try:
        eh_melao(2) #Tenta chamar a função eh_melao com o parâmetro 2
    except ValueError as ve:    #Se ocorrer uma Exceção de ValueError
        print("Ocorreu uma exceção do tipo ValueError") #Acontece isso
    except TypeError as te:     #Se ocorrer uma Exceção de ValueError
        print("Ocorreu uma exceção do tipo TypeError")  #Acontece isso
    except Exception as e:      #Se ocorrer outra Exceção qualquer
        print("Ocorreu algum erro!")    #Acontece isso
    finally:    #Independente se ocorre exceção ou não
        print("Terminei de rodar!") #Roda esse instrução

~~~

A linguagem Python por padrão já possui várias Exceções embutidas na Classe Exception. As principais são: <br>
- TypeError: essa exceção é lançada quando uma função é recebe a um objeto que é de um tipo não apropriado.
- ValueError: essa exceção é lançada quando uma função recebe o argumento com o tipo certo, mas o valor não adequado.
- ZeroDivisionError: essa exceção é lançada quando tenta dividir algum número por zero.
- NameError: essa exceção é lançada quando um nome não existe. Exemplo uma variável não definida


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
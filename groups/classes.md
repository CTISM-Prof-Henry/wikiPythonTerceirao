
## Classes
tales humilde

### Resumo simplificado

Exceção ocorre quando algum erro possivelmente esperado ocorre, então ele é tratado e retorna o seu problema, seja erro de valor, tipo, nome, etc... Ou até faz alguma outra coisa.

Sua estrutura é: <br>
~~~python
try:
    print("estamos tentando")
except:
    print("não deu, estamos tratando")
~~~

### Resumo expandido

Depois eu faço.

## Objetos de Instância

### Resumo simplificado:
Um objeto de instância surge quando uma classe é instanciada. Esses objetos de instância apenas compreendem a operação de referência de atributos.

### Resumo expandido:
Existem dois tipos de atributos: atributos de dados e métodos. Atributos de dados são como variáveis locais, que podem ser declaradas ou podem existir a partir da primeira vez em que é feita uma atribuição. 
Suponhamos que um objeto `x` de uma classe qualquer precise de um atributo de dados chamado `contador`, porém esse atributo não foi declarado ainda. Podemos declará-lo e atribuir automaticamente um valor a ele, como no exemplo a seguir.
~~~python
x.contador = 0
~~~
A partir de agora o atributo `contador` existe dentro do objeto `x`, mesmo que esse atributo não tenha sido declarado em sua classe.
Outro tipo de atributos de instância é um método, que falaremos sobre no próximo tópico.

## Métodos e Objetos Método

### Resumo simplificado:
Métodos são funções que "pertencem" a um objeto. Esses métodos são definidos dentro de uma classe e são referenciados e chamados por meio de um objeto de instância.

### Resumo expandido:
Métodos podem ser invocados logo após serem referenciados. Utilizaremos como exemplo o método `f`.
~~~python
def f(self):
    return 'Olá Mundo!'
~~~
Para referenciá-lo utlizamos `x.f`.
Normalmente métodos são invocados logo após serem referenciados. Se digitarmos print(x.f()), será exibida a string `'Olá Mundo!'`.
Porém, como `x.f` também é um objeto, ele pode ser armazenado e invocado posteriormente. Por exemplo:
~~~python
xf = x.f
print(xf())
~~~
exibirá `Olá Mundo!` na tela.

## Variáveis de classe e instância

### Resumo Simplificado
* Variável de Classe: 
Variável comum para todas as instâncias da classe.
Recomendado ser dados imutáveis

* Variável de Instância:
Variável específica para cada objeto da classe.

### Resumo Expandido

~~~python
class brasileiro():
	origem = 'Brasil' # Variável comum a todos os objetos da classe
	def __init__(proprio, estadoOrigem=str(), nome=str(), cpf=int()):
		proprio.nome = nome # Variável específica de um objeto
		proprio.estado = estadoOrigem # Variável específica de um objeto
		proprio.cpf = cpf # Variável específica de um objeto

pessoa1 = brasileiro('RS', 'Henry', 86960099080)

print(pessoa1.estado) # Variável "estado" do objeto pessoa1
print(pessoa1.nome) # Variável "nome" do objeto pessoa1
print(pessoa1.cpf) # Variável "cpf" do objeto pessoa1
print(pessoa1.origem) # Váriavel "origem" da classe "brasileiro"e
~~~

## Exercícios

1. Crie uma classe qualquer com pelo menos um método, instancie essa classe e imprima o retorno desse método através da instância.

## Resolução

1.
~~~python
def Classe:
    def retorna_oi(self):
        return "oi"
x = Classe()
print(x.retorna_oi)
~~~

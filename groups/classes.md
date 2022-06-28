# Classes

## Sintaxe de Definição de Classes

### Resumo Simplificado:
Tem basicamente como função dar o nome às variáveis da classe, isso será explicado com mais precisão na parte de métodos.


### Resumo Expandido:
Quando a definição de classes começa, é criado um espaço de nomes, onde são atribuídas as variáveis locais. 
Quando tudo ocorre normalmente, o objeto classe é criado.
~~~python
class Atleta:
	

~~~

## Objetos de Classe

### Resumo Simplificado:
Duas operações: referências a atributos e instanciação.

*Referências a atributos:* Define o resultado à variável local.

*Instanciação*: Gera um objeto vazio, classe pode determinar um método importante, o __init__.

### Resumo Expandido:
~~~python
class Atleta:

	def __init__(proprio, nome='Jean Pyerre', time='Avaí'):
	  proprio.nome = nome

	def get_nome(proprio) :
	  return proprio.nome

~~~

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
Para referenciá-lo utilizamos `x.f`.
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

No exemplo a seguir, definimos uma classe <i>brasileiro</i>. Como Variável de Classe  (comum a todos os objetos da classe) temos a variável <i>origem</i>. Desta forma, independente do objeto criado, a variável sempre será 'Brasil' .

Dentro do construtor da classe há as Variáveis de Instância: <i>nome, estado,</i> e <i>cpf</i>. Elas não são constantes entre os Objetos. Assim, os diferentes Objetos possuem Variáveis com o mesmo nome, entretanto seus valores não são obrigatoriamente iguais. No código de demonstração, temos que pessoa1 possui <i>estadoOrigem</i> = "RS" e <i>nome</i> = "Henry", enquanto que pessoa2 tem <i>estadoOrigem</i> = "SP" e <i>nome</i> = "Ayrton Senna". 

Note que a diferença na definição entre uma variável de Instância e Classe está na forma como são declaradas. Na primeira , é necessário fazer referência ao próprio Objeto <i>(self)</i>, e a segunda é definida antes do construtor, sem referência.

~~~python
class brasileiro():
	origem = 'Brasil'
	def __init__(self, estadoOrigem=str(), nome=str(), cpf=int()):
		self.nome = nome
		self.estado = estadoOrigem
		self.cpf = cpf

pessoa1 = brasileiro('RS', 'Henry', 86960099080)
pessoa2 = brasileiro('SP', 'Ayrton Senna', 49539261880)
~~~

## Observações Aleatórias
### Resumo Simplificado
Diferentes informações adicionais sobre classes e suas sintaxes.
* <i>self</i> não é uma palavra reservada
*  Entre variáveis de Classe e Instância com o mesmo nome, a prioridade será da Instância.

### Resumo Expandido

* O  primeiro parâmetro, utilizado para referenciar o próprio objeto, é por convenção chamado de <i>self</i>. Entretanto, qualquer outro nome de variável funciona da mesma forma.
~~~python
class tuberculo():
	def __init__(planta, nome=str()):
		planta.nome = nome
		
h1 = tuberculo(nome='batata')
~~~
* Variáveis de Classe e Instância com o mesmo nome são possíveis de ocorrer na mesma classe, entretanto apenas o valor da variável de instância será retornada. No código abaixo, o humano sobrepõe <i>origem</i> = america por <i>brasil</i>. Outros Objetos continuam tendo <i>origem</i> = america.
~~~python
class pessoa:
		origem = "america"

humano = pessoa()
humano.origem = "brasil"
~~~
## Exercícios

1. Crie uma classe qualquer com pelo menos um método, instancie essa classe e imprima o retorno desse método através da instância.

2. Considerando o código abaixo, assinale o que será IMPRESSO na tela?

~~~python
class ClasseTeste:
    """Classe Qualquer"""
    i = 561237

    def funcao(self):
        return 'Hello World'
~~~

<pre>
A) 561237
B) Hello World
C) self
D) Nada
E) Classe Qualquer
</pre>

3. Considerando os dois códigos abaixo, qual imprimirá na tela o nome de uma música famosa? Qual é ela? 
~~~python
#Código 1
class musica:
	def __init__(self, nome=str(), lancamento=int()):
	    self.nome = nome
	    self.lancamento = lancamento

smells_like_teen_spirit = musica("Smells Like Teen Spirit", 1991)

eh_o_amor = smells_like_teen_spirit
eh_o_amor.nome = "É o Amor"

print(eh_o_amor.nome)
~~~

~~~python
#Código 2
class musica:
    nome="Na Boquinha da Garrafa"
    def __init__(self, nome=str(), lancamento=int()):
	    self.nome = nome
	    self.lancamento = lancamento

good_for_you = musica(lancamento=2021)

smells_like_teen_spirit = good_for_you

print(good_for_you.nome)
~~~

## Resolução

1.
~~~python
def Classe:
    def retorna_oi(self):
        return "oi"
x = Classe()
print(x.retorna_oi)
~~~

2. D
3. Código 1 mostrará na tela a música É o Amor. Código 2 irá priorizar o valor da Variável de Instância <i>nome</i>, mas como não foi definida, não mostrará nada na tela.

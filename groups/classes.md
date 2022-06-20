
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

## Resolução

# Leitura e Escrita de Arquivos

Um algoritmo consiste em três partes: (i) uma entrada, (ii) uma sequência de instruções (passos), e (iii) uma saída.
Enquanto a entrada e a saída podem ser opcionais, a sequência de instruções é sempre obrigatória.

A entrada em um programa pode se dar de diversas formas: escrita em um teclado, entrada de dados pela rede de 
computadores (Internet), mouse, etc. Da mesma maneira, a saída pode ser para a tela de um computador, para a rede de
computadores, ou então para um arquivo, salvo no disco local do computador.

Nesta página serão cobertos os métodos de entrada e saída para arquivos salvos no disco.  

## Sumário

* [Manipulação de arquivos](#manipulação-de-arquivos)
* [Lendo dados](#lendo-dados)
* [Mostrando dados](#mostrando-dados)
* [Convertendo texto em números](#convertendo-texto-em-números)
  * [Outros métodos de leitura de dados](#outros-métodos-de-leitura-de-dados)
* [Método with](#método-with)

## Manipulação de arquivos

Para abrir um arquivo em Python usamos a função `open()`, que recebe dois parâmetros (ou seja, dois valores): 
* o nome do arquivo a ser aberto; e 
* o que queremos fazer com este arquivo, seja escrever (`w`) ou ler (`r`)

### Lendo dados

Para ler dados digitados pelo teclado, utilizamos a função nativa `input`:

```python
filme = input("Digite qual seu filme favorito da Disney: ")
```

### Mostrando dados 

Como mostramos informações na tela, usando Python? Usamos a função nativa `print`:

Exemplo:

```python
filme = "Frozen"
print("Meu filme favorito da Disney é", filme)
```
 
Juntando os dois exemplos:

```python
filme = input("Digite qual seu filme favorito da Disney: ")
print("Meu filme favorito da Disney é", filme)
```

A saída do código acima será

````
Digite qual seu filme favorito da Disney: Frozen
Meu filme favorito da Disney é Frozen
````

### Convertendo texto em números

A função `input` aceita strings como entrada. Caso queira-se converter esta string em um número, é preciso usar uma 
função de _cast_:

```python
numero_texto = input("digite um número: ")
numero_numero = int(numero_texto)
print(type(numero_texto), type(numero_numero), type(float(numero_texto)))
```

### Outros métodos de leitura de dados

Outra função de leitura de dados é o `readline`.

Se caso quer ler dois números inteiros ou arredondados, como por exemplo `90` e `65`, escrevemos o seguinte código:

```python
import sys

peso, idade = map(int, sys.stdin.readline().split())
```

Tornando cada elemento lido para int.

## Método with

O método `with` é usado na leitura de dados e garante a finalização de recursos como fechar corretamente um arquivo após 
sua utilização.

Pense no método `with` como retirar um pendrive antes do computador terminar de escrever dados nele; muito provavelmente
os dados ficarão corrompidos. O método `with` evita que isto aconteça.

Para ler um arquivo com método `with`, escrevemos o seguinte código:

 ```python
with open('workfile.txt', 'r') as f:
    read_data = f.read()
```

Que é equivalente ao seguinte código, que **não usa** o método `with`:

```python
f = open('workfile.txt', 'r')
read_data = f.read()
f.close()
```

Podemos verificar se o arquivo f já foi fechado com o atributo `closed`:

```python
f = open('workfile.txt', 'r')
read_data = f.read()
print(read_data)
print('O arquivo f foi fechado já?', f.closed)
f.close()
print('O arquivo f foi fechado já?', f.closed)
```

A saída deste segundo código na tela será

```
olá mundo!
O arquivo f foi fechado já? False
O arquivo f foi fechado já? True
```

**Nota:** Caso não utilize o método `with`, devemos utilizar o método `close` para efetuar a finalização correta.

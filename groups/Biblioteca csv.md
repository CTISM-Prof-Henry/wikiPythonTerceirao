# <center>Biblioteca CSV</center>

## Os arquivos csv sempre estarão em um formato de (tabela), nunca serão em formato de um texto.

### Ex: Formato Tabela

<center>![myImage](https://media.giphy.com/media/lPoxtQlcX30doRbHTN/giphy.gif)</center>

### Ex: Formato Texto

<center>![myImage](https://media.giphy.com/media/lPoxtQlcX30doRbHTN/giphy.gif)</center>

# Importante

## import csv -> Utilizado para importar a biblioteca csv


## Criando um arquivo csv:

Um arquivo de colunas, as colunas normalmente são separadas por " , ". Geralmente sendo a primeira linha definindo as colunas, que será chamado de cabeçalho.

```python
import csv
# Abrir/criar o arquivo(teste.csv)
with open('./teste.csv, 'w') as csvfile:
# Cria a primeira linha, separando as colonas por "," '''
    csv.writer(csvfile, delimiter=',').writerow(['João', '30' ])
    csv.writer(csvfile, delimiter=',').writerow(['José', '27'])
    csv.writer(csvfile, delimiter=',').writerow(['Pedro', '20'])
```
podendo criar no excel:
<center> ![Explicaçãolerumarquivocsv](Link img)</center>

## Lendo um arquivo csv:

 * open('Arquivo.csv', newline='') -> Função usada para abrir um arquivo

* csv.reader -> Utilizado para ler um arquivo csv (irá ler todas as linhas do arquivo)

### Esse código irá retornar as linhas do arquivo como estão:

```python
# Importa a biblioteca csv 
import csv
# Abre o arquivo(nomeaquivo.csv)
arquivo = open('nomearquivo.csv')
# lê as linhas do arquivo
linhas = csv.reader(arquivo)
# for para retornar as linhas
for linha in linhas:
    print(linha)
```

### Esse código irá retornar os parâmetros chamados no print:

~~~~python
import csv

arquivo = open('pessoas.csv')

pessoas = csv.DictReader(arquivo)

for pessoa in pessoas:
    print("Nome:", pessoa["nome"], " - Idade:", pessoa["idade"], " - Email:", pessoa["email"])
~~~~

#### Obs: Podemos abrir um arquivo dando um modo, quando usará especificamente para ler ou modificar. 
* open('file.csv', mode='r')

Caractere | Significado
-------------------------------
: 'r':           |  abre para leitura (padrão)
:'w':           | abre para escrita, removendo tudo que está no mesmo

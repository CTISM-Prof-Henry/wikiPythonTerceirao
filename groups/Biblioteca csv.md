# Biblioteca CSV

Os arquivos csv sempre estarão em um formato de (tabela), nunca serão em formato de um texto.

## Ex: Formato Tabela

### Arquivo Raiz
![csvraiz](https://github.com/CTISM-Prof-Henry/wikiPythonTerceirao/blob/main/images/Arquivo%20csv%20raiz.png)
### Arquivo Nutela
![csvnutela](https://github.com/CTISM-Prof-Henry/wikiPythonTerceirao/blob/main/images/Arquivo%20csv%20nutela.png)

### Ex: Formato Texto

![Formatotexto](https://github.com/CTISM-Prof-Henry/wikiPythonTerceirao/blob/main/images/Aquivo%20texto.png)


# import csv -> Utilizado para importar a biblioteca csv

# Criando um arquivo csv:

Um arquivo de colunas, as colunas normalmente são separadas por " , ". Geralmente sendo a primeira linha definindo as colunas, que será chamado de cabeçalho.

```python
import csv

# Abrir/criar o arquivo(teste.csv)
with open('./arquivo.csv', 'w') as arquivocsv:

# Criando as linhas, separando as colonas por "," '''
	csv.writer(arquivocsv, delimiter=',').writerow(['Ricardinho', 'Bom'])
	csv.writer(arquivocsv, delimiter=',').writerow(['Felipe', 'Bom'])
	csv.writer(arquivocsv, delimiter=',').writerow(['Henry', 'Bom'])
	csv.writer(arquivocsv, delimiter=',').writerow(['Guilherme', 'Ruim'])
```
podendo criar no excel:
<center> ![Explicaçãolerumarquivocsv](Link img)</center>

# Lendo um arquivo csv:

 * open('Arquivo.csv', newline='') -> Função usada para abrir um arquivo

* csv.reader -> Utilizado para ler um arquivo csv (irá ler todas as linhas do arquivo)

## Esse código irá retornar as linhas do arquivo como estão:

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

# Abrirá "arquivo.csv" com modo de leitura
with open('./arquivo.csv', 'r') as arquivocsv:
#for para ler as linhas
	for linhas in csv.reader(arquivocsv):
		# printa as linhas
		print(linhas)
```

## Esse código irá retornar os parâmetros chamados no print:

```python
import csv

arquivo = open('pessoas.csv')

pessoas = csv.DictReader(arquivo)

for pessoa in pessoas:
    print("Nome:", pessoa["nome"], " - Idade:", pessoa["idade"], " - Email:", pessoa["email"])
```

### Obs: Podemos abrir um arquivo dando um modo, quando usará especificamente para ler ou modificar. 
* open('file.csv', mode='r')

Caractere | Significado
----------|----------------------------
'r'       |  abre para leitura (padrão)
'w'       | abre para escrita, removendo tudo que está no mesmo


# Questão

~~~~ python
import csv

with open('./arquivo.csv', 'w') as arquivocsv:
	csv.writer(arquivocsv, delimiter=',').writerow(['Ricardinho', 'Bom'])
	csv.writer(arquivocsv, delimiter=',').writerow(['Felipe', 'Bom'])
	csv.writer(arquivocsv, delimiter=',').writerow(['Henry', 'Bom'])
	csv.writer(arquivocsv, delimiter=',').writerow(['Guilherme', 'Ruim'])


with open('./arquivo.csv', 'r') as arquivocsv:
	for linhas in csv.reader(arquivocsv):
		print(linhas)
~~~~

## Quantas linhas terá "arquivo.csv" e quantas linhas retornarão?

A) 4, 4
B) 4, 2
C) 4, 0
D) 0, 0

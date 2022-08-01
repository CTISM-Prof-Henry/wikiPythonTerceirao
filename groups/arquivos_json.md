# Arquivos JSON

JSON (JavaScript Object Notation) é um formato de arquivo, independente da linguagem de programação - apesar de levar
_Javascript_ no nome.

Arquivos JSON tem a sintaxe muito parecida com dicionários em Python:

```json
{
  "nome": "henry",
  "altura": 1.83,
  "beleza": "máxima"
}
```

Neste exemplo, as palavras `nome`, `altura` e `beleza` são as **chaves**, enquanto `henry`, `1.83` e `máxima` são os
**valores**.

## Sumário

* [Escrevendo arquivos JSON](#escrevendo-arquivos-json)
* [Lendo arquivos JSON](#lendo-arquivos-json)
* [Listas em JSON](#listas-em-json)
* [Exercícios](#exercícios)

## Escrevendo arquivos JSON

Supomos que queremos escrever os seguintes dados em um arquivo de nome `henry.json`:

```json
{
  "nome": "henry",
  "altura": 1.83,
  "beleza": "máxima"
}
```

Podemos escrever estes dados em um arquivo utilizando o seguinte código Python:

```python
import json

dicionario = {
  "nome": "henry",
  "altura": 1.83,
  "beleza": "máxima"
}

with open('henry.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dicionario, arquivo, indent=2)
```

O método `dump` escreve um dicionário em um arquivo, que precisa ser aberto previamente. No exemplo acima, utilizamos
o método `with`, mas podemos fazer sem este método também (apesar de não ser recomendado):

```python
import json

dicionario = {
  "nome": "henry",
  "altura": 1.83,
  "beleza": "máxima"
}

arquivo = open('henry.json', 'w', encoding='utf-8')
json.dump(dicionario, arquivo)
arquivo.close()
```

## Lendo arquivos JSON

Para ler o conteúdo do arquivo `henry.json`, utilizamos o seguinte código-fonte:

```python
import json

with open('henry.json', 'r') as arquivo:
    dicionario = json.load(arquivo)
    print(dicionario)
```

Que imprimirá na tela

```
{'nome': 'henry', 'altura': 1.83, 'beleza': 'máxima'}
```

## Listas em JSON

Para fazer uma lista de objetos em JSON, basta delimitar os itens por colchetes:

```json
[
  {
      "nome": "henry",
      "altura": 1.83,
      "beleza": "máxima"
  },
  {
      "nome": "jorge",
      "altura": 1.60,
      "beleza": "mínima"
  }
]
```

Ao ler este arquivo com `json.load`, o objeto retornado será uma **lista de dicionários**, ao contrário de um 
**dicionário.**

## Exercícios

No Rio Grande Do Sul, a empresa SEG (Sistema de Ensino Gaúcho) quer correlacionar quanto cada aluno deverá pagar por 
um curso, pois, devido ao grande número de pessoas querendo se matricular no curso de Técnico de Enfermagem, a 
funcionária Cláudia se confundiu com os valores de desconto e perdeu a lista com o total de participantes, gerando uma 
confusão. Faça uma lista de objetos em JSON com os valores que cada aluno pagará pelo curso. Não erre, como 
Cláudia!

Alunos:

```
  Luana = 349,50
  Pedro = 299,00
  Joana = 199,00
Gabriel = 299,00
   João = 300,00
  Júlia = 200,00
```

Resolução:

```python	

import json
	
list = "{
	"Alunos de  enfermagem": 6, 
	"Luana": 349.50, 
	"Pedro": 299.00, 
	"Joana": 199.00, 
	"Gabriel" : 299.00,
	"João": 300.00, 
	"Júlia": 200.00
}"
	
print(list)
```	
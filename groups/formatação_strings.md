# Formatação de Strings

A formatação de strings é utilizada para organizar a maneira como os dados serão 
exibidos na saída.

Às vezes, ao final de um código em que são usadas strings, desejamos visualizar 
a saída de dados contendo uma certa organização, buscando suprir o interesse 
final do algoritmo.

Com python, há 3 formas de formatar strings, que aqui serão mostradas **duas**
formas.

## Metódo format

### Uso básico

```python
print('Sou aluno da {} {}'.format('turma', '433'))
```

Saída:

```
Sou aluno da turma 433
```
  
As chaves vazias são substituídas pelos objetos referenciados no método 
`format()`.


### Com argumentos numerados

```python
print('{0} e {1}'.format('dor', 'horror'))
```

Saída:
```
dor e horror
```

Os objetos presentes no método format podem ser referenciados por números, 
tendo suas posições numeradas.

### Com argumentos nomeados

```python
print(
    'Nós, da {turma}, adoramos o {docente}!'.format(
        turma='433', docente='sor Henry'
    )
)
```

Saída:

```
Nós, da 433, adoramos o sor Henry!
```
  
### Com o uso de dicionários usando a notação

```python
tabela = {'terceiro': 433, 'segundo': 423, 'primeiro': 413}
print(
    'Primeiro ano: {primeiro:d}; Segundo ano: {segundo:d}; ' + \
    'Terceiro ano: {terceiro:d}'.format(**tabela)
)
```

Saída:

```
Primeiro ano: 413; Segundo ano: 423; Terceiro ano: 433
```

## Formatação de strings à moda antiga

```python
notas = "tirei %1.1f na prova de genética e %d na prova de literatura"
print(notas % (4, 8))
```

Saída:

```
tirei 4.0 na prova de genética e 8 na prova de literatura
```

O operador % (módulo) é usado na formatação de strings por meio de interpolação
de strings. Esse processo ocorre quando as instâncias da expressão 
`'string % valores'`, que estão em formato de strings, são substituídas por 
números.


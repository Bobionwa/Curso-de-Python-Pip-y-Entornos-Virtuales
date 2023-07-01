import math 
import functools
'''
inputUsuario = {2,3,41,4,12,5,13, 12}
inputPares = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
conjuntOutput = inputUsuario.union(inputPares) 
print(conjuntOutput)  

countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA", "MX"}
centralAm = {"GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = countries.union(southAm)

print(new_set)

def compareTriplets(a, b):
  result = [0,0]
  i = 0
  while i <= 2:
    result[0] += 1 if a[i] > b[i] else 0
    result[1] += 1 if a[i] < b[i] else 0
    result[1] += 0 if a[i] == b[i] else 0
    i += 1
  return result

a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
result = compareTriplets(a, b)
print(str(result))

# LIST COMPRENHENSION

x = 3
y = 3
p = 3
ternario = [[i, z, j] for i in range(x+1) for z in range(y+1) for j in range(p+1)]
for i in range(x+1):   # Cada vez que el ciclo externo hace una interacion el ciclo interno hace  una 
  for z in range(y+1): # interacion completamente. Mientras en la primera interacion i es igual a 0 en z
    print(i,z)         # hace una interacion de los numeros del 0 al 3, el la siguiente interaccion i es
print(ternario)        # igual a 1 mientras que z hace una iteracion completamente nuevamente


# DICTIONARY COMPRENHENSION

#diccionario = {i: i**i for i in range(1, 11)}
#print(f'{diccionario}' + '\n')

#import random
#countries = ['col', 'mex', 'arg']
#population = {country : random.randint(1, 100) for country in countries}
#print(population)

#names = ['Timotie', 'Patricio', 'Calamardo']
#age = [19, 37, 26]
#diccionario_edades = {names[i]: age[i] for i in range(len(names))}
#print(diccionario_edades)

text = 'one shot is never enought of this way of us to go in circles ppppp'
frase = text.split()
vocales = {palabra: text.count(palabra) for palabra in text if palabra in 'aeiou'}
print(vocales)

results = 0
i = 0
inpu = input('Operacion separada por espacios: ')
inpu = inpu.split()
while i <= len(inpu):
  if '+' in inpu:
    numeros = [numero for numero in inpu if numero != '+'] 
    signo = inpu.index('+') 
    a = int(inpu[1-signo])
    b = int(inpu[signo+1])
    results = a + b 
    del inpu(1-signo)
    del inpu(signo+1)
    inpu.insert(inpu[1-signo], results)
    del inpu(signo)
    i += 1
    
    for numero in numeros:
      numero = int(numero)
      n = int(numeros[+1])
      results += numero
  elif '-' in inpu: 
    numeros = [numero for numero in inpu if numero != '-']
    for numero in numeros:
      numero = int(numero) 
      results -= numero
  elif '*' in inpu:
    numeros = [numero for numero in inpu if numero != '+'] 
    for numero in numeros:
      numero = int(numero)
      n = int(numeros[+1])
      results == numero*n
      print(type(numero))
      print()

### Clase 16

import random
def message_creator(text):
  if text == 'computadora':
     print('Con mi computadora puedo programar usando Python')
  elif 'celular' in text:
     print('En mi celular puedo aprender usando la app de Platzi')
  elif text == 'cable':
   print('¡Hay un cable en mi bota!')
  else:
   print('Artículo no encontrado.')
text = random.choice(['computadora', 'celular', 'cable']) 
response = message_creator(text)
print(response)

### Clase 17

taste = lambda text: print('No es buena musica') if text != 'The Strokes' else print('Good Taste of Music')
question = input('Cual es tu banda favortia? ')
taste(question)

### Clase 19

numbers = [2, 4, 5 ,6 , 7, 8, 9] 
potencia = int(input('Potencia: '))
pot = []
po = [pot.append(potencia) for i in numbers]
result = list(map(lambda x,y: x ** y, numbers, pot)) 
print(result)

### Clase 20

items = [
  {
    'producto': 'Tenis Vans',
    'price': 2299
  },
  {
    'producto': 'Sudadera Slim Fit',
    'price': 999
  },
  {
    'producto': 'Chaqueta Vinil de Cuero',
    'price': 1299
  }
] 
prices = list(map(lambda item: ,items))
print(prices)
def addTaxes(item):
  item = item.copy()
  item['taxes'] = item['price'] * .19
  return item
taxes = list(map(addTaxes, items))
print(taxes)
print('')
print(items) 

### Clase 23

matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

winteams = list(filter(lambda team: team['home_team_result'] == 'Draw', matches))
print(winteams)

personas = [
  {
    'name' : 'Pedro',
    'country': 'Colombia',
    'age' : 18,
    'course' : 'developer'
  },
  {
    'name' : 'Juan',
    'country': 'Perú',
    'age' : 17,
    'course' : 'UX'
  },
  {
    'name' : 'Carlos',
    'country': 'Chile',
    'age' : 31,
    'course' : 'Diseño'
  },
  {
    'name' : 'Ana Maria',
    'country': 'Colombia',
    'age' : 25,
    'course' : 'Tester'
  }
]
Col = list(filter(lambda perfil: perfil['country'] == 'Colombia' and perfil['age'] >= 18  ,personas))
print(Col)
print(len(Col))

def filter_by_length(words): 
   return[list(filter(lambda palabra: len(palabra) >= 4, words))]
words = ['amor', 'sol', 'piedra', 'día', 'BEBECITA']
response = filter_by_length(words)
print(response)

numbers = [1,2,3,4,5,6]
suma = functools.reduce(lambda counter, numero: counter + numero ,numbers)
max = numbers.max()
print(max)
print(suma

### Clase 26

#import sys
#print(sys.path)
import re 
telefono = 'Pedro trago trigo en un trigal'
result = re.findall('o', telefono)
reserch = re.search("z", telefono)
res = ['yes'  if reserch else 'no']
print(res) 
print(len(result))

import time
timecom = time.localtime()
timemx = time.asctime(timecom)
print(timecom)
print(timemx)

import collections
string = 'Stick es un don pendejo'
string = string.upper()
string.split()
result = collections.Counter(string)
print(result)

orders = [100, 120, 20]
result = functools.reduce(lambda counter, order: order + counter, orders)
print(result)

###Clase 32

string = input('Compon: "anaattasp": ')
assert string == 'patanatas', 'String es igual:  Patanatas'  ##Si entrin es diferente a Patanatas se ejecutara el error de 'String es igual:  Patanatas'

edad = int(input('Edad: '))
raise Exception('Eres menor de edad cbrn') if edad < 18 else print('Aceess to adult content')
#En el codigo de arriba crearemos un error propio si no se cumpre la condicion

def my_divide(a, b): 
   try:
     return a/b                 #En este bloque se coloca el codigo que puede generar algun error
   except ZeroDivisionError:
      return 'No se puede dividir entre 0' #Si se genero, este bloque de codigo sin parar el programa
    
response = my_divide(10, 2)
print(response) 

response = my_divide(10, 0)
print(response) 

import re
try: 
  file = open('./EsEpico_Letra.txt')
  list = []
  for line in file:
    reserach = re.search('aire', line)
    list.append(reserach)
  print(list)
except FileNotFoundError as error:
  print(error)
  
l = []
with open('./EsEpico_Letra.txt', 'r+') as file: 
  print(file.readlines())

  for line in file: 
    if 'tucum' in line:
      line.replace('tucum', 'aves')
      print(line) 
'''
import csv

def read_csv(path): 
  with open(path, 'r') as file:
    total = 0
    listas = list(csv.reader(file, delimiter=',')) 
    for lista in listas:  
      number = int(lista[1]) 
      total += number
    return total

response = read_csv('./data.csv')
print(response)

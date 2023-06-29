
import matplotlib.pyplot as pit 
'''
### Chart Bar with input
def charts_basic(labels, values):
  fix, ax = pit.subplots()
  ax.bar(labels, values)
  pit.show()

if __name__ == '__main__':
  #countries = ['Mexico', 'Colombia', 'Argentina', 'Chile']
  Etiquetas = input('Etiquetas: ')
  Etiquetas = list(Etiquetas.split()) 
  #Mundiales = [4, 3, 3, 1]
  Valores = input('Valores separador por coma: ')
  Valores = Valores.split(',')
  Valores = [int(valor) for valor in Valores]
  charts_basic(Etiquetas, Valores)

import csv
### Chat Circle from a Database
def charts_Circle(labels, values):
  fix, ax = pit.subplots()
  ax.bar(labels, values) 
  pit.show()

def analizeData(path):
  with open(path, 'r') as file:
    listas = list(csv.reader(file, delimiter = ',')) 
    labels = [] values = [] 
    for lista in listas:
      values.append(lista[1])
      labels.append(lista[0]) 
    values = [int(value) for value in values] 
    return labels, values
  
if __name__ == '__main__':
  labels, values = analizeData('./datas.csv')
  charts_Circle(labels, values)
'''
import csv

def charts_Circle(name, labels, values):
  fix, ax = pit.subplots()
  ax.pie(values, labels=labels)
  pit.axis('equal')
  pit.savefig(f'./img/{name}.png')
'''
def analizeData(path, country):
  with open(path, 'r') as file:
    labels, values = [], []  
    file_read = csv.reader(file, delimiter = ',')  
    subtemas = next(file_read) 
    Busqueda  = [list(line.split(',')) for line in file if country in line]   
    for dato in Busqueda:
      iterable = zip(subtemas, dato) 
    iterable = list(iterable) 
    data = [list(par) for par in iterable] 
    dataPopulation = [par for par in data if 'Population' in par[0] and 'World' not in par[0]] 
    for date in dataPopulation:
      values.append(date[1])
      labels.append(date[0])
    return labels, values
        
if __name__ == '__main__':
  name = input('country: ')
  labels, values = analizeData('/home/pagnolix16/PythonPip/Curso-de-Python-Pip-y-Entornos-Virtuales/world_population.csv', name)
  charts_Circle(name, labels, values)

def analizeData(path):  
  with open(path,'r') as file:
    file_read = csv.reader(file, delimiter = ',')   
    listas = [lista for lista in file_read if 'South America' in lista]
    countries = [elemento[2] for elemento in listas if 'Country/Territory' not in elemento[2]]
    worldPopu = [elemento[-1] for elemento in listas if 'W' not in elemento[-1]]
    return countries, worldPopu

if __name__ == '__main__': 
  labels, values = analizeData('./world_population.csv')
  charts_Circle(labels, values)
'''

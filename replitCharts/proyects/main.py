import dataAnalist as analist
'''
print(analist.variableA)

mode = input('Mode: ')
mode = mode.lower()
numbers = input('List Of Numbers: ')
numbers = numbers.split(' ') 
numeros = [int(number) for number in numbers] 

if mode == 'mean':
  print(analist.mean(numeros))
elif mode == 'median':
  print(analist.median(numeros))
elif mode == 'mode':
  print(analist.mode(numeros))
elif mode == 'range':
  print(analist.range(numeros))
else:
  print('thats WRONG, STUPID')

import panda as pd
import charts
def analizeData(path):
  with open(path,'r') as file:
    file_read = csv.reader(file, delimiter = ',')
    listas = [lista for lista in file_read if 'South America' in lista]
    countries = [elemento[2] for elemento in listas if 'Country/Territory' not in elemento[2]]
    worldPopu = [elemento[-1] for elemento in listas if 'W' not in elemento[-1]]
    return countries, worldPopu
'''
import pandas as pd
import charts
if __name__ == '__main__':
  #labels, values = analizeData('./world_population.csv')
  #charts_Circle(labels, values)
  name = input('Continent(South America, Africa, Asia, Europe, Oceania, North America): ')
  df = pd.read_csv('world_population.csv')
  df = df[df['Continent'] == name]
  countries = df['Country/Territory'].values
  worldPopu = df['World Population Percentage'].values
  charts.charts_Circle(name, countries, worldPopu)

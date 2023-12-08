import csv

communes_2008 = []
communes_2016 = []
communes_2021 = []
metadonnees_communes = []

with open('donnees_2008.csv', newline = '') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    for row in reader:
#        print(','.join(row))
        communes_2008.append(row)
del(communes_2008[0])
with open('donnees_2016.csv', newline = '') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    for row in reader:
#        print(','.join(row))
        communes_2016.append(row)
del(communes_2016[0])
with open('donnees_2021.csv', newline = '') as csvfile:
    reader = csv.reader(csvfile, delimiter = ';')
    for row in reader:
#        print(','.join(row))
        communes_2021.append(row)
del(communes_2021[0])
with open('metadonnees_communes.csv', newline = '') as csvfile:
    reader = csv.reader(csvfile, delimiter = ';')
    for row in reader:
#        print(','.join(row))
        metadonnees_communes.append(row)
del(metadonnees_communes[0])


communes_2008 = [[communes_2008[i+1][6], int(communes_2008[i+1][9])] for i in range(len(communes_2008)-1)]
#print(communes_2008)
test = []
for i in range(len(communes_2008)):
#    m = list(communes_2008[i][0])
#    if m[0] == '8':
    if communes_2008[i][0] == 'Auxerre':
        test.append(communes_2008[i])
print(test)
test = []
communes_2016 = [[communes_2016[i+1][6], int(communes_2016[i+1][9])] for i in range(len(communes_2016)-1)]
for i in range(len(communes_2016)):
#    m = list(communes_2016[i][0])
#    if m[0] == '8':
    if communes_2016[i][0] == 'Auxerre':
        test.append(communes_2016[i])
print(test)
test = []
communes_2021 = [[communes_2021[i+1][2], int(communes_2021[i+1][5])] for i in range(len(communes_2021)-1)]
#print(communes_2021)
for i in range(len(communes_2021)):
    m = list(communes_2021[i][0])
    if m[0] == '89024':
        test.append(m)
print(test)

#import numpy as np 
from matplotlib import pyplot as plt
from pylab import*
"""
plt.plot(communes_2008, color = 'b')
plt.scatter(communes_2016, color = 'r')
plt.scatter(communes_2021, color = 'g')
plt.ylabel('Population')
plt.xlabel('Communes')
plt.show()
"""


#  -*- coding: utf-8 -*-
#
# Author: Lucas Gabriel B

from matplotlib import pyplot as plt
import numpy as np

# create empty lists
dataX = list()
dataY = list()
data = list()

# read the data of the file and covert to float
with open('dados.txt', 'r') as file:
    data = [i.replace(',', '.').split(';') for i in file.readlines()]
    for point in data:
        # split the data in two lists x and y
        x, y = point
        dataX.append(float(x))
        dataY.append(float(y))


def sum_of_xy():
    ''' return the sum of x*y for all values in data '''
    result = 0
    for i, v in enumerate(dataX):
        result += v * dataY[i]

    return result


def sum_of_x2():
    ''' return the sum of x**2 for all values in data '''
    result = 0
    for x in dataX:
        result += x ** 2

    return result


def sum_of_y2():
    ''' return the sum of y**2 for all values in data '''
    result = 0
    for y in dataY:
        result += y ** 2

    return result


# calculates A and b in Y=AX+B
a = round(((len(data) * sum_of_xy()) - (sum(dataX) * sum(dataY))) / ((len(data) * sum_of_x2()) - (sum(dataX) ** 2)), 2)
b = round((sum(dataY) / len(data)) - (a * (sum(dataX) /len(data))), 2)

# calculates the linear correlation
linear_correlation = round(((len(data) * sum_of_xy()) - (sum(dataX) * sum(dataY))) /
 (((len(data) * sum_of_x2()) - (sum(dataX) ** 2)) * ((len(data) * sum_of_y2()) - (sum(dataY) **2))) ** 0.5, 2)

def predicts(data):
    ''' predicts y based on data from x '''
    result = list()
    for x in data:
        result.append(a*x+b)

    return result

 
plt.grid(alpha=0.9)

# plot the data
plt.scatter(dataX, dataY, label='Dados')

# plot the line
plt.plot(dataX, predicts(dataX), linestyle='solid', label='Previsão', color='red')

title_text = 'Regressao Linear\n'

# checks whether b is positive or negative for better text formatting
if b > 0:
    title_text += f'\nEquação da reta: Y = {a}X + {b}'.replace('.', ',')
else:
    title_text += f'\nEquação da reta: Y = {a}X - {abs(b)}'.replace('.', ',')

# add the linear correlation to the title text
title_text += f'\nCorrelação Linear: {linear_correlation}'

# plot the title text
plt.title(title_text)

plt.xlabel('X')
plt.ylabel('Y')
plt.gca().legend()
plt.show()

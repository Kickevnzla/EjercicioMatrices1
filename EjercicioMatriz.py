from mimetypes import init
from turtle import width, window_height
from typing import final
import numpy as np
import random as rnd

initialData = []

width = 5
height = 5

for i in range(width * height):
    initialData.append(rnd.randint(1, 5))

matrix1 = np.reshape(initialData, (width, height), order="C")
print(initialData)

finalData = [None for i in range(len(initialData))]


def isTopLeftItem(i):
    if i == 0:
        return True
    else:
        return False


def isTopRigthItem(i):
    if i == width - 1:
        return True
    else:
        return False


def isButtomLeftItem(i):
    if i == len(initialData) - width:
        return True
    else:
        return False


def isButtomRigthItem(i):
    if i == len(initialData):
        return True
    else:
        return False


def isTopRow(i):
    if i > 0 and i < width - 1:
        return True
    else:
        return False


def isLeftColumn(i):
    if isTopLeftItem(i) is False and isButtomLeftItem(i) is False and i % width == 0:
        return True
    else:
        return False


def isRigthColumn(i):
    if isTopRigthItem(i) is False and isButtomRigthItem(i) is False and i + 1 % width == 0:
        return True
    else:
        return False


def isButtomRow(i):
    if isButtomLeftItem(i) is False and isButtomRigthItem(i) is False and i >= len(initialData) - width & i < len(initialData):
        return True
    else:
        return False


def isCenterItem(i):
    if i > 0 and i < len(initialData) and isTopLeftItem(i) is False and isTopRow(i) is False and isTopRigthItem(i) is False and isLeftColumn(i) is False and isRigthColumn(i) is False and isButtomLeftItem(i) is False and isButtomRow(i) is False and isButtomLeftItem(i) is False:
        return True
    else:
        return False


for i in range(len(initialData)):
    if isTopLeftItem(i):
        if initialData[i] == initialData[i + 1] or initialData[i] == initialData[width]:
            finalData[i] = 1
        else:
            finalData[i] = 0
    if isTopRow(i):
        if initialData[i] == initialData[i - 1] or initialData[i] == initialData[i + 1] or initialData[i] == initialData[width + i]:
            finalData[i] = 1
        else:
            finalData[i] = 0
    if isTopRigthItem(i):
        if initialData[i] == initialData[i - 1] or initialData[i] == initialData[(width * 2) - 1]:
            finalData[i] = 1
        else:
            finalData[i] = 0
    if isLeftColumn(i):
        if initialData[i] == initialData[i + 1]:
            finalData[i] = 1
        else:
            finalData[i] = 0
    if isRigthColumn(i):
        if initialData[i] == initialData[i - 1]:
            finalData[i] = 1
        else:
            finalData[i] = 0
    if isButtomLeftItem(i):
        if initialData[i] == initialData[i + 1] or initialData[i] == initialData[len(initialData) - (width * 2)]:
            finalData[i] = 1
        else:
            finalData[i] = 0
    if isButtomRow(i):
        if initialData[i] == initialData[i - width]:
            finalData[i] = 1
        else:
            finalData[i] = 0
    if isButtomRigthItem(i):
        if initialData[i] == initialData[i - 1] or initialData[i] == initialData[i - width]:
            finalData[i] = 1
        else:
            finalData[i] = 0

matrix2 = np.reshape(finalData, (width, height), order="C")

print(matrix1)

print(matrix2)
print(initialData)
import random as rnd
import numpy as np

initial_data = []

width = int(input('Ingrese ancho de matriz: '))
height = int(input('Ingrese alto de matriz: '))

initial_matrix = np.random.randint(1, 5, (width, height))

extended_matrix = np.insert(np.insert(initial_matrix, 0, np.zeros(
    height), axis=1), width + 1, np.zeros(height), axis=1)

extended_matrix = np.insert(np.insert(extended_matrix, 0, np.zeros(
    width+2), axis=0), width+1, np.zeros(width+2), axis=0)

left_matrix = extended_matrix[1:height+1, :width]

top_matrix = extended_matrix[:height, 1:width+1]

right_matrix = extended_matrix[1:height+1, 2:]

bottom_matrix = extended_matrix[2:, 1:width+1]

final_matrix_l = initial_matrix - left_matrix
final_matrix_t = initial_matrix - top_matrix
final_matrix_r = initial_matrix - right_matrix
final_matrix_b = initial_matrix - bottom_matrix

answer = (final_matrix_l == 0) | (final_matrix_t == 0) | (
    final_matrix_r == 0) | (final_matrix_b == 0)

answer = np.where(answer == True, answer, 0)

print(initial_matrix)

print(answer)

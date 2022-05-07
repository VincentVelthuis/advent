import sys, fileinput
import numpy as np

# GLOBALS
gamma = ''
epsilon = ''

# FUNCTIONS
def calculate_rates(array):
    for column in range(array.shape[1]):
        most_common_bit(array[:,column])
    return int(gamma,2), int(epsilon,2)
        
def most_common_bit(array):
    global gamma, epsilon

    if np.bincount(array).argmax() > 0:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

def initialize_np_array():
    lines = [line.strip() for line in fileinput.input(files=sys.argv[1])]
    matrix = np.zeros((len(lines),len(lines[0])), dtype=np.int64)
    
    for line_number, line in enumerate(lines):
        for char_number, char in enumerate(line):
            if char == '1':
                matrix[line_number,char_number] = 1
        
    return matrix

# ACTIONS
matrix = initialize_np_array()
gamma_int, epsilon_int = calculate_rates(matrix)
ans = gamma_int*epsilon_int
print(gamma,gamma_int,'___',epsilon,epsilon_int,'___',ans)
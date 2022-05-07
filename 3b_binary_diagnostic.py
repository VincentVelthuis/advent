import sys, fileinput
import numpy as np
import copy

oxygen_generator_rating = 0
co2_scrubber_rating = 0

def initialize_np_array():
    lines = [line.strip() for line in fileinput.input(files=sys.argv[1])]
    matrix = np.zeros((len(lines),len(lines[0])+1), dtype=np.int64)
    
    for line_number, line in enumerate(lines):
        for char_number, char in enumerate(line):
            if char == '1':
                matrix[line_number,char_number] = 1
        matrix[line_number,-1]=line
        
    return matrix

def oxygen_generator_rating(array):
    if len(array) == 1:
        global oxygen_generator_rating
        oxygen_generator_rating = array[0][-1]
        return
    
    column = array[:,0]
    
    most_common = np.bincount(column).argmax()
    if np.bincount(column)[0] == np.bincount(column)[1]:
        most_common = 1
    
    row_most = np.where(column == most_common)
    # row_least = np.where(column!=most_common)
    
    new = array[row_most,1:]
    new = new.reshape(new.shape[1:])
    oxygen_generator_rating(new)

def calc_co2_scrubber_rating(array):
    if len(array) == 1:
        global co2_scrubber_rating
        co2_scrubber_rating = array[0][-1]
        return
    
    column = array[:,0]
    
    most_common = np.bincount(column).argmax()
    if np.bincount(column)[0] == np.bincount(column)[1]:
        most_common = 1
    
    row_least = np.where(column!=most_common)
    
    new = array[row_least,1:]
    new = new.reshape(new.shape[1:])
    calc_co2_scrubber_rating(new) 

# ACTIONS
matrix = initialize_np_array()

oxygen_generator_rating(matrix)
ox = int(str(oxygen_generator_rating),2)

calc_co2_scrubber_rating(matrix)
co2 = int(str(co2_scrubber_rating),2)

ans=ox*co2
print(oxygen_generator_rating, ox, co2_scrubber_rating, co2, ans)

"""
Program to calculate number of attacking queens
"""
from scipy import stats
from collections import Counter
from itertools import combinations
import ipdb

def attacking_queens(queen_string):
    # Get number of row wise attacking queens
    numbers = [int(i) for i in queen_string]
    row_attacks = 0
    for pair in combinations(numbers,2):
        if pair[0] == pair[1]:
            row_attacks +=1

    # Get diagonals by checking if slope is zero
    integers = [(i,int(l)) for i,l in enumerate(queen_string,1)]
    
    diagonal_attacks = 0
    # Calculate Slope, if 1 it's a diagonal attack

    for queen_1, queen_2 in combinations(integers, 2):
        l = [*zip(queen_1,queen_2)]
        slope, _, _, _, _ = stats.linregress(l)
        if slope in (-1,1):
            diagonal_attacks +=1

    return row_attacks + diagonal_attacks

#jprint(attacking_queens('24748552'))
#print(attacking_queens('32752411'))
#print(attacking_queens('24415124'))
#print(attacking_queens('32543213'))

print(attacking_queens('32748552'))
print(attacking_queens('32752124'))
print(attacking_queens('24752411'))


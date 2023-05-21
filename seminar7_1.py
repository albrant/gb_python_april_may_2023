import math 

def find_farthest_orbit(data):
    squares = list(map(lambda i: math.pi * i[0] * i[1], data))
    # for i in data:
    #     a,b = i
    #     s = math.pi * a * b
    #     squares.append(s)
    ind = squares.index(max(squares))
    return data[ind]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))

import math

T = int(input(""))

def highest(list):
    high = list[0]
    for num in list:
        if num > high:
            high = num
    return high

def sign(num):
    if num < 0:
        return (-1)
    else:
        return(1)

outputs = []

for i in range(0,T):
    NM = input("")
    starts = input("") #space separated
    ends = input("")
    start_list = []
    end_list = []
    nm_list = []
    for char in NM: 
        if char != " ":
            nm_list.append(int(char))
    
    for start in starts:
        if start != " ":
            start_list.append(int(start))
    
    for end in ends:
        if end != " ":
            end_list.append(int(end))

    travel_dists = []

    for i in range(0,len(end_list)):
        n = nm_list[0]
        m = nm_list[1]
        dist = end_list[i] - start_list[i]
        if dist <= m and dist >= 1:
            travel_dists.append(dist)
        else:
            sgn = sign(dist)
            dist = sgn * (abs(dist) % m) + m
            travel_dists.append(dist)

    output = highest(travel_dists)
    outputs.append(output)

for output in outputs:
    print(output)
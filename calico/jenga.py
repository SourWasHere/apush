T = int(input(""))

for i in range(0,T):
    N = int(input(""))
    current = 0
    layers = 0
    if N % 3 == 0:
        layers = int(N/3)

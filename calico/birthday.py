
T = int(input(""))

outputs = []

for i in range(0,T):
    N = int(input(""))
    days = N * N
    before_end = N - 1
    current_days = days - before_end
    for j in range(2, N):
        current_days = current_days + j*j
    if N == 1:
        outputs.append(0)
    else: 
        outputs.append(current_days)

for output in outputs: 
    print(output)



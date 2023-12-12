while True:
    T = int(input(""))
    if T >= 1 and T <= 100:
        break 
    else: 
        print("out of range")

outputs = []

for i in range(0,T):
    N = 0
    while True:
        N = int(input(""))
        if N % 10 == 0 and N >= 0 and N <= 500:
            break
        else: print("input needs to be multiple of 10 and in range")
    if N == 0:
        outputs.append("haha good one")
    elif N > 0 and N < 180:
        str = ""
        for i in range(int(N/10)):
            str = str + "berkeley"
        str = str + "time"
        outputs.append(str)
    else:
        outputs.append("canceled")
  
for output in outputs:
    print(output)
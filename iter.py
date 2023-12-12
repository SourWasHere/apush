import random

tries = 0
while True:
    num = random.randint(0, 100)
    if num == 1:
        print(num)
        break
    else:
        tries += 1

print(tries)

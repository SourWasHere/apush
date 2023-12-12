while True:
    T = int(input("test cases: "))
    if T >= 1 and T <= 100:
        break
    else:
        print("input a number between 1 and 100")

for i in range(0,T):
    N = input("number of faces: ")
    face_numbers = input("number for each face (space separated): ")
    numbers_list = []
    j = 0
    while j < len(face_numbers):
        if face_numbers[j] != " ":
            numbers_list.append(int(face_numbers[j]))
        j = j + 1
    numbers_tuple = tuple(numbers_list)
    count_list = []
    for num in numbers_tuple:
        count = 0
        for number in numbers_list:
            if number == num:
                count = count + 1
        count_list.append(count)
    high = 0
    for count in count_list:
        if count > high:
            high = count
    print(numbers_tuple[count_list.index(high)])






with open("travel-bucket-list.txt", "w+") as file:
    content = []
    input_1 = input("where yuo want travel")
    if input_1 != "quit":
        content.append(input_1)
    while True:
        if input_1 == "quit":
            break
        input_2 = input("am add to list\n\naanywhere else")
        if input_2 == "quit":
            break
        else:
            content.append(input_2)
    
    for place in content:
        file.write(place + "\n")
print("of bye")





























































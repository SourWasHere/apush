my_list = [1, 7, 8, 3, 5]

my_iter = iter(my_list)

print(next(my_iter))

while True:
    try:
        #Get the next item
        element = next(my_iter)
        print(element)
    except StopIteration:
        print("all done")
        break
import random

#change str value of unit variable below to change unit
unit = "6" 
txt = open("C:/Users/sour/OneDrive/Documents/python/apush/chronology/unit" + unit + "_events.txt", encoding="utf-8") 
lines = txt.readlines()
datenumbers = [] #all dates and events
events = []

def display(list, nums_list):
    order = ""
    for i in range(0,len(list)):
        order = order + "(" + str(nums_list[i]) + ") " + list[i] + " " #(1) american revolution
    order = order + "\n"
    print(order)


def list_match(list, comparison): #returns number of elements in same index for both lists 
    matches = 0
    for i in range(0,len(list)):
        if comparison[i] == list[i]:
            matches = matches + 1
    
    matches_score = str(matches) + "/" + str(len(list)) + " correct\n" #1/5
    return matches_score

def change_indexes(lists, elems, newindex): #first two parameters are lists
    for i in range(0,len(lists)): #makes same change to all indexes
        lists[i].remove(elems[i])
        lists[i].insert(newindex, elems[i])

def read4(string): #reads 1st 4 characters of string
    read = ""
    for i in range(4):
        read = read + string[i]
    return read

def sort(list): #sorts by least to greatest
    list = list.copy()
    sorted_list = []
    length = len(list)
    for i in range(0, length):
        low = list[0]
        for num in list:
            if low > num:
                low = num
        sorted_list.append(low)
        list.remove(low)
    return(sorted_list)

for event in lines: #processes txt readings into lists
    event = event.rstrip()
    date = read4(event)
    events.append(event.lstrip(date).strip())
    datenumbers.append(int(date))

#game

event_nums = [1,2,3,4,5]
events_round = [] #5 events and matching dates are picked per game
dates_round = []

rands = []
while True:
    rand = random.randrange(0,len(events))
    rands.append(rand)
    if len(tuple(rands)) != len(rands):
        rands.remove(rand)
        print("same rand")
    elif len(rands) > 5:
        break
    else:
        events_round.append(events[rand])
        dates_round.append(datenumbers[rand])


correct_dates = sort(dates_round)

while True:
    new_index = 0
    event_num = 0
    display(events_round, event_nums)

    while True:
        command = input("input:") #format: [number][< or > signs] (no spaces) (ex: "1>>" moves event 1 two spaces right)

        if command == "exit":
            quit()
             
        event_num = int(command[0])
        index = (event_nums.index(event_num))
        move_sum = 0
        
        for i in range(1,len(command)):
            if command[i] == ">":
                move_sum = move_sum + 1
            elif command[i] == "<":
                move_sum = move_sum - 1

        new_index = index + move_sum

        if new_index < 0 or new_index > 4:
            print("out of range")
        else:
            break

    ind = event_nums.index(event_num)
    change_indexes([event_nums, events_round, dates_round], [event_nums[ind], 
    events_round[ind], dates_round[ind]], new_index)

    #print(dates_round) #bugfix
    #print(correct_dates)

    print(list_match(dates_round, correct_dates))
    if list_match(dates_round, correct_dates) == "5/5 correct\n":
        print("you win")
        display(events_round, event_nums)
        break

    
    

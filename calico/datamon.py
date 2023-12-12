T = input("")

class mon():
    def __init__(self, type_):
        type_ = self.type_
    
    input_list = []
    
    def eat(self, num):
        self.input_list.append(num)
    
    def poop(self):
        input_list = self.input_list
        if self.type_ == "heap":
            high = input_list[0]
            for num in input_list:
                if num > high:
                    high = num
            return [high]
        
        elif self.type_ == "stack":
            last = input_list[len(input_list) - 1]
            input_list.remove(last)
            return(last)

            




        

import random

class LotteryNumbers:
    def __init__(self, tries, list):
        self.tries = tries
        self.list = list
 
    def number_of_hits(self, numbers: list):    
        return f"You nailed {len([number for number in numbers if number in self.list])} numbers in your {self.tries} try"
 
    def hits_in_place(self, numbers):
        print(f"You nailed the below numbers in your {self.tries} try")
        return [number for number in numbers if number in self.list ]
 
if __name__ == "__main__":
    
    lotteryNums1 = random.sample(range(0, 41), 7)
    try1 = LotteryNumbers("first", lotteryNums1)
    numbers = input("please enter 7 numbers from 1 to 40, separated by a space: ")
    my_numbers = map(int, numbers.split()) 
    print(f"The lottery numbers today are: {lotteryNums1}")
    print(try1.number_of_hits(my_numbers))            
 
    lotteryNums2 = random.sample(range(0, 41), 7)
    try2 = LotteryNumbers("second", lotteryNums2)
    numbers2 = input("please enter 7 numbers from 1 to 40, separated by a space: ")
    my_numbers2 = map(int, numbers2.split()) 
    print(f"The lottery numbers today are: {lotteryNums2}")
    print(try2.hits_in_place(my_numbers2))
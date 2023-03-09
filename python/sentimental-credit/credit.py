import cs50

# Checks if the number is valid with Hans Peter Luhn algorithm and returns True or False
def sum_1(cc_number):
    list2 = []
    rev = cc_number[::-1]
    i = 1
    while i < len(rev):
        list2.append(rev[i]*2)
        i+=2
    rev2 = "".join(map(str,list2))
    sum1 = 0
    for i in range(len(rev2)):
       sum1 += int(rev2[i])

    sum2 = 0
    i = 0
    while i < len(rev):
        sum2 +=rev[i]
        i+=2
    total= sum1+sum2
    return total % 10 == 0



number = cs50.get_string("Please enter a cc number: ")
number.split(sep = ",") # splits the strings and adds commas
numbers = list(map(int, number)) #converts the string into a list of ints
if sum_1(numbers) == False: #first checks if the number is valid
    print("INVALID\n")
else:
    if len(numbers) == 15 and numbers[0] == 3 and numbers[1] in (4,7):
        print("AMEX\n")
    elif len(numbers) == 16:
        if numbers[0] == 4:
            print("VISA\n")
        elif numbers[0] == 5 and numbers[1] in (1,2,3,4,5):
            print("MASTERCARD\n")
        else:
            print("INVALID\n")
    elif len(numbers) == 13:
        print("VISA\n")

    else:
        print("INVALID")


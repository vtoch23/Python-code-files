def even_numbers(beginning: int, maximum: int):
    number = beginning
    while number >= beginning and number <= maximum:
        if number % 2 == 0:
            yield number
        number += 1
 
if __name__ == "__main__":
    number1 = int(input("Please enter start number: "))
    number2 = int(input("Please enter end number: "))
    numbers = even_numbers(number1, number2)
    for number in numbers:
        print(number)
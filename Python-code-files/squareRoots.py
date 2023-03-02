from math import sqrt
def square_roots(numbers: list):   
    return [sqrt(number) for number in numbers]
 
if __name__ == "__main__":
    numbers2 = input("Please enter numbers separated by a comma to calculate their roots: ")
    roots = list(map(int, numbers2.split(",")))
    for b in range(len(square_roots(roots))):
        root = square_roots(roots)[b]
        for i in range(len(roots)):
            if i == b:
                print(f"The square root of {roots[i]} is: {root}")
            else:
                continue
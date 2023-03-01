def sort_by_remaining_stock(items: list):
    def sort_by_stock(item: tuple):
        return item[1]
    
    return sorted(items, key = sort_by_stock, reverse = True)
 
 
if __name__ == "__main__":
    fruit1 = input("Please enter a fruit: ")
    stock1 = int(input(f"How many {fruit1}s do you have? "))
    fruit2 = input("Please enter another fruit: ")
    stock2 = int(input(f"How many {fruit2}s do you have? "))
    fruit3 = input("Finally please enter the last fruit: ")
    stock3 = int(input(f"And how many {fruit3}s do you have? "))

    products = [(fruit1, stock1), (fruit2, stock2), (fruit3, stock3)]
 
    for product in sort_by_remaining_stock(products):
        print(f"{product[0]} {product[1]}")
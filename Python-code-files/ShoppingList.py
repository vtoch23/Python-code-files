class ShoppingList:
    def __init__(self):
        self.products = []
 
    def number_of_items(self):
        return len(self.products)
 
    def add(self, product: str, number: int):
        self.products.append((product, number))
 
    def __iter__(self):
        self.n = 0
        return self
 
    def __next__(self):
        if self.n < len(self.products):
            product = self.products[self.n]
            self.n += 1
            return product
        else:
            raise StopIteration
 
def products_in_shopping_list(shopping_list, amount: int):
    return [item[0] for item in shopping_list if item[1] >= amount]
 
 
if __name__ == "__main__":
    product1 = input("Please enter any product (1/4): ")
    quantity1 = int(input("How many do you have? "))
    product2 = input("Please enter another product (2/4: ")
    quantity2 = int(input("How many do you have? "))
    product3 = input("Please enter another product (3/4: ")
    quantity3 = int(input("How many do you have? "))
    product4 = input("Please enter the last product (4/4: ")
    quantity4 = int(input("How many do you have? "))

    minimum=int(input("OK. What is the minimum number of products you require? "))

    my_list = ShoppingList()
    my_list.add(product1, quantity1)
    my_list.add(product2, quantity2)
    my_list.add(product3, quantity3)
    my_list.add(product4, quantity4)
    

    print(f"the shopping list contains at least {minimum} of the following items:")
    
    for product in products_in_shopping_list(my_list, minimum):
        print(product)
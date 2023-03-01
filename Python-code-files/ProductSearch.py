def search(products: list, criterion: callable, price):
    list = []
    for product in products:
        if criterion(product, price):
            list.append(product)
    return list        
 
def price_under_4_euros(product, price):
    return product[1] < price
 
 
if __name__ == "__main__":
    product1 = input("Please enter a fruit: ")
    price1 = int(input("Please enter the fruit's price: "))
    product2 = input("PLease enter another fruit: ")
    price2 = int(input("Please enter the fruit's price: "))
    price = int(input("Enter maximum price of products you'd like to find: "))
    products = [(product1, price1), (product2, price2)]
    for product in search(products, price_under_4_euros, price):
        print(product)
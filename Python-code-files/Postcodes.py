class City:
    
    def __init__(self, name: str, population: int):
        self.__name = name
        self.__population = population
 
    def name(self):
        return self.__name
 
    def population(self):
        return self.__population
 
    def __str__(self):
        return f"{self.__name} ({self.__population} residents)."

if __name__ == "__main__":
    while True:
        try:     
            city1 = City(input("Please enter a city: "), int(input("Please enter number of poeple(population): ")))  
            city2 = City(input("Please enter a city: "), int(input("Please enter number of poeple(population): ")))
            city3 = City(input("Please enter a city: "), int(input("Please enter number of poeple(population): ")))  
            break
        except Exception as e:
            print(f"Invalid input - {e.args}")
            continue

    postcodes = ([city1, city2, city3])
    for post in postcodes:
        print(post)
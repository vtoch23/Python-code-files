class RealProperty:
    def __init__(self, id: int, rooms: int , square_meters: int, price_per_sqm: int, description: str):
        self.number = id
        self.rooms = rooms
        self.square_meters = square_meters
        self.price_per_sqm = price_per_sqm
        self.description = description
 
    def price(self):
        return self.price_per_sqm * self.square_meters
        
    def bigger(self, compared_to):
        return self.square_meters > compared_to.square_meters
 
    def price_difference(self, compared_to):
        # Function abs returns absolute value
        difference = abs((self.price_per_sqm * self.square_meters) - (compared_to.price_per_sqm * compared_to.square_meters))
        return difference
 
    def more_expensive(self, compared_to):
        difference = (self.price_per_sqm * self.square_meters) - (compared_to.price_per_sqm * compared_to.square_meters)
        return difference > 0
    
    def __str__(self):
        return f"Property id:{self.number}, {self.square_meters} sqm, price per sqm: {self.price_per_sqm}, description: {self.description}"
 
    def __repr__(self):
        return (f'RealProperty(rooms = {self.rooms}, square_meters = {self.square_meters}, ' + 
            f'price_per_sqm = {self.price_per_sqm}, description = {self.description})')
 
def cheaper_properties(properties: list, reference: RealProperty):
    return [(house, reference.price_difference(house))for house in properties if reference.more_expensive(house)]
 
 
if __name__ == "__main__":
    a1 = RealProperty(1, 1, 16, 5500, "Central studio")
    print(a1)
    a2 = RealProperty(2, 2, 38, 4200, "Two bedrooms downtown")
    print(a2)
    a3 = RealProperty(3, 3, 78, 2500, "Three bedrooms in the suburbs")
    print(a3)
    a4 = RealProperty(4, 6, 215, 500, "Farm in the middle of nowhere")
    print(a4)
    a5 = RealProperty(5, 4, 105, 1700, "Loft in a small town")
    print(a5)
    a6 = RealProperty(6, 25, 1200, 2500, "Countryside mansion")
    print(a6)
    
    properties = [a1, a2, a3, a4, a5, a6]
    prop = int(input("Enter a property id to find the cheaper options: "))
    for item in properties:
        if item.number == prop:
            property = item

    print(f"cheaper options when compared to {property.description}:")
    for item in cheaper_properties(properties, property):
        print(f"{item[0].description:35} price difference {item[1]} euros")
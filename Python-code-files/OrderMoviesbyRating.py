def sort_by_ratings(items: list):
    def order_by_rating(item: dict):
        return item["rating"]
    return sorted(items, key = order_by_rating, reverse = True)
 
if __name__ == "__main__":
    movie1 = input("Please enter a movie name: ")
    rating1 = float(input("Please enter the movie's rating: "))
    movie2 = input("Please enter another movie name: ")
    rating2 = float(input("Please enter the movie's rating: "))
    movie3 = input("Please enter the last movie name: ")
    rating3 = float(input("Please enter the movie's rating: "))
    shows = [{ "name": movie1, "rating" : rating1 }, { "name": movie2, "rating" : rating2 },  { "name": movie3, "rating" :rating3 }  ]
 
    print("Rating according to IMDB")
    for show in sort_by_ratings(shows):
        print(f"{show['name']}  {show['rating']}")
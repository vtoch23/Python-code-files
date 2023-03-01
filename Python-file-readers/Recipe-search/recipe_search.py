def search_by_name(filename: str, word: str):
    finalList = []
    with open(filename) as file:
        data = file.read()
        for line in data:
            line = data.replace("\n", ",")
            recipes = line.split(",,")
        for x in recipes:
            ingredients = x.split(",")
            name = ingredients[0]
            if word in name.lower():
                finalList.append(ingredients)
            else:
                continue  
    if len(finalList) > 0:
        return finalList
    return False             

def search_by_time(filename: str, prep_time: int):
    finalList = []
    with open(filename) as file:
        data = file.read()
        for line in data:
            line = data.replace("\n", ",")
            recipes = line.split(",,")
        for x in recipes:
            ingredients = x.split(",")
            time = int(ingredients[1])
            if time <= prep_time:
                finalList.append(ingredients)
            else:
                continue  
    if len(finalList) > 0:
        return finalList
    return False    

def search_by_ingredient(filename: str, ingredient: str):
    allRecipes = []
    recipeList=[]
    with open(filename) as myFile:
        content = myFile.read()
        for line in content:
            line = content.replace("\n", ",")
            recipe = line.split(",,")  
        allRecipes.append(recipe)
    for item in allRecipes:
        for i in range(len(item)):
            recipe = item[i]
            recipeList.append(recipe)
    
    finalList3 = []
    
    for i in range(len(recipeList)):
        recipe2 = recipeList[i]    
        comma = recipe2.find(",")
        word1 = recipe2[0:comma]
        recipe3 = recipe2[comma+1:]
        comma2 = recipe3.find(",")
        word2 = recipe3[0:comma2]
        word2 = int(word2)
        rest = recipe2[comma2:]
        found2 = rest.find(ingredient)
        if found2 != -1:
            sentence = ""
            sentence = word1+", preparation time "+str(word2) + " min"
            finalList3.append(sentence)
        continue
        
    if len(finalList3) > 0:
        return finalList3  
    else:
        return False 

if __name__ == "__main__":
    
    while True:
        print("Search recipes by ingredient, by desired preparation time or by name")
        try:
            for recipe in search_by_ingredient("recipes1.txt", input("Please search by basic ingredient: ")):
                print("Recipe: ")
                print(recipe)  
            print()

            for recipe in search_by_time("recipes1.txt", int(input("Please enter a desired maximum time of preparation: "))):
                print("Recipe: ")
                for item in recipe:
                    print(item, end = ",")  
                print("\n")    
            print()

            for recipe in search_by_name("recipes1.txt", input("Please find a recipe for: ")):
                print("Recipe: ")
                for item in recipe:
                    print(item, end = ",")  
                print()  
            print()
            break           
        except:
            print("Invalid input or missing item, please try again")
            continue

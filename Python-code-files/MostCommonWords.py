def most_common_words(filename: str, lower_limit: int):

    with open (filename) as file:
        content = file.read()
        content = content.strip()
        content = content.replace(".", "")
        content = content.replace(",", "")
        content = content.replace("\n", " ")
        words = content.split(" ")
        return {word: words.count(word) for word in words if words.count(word) >= lower_limit}        
if __name__ == "__main__":
    list2 = most_common_words("programming.txt", 6)
    print(list2)
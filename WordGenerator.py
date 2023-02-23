from random import choice
def word_generator(characters: str, length: int, amount: int):
    return (characters[i:i+length] for i in range(amount)) 
     
 
if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)
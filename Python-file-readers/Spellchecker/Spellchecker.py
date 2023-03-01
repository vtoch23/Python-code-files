string = input("Write text")
newSentence = ""
parts = string.split(" ")
dictionary = []
for i in range(len(parts)):
    word = parts[i]
    with open("wordlist.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            dictionary.append(line)
        if word.lower() in dictionary:
            newSentence += word +" "
        else:
            word = "*"+word+"* "
            newSentence += word
print(newSentence)   
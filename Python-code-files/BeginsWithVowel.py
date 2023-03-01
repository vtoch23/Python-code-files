def begin_with_vowel(words: list):
    vowel_words = [word for word in words if word[0].lower() in "a, e, i, o, u"]
    if len(vowel_words) == 1:
        print(f"The only word beginning with a vowel is {vowel_words[0]}")
    else:
        print("Words beginning with a vowel: ")
        return vowel_words
if __name__ == "__main__":
    words = input("Please enter random words separated by a space: ")
    word_list = map(str, words.split(" "))
    try:
        for vowelled in begin_with_vowel(list(word_list)):
            print(vowelled)
    except:
        pass        
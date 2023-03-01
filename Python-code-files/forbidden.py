def filter_forbidden(string: str, forbidden: str):
    new_string = "".join([character for character in string if not character in forbidden])
    return new_string
 
 
if __name__ == "__main__":

    sentence = input("Please enter a sentence and insert randomly some of the following characters '!?:,.$%&@<>'")
    filtered = filter_forbidden(sentence, "!?:,.$%&@<>")
    print(filtered)  
mydict = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J", 10: "K", 11: "L", 12:  "M", 13: "N", 14: "O", 15: "P", 16: "Q", 17: "R", 18: "S", 19: "T", 20: "U", 21: "V", 22: "W", 23: "X", 24: "Y", 25: "Z"}
def letter_def(number23):
    if number23 < 0:
        return number23*-1
    else:
        return number23
number = int(input("Layers: "))
beginning = -number+1
end = number-1
mylist = []
for i in range(beginning,1):
    mystr = ""
    if i == beginning or i == end or i == -beginning or i == -end:
        for b in range(beginning, number):
            letter = mydict[letter_def(i)]        
            mystr+=letter
     
    elif i == 0 :
        for b in range(beginning,number):
            if b == -beginning or b == beginning: 
                letter = mydict[letter_def(b)]
            elif b == 0:
                letter = mydict[i]
            else:
                if b <= 0:
                    letter = mydict[i-b]
                else:
                    letter = mydict[i+b]   
            mystr+=letter 
    elif i != number and i != 0 or i != -number and i != 0:
        for b in range(beginning,number):
            if b == -beginning or b == beginning:
                letter = mydict[letter_def(b)]
            else:
                if b < i or b > -i:
                    letter = mydict[letter_def(b)]
                else:    
                    letter = mydict[letter_def(i)]
            mystr+=letter   
    else:    
        letter = mydict[letter_def(i)]
        mystr+=letter    
    mylist.append(mystr)
    print(mystr)
for item in reversed(mylist[0:-1]):
    print(item)
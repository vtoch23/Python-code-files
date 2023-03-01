# Stores results of mathematical operations in two file, selects and prints the correct and incorrect ones
import os

def filter_solutions():
    dict={}
    with open("solutions.csv") as fileSolutions:
        listRows = []
        rows = []
        for row in fileSolutions:
            row = row.strip()
            word = row.split(";")
            rows.append(word)
        listRows.append(rows)
        for row in listRows:
            for item in row:
                name = item[0]
                dict[name] = item[1:]
    listCorrect = []
    listWrong = []
    for row in listRows:
        for item in row:
            name = item[0]
            result = item[2] 
            result = int(result)
            operation = item[1]
            plus = operation.find("+")
            minus = operation.find("-")
            if plus != -1:
                operation = operation.split("+")
                first = operation[0]
                first = int(first)
                second = operation[1]
                second = int(second)
                resultAdd = first+second
                if resultAdd == result:
                    sentence = ""
                    sentence = f"{name};{operation[0]}+{operation[1]};{result}"
                    listCorrect.append(sentence)
                else:
                    sentence = ""
                    sentence = f"{name};{operation[0]}+{operation[1]};{result}"
                    listWrong.append(sentence)
            if minus != -1:
                operation = operation.split("-")
                first = operation[0]
                first = int(first)
                second = operation[1]
                second = int(second)
                resultSub = first-second
                if resultSub == result:
                    sentence = ""
                    sentence = f"{name};{operation[0]}-{operation[1]};{result}"
                    listCorrect.append(sentence)
                else:
                    sentence = ""
                    sentence = f"{name};{operation[0]}-{operation[1]};{result}"
                    listWrong.append(sentence)            

    with open("correct.csv", "w") as fileCorrect:
        for item in listCorrect:
            fileCorrect.write(item+"\n")
    
    with open("incorrect.csv", "w") as fileWrong:
        for item in listWrong:
            fileWrong.write(item+"\n")       

if __name__ == "__main__":    
    solutions = filter_solutions()
    
    print("Correct: ")
    with open("correct.csv") as my_file1:
        contents = my_file1.read()
        print(contents)
    print("Incorrect: ")
    with open("incorrect.csv") as my_file2:
        contents = my_file2.read()
        print(contents)    

    os.remove("correct.csv")
    os.remove("incorrect.csv")
def read_fruits():
    with open("fruits.csv") as new_file:
        myDict = {}
        print(new_file)
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            name = parts[0]
            grades = float(parts[1])
            if name not in myDict:
                myDict[name]=[]
                myDict[name]=grades
            
    return myDict
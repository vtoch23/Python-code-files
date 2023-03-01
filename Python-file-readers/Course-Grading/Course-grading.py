if False:
    # this is never executed
    student_info = input("Please type in the file name (students1.csv or students2.csv or students3.csv or students4.csv): ")
    exercise_data = input("Exercises completed: ")
    exam_points = input("Exam points:")
    course_info = input("Course information: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_points = "exam_points1.csv"
    course_info = "course1.txt"

# Reads the student information file 
with open(student_info) as my_file:
    names = {}
    for line in my_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        if parts[0] == "id":
            continue
        names[parts[0]] = parts[1] + " " + parts[2]

# Reads the exercise data file
with open(exercise_data) as my_file:
    exercises = {}
    for line in my_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        if parts[0] == "id":
            continue
        exercises[parts[0]] = parts[1:] 
    
    sumDict = {}    
    dictExpoints = {}
    for id, value in exercises.items():
        if id in names:
            name = names[id]
        sumE = 0
        exPoints = 0
        for item in value:
            item = int(item)
            sumE+=item
            exPoints = int((sumE/40)*10)
            exPoints = int(exPoints)
            dictExpoints[name] = exPoints
            sumDict[name] = sumE
        
    points = {}

# Reads the Exam points file
with open(exam_points) as my_file:  
    for line in my_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        if parts[0] == "id":
            continue
        id = parts[0]
        if id in names:
            name = names[id]
        sumP = 0
        for i in range(1,4):
            sumP += int(parts[i])
            points[names[id]] = sumP 
dictTotal = {}
for line in exercises.items():
    id = line[0]
    if id in names:
        name = names[id]
        if name in sumDict:
            number1 = points[names[id]]
            number2 = dictExpoints[name]
            dictTotal[name] = number1+number2 
 
dictGrades = {} 
printName = "name"
printExer = "exec_nbr"
printExerP = "exec_pts."
printExmP = "exm_pts."
printTotal = "tot_pts."
printGrade = "grade"

# Reads the Course information file
with open(course_info) as read_file:
    course = ""
    credits = ""
    for line in read_file:
        line = line.replace("\n", "")
        parts = line.split(":")
        if parts[0] == "name":
            course = parts[1]
            if course[0] == " ":
                course = course[1:]
        if parts[0] == "study credits":
            credits = int(parts[1])

# Creates a new txt file  
with open ("results.txt", "w") as new_file:
    new_file.write(f"{course}, {credits} credits\n")
    new_file.write("="*38+"\n")
    new_file.write(f"{printName:<29} {printExer:<9} {printExerP:<9} {printExmP:<9} {printTotal:<9} {printGrade:<9}\n")        
 
    for name, value in dictTotal.items():
        if value >= 0 and value <=14:
            dictGrades[name] = 0    
        if value >= 15 and value <= 17:
            dictGrades[name] = 1
        if value >= 18 and value <= 20:
            dictGrades[name] = 2
        if value >= 21 and value <= 23:
            dictGrades[name] = 3
        if value >= 24 and value <= 27:
            dictGrades[name] = 4
        if value >= 28:
            dictGrades[name] = 5                   
        
        new_file.write(f"{name:<29} {sumDict[name]:<9} {dictExpoints[name]:<9} {points[name]:<9} {dictTotal[name]:<9} {dictGrades[name]:<190}\n")
        print(f"{name:<29} {sumDict[name]:<9} {dictExpoints[name]:<9} {points[name]:<9} {dictTotal[name]:<9} {dictGrades[name]:<190}\n")

# Creates a new csv file
with open ("results.csv", "w") as new_file2: 
 
    for name, valueGrade in dictGrades.items():
        for key,value in names.items():
            if name == value:
                id = key    
                new_file2.write(f"{id};{name};{valueGrade}"+"\n")
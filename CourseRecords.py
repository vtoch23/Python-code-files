from math import sqrt
class Courses:
    def __init__(self):
        self.courses = {}
        self.creditCount = 0
        self.gradeCount = 0
        self.gradeList = []
 
    def add_grade(self, course, grade: int):
        if not course in self.courses:
            self.courses[course] = Course(course)
        else:
            if self.courses[course].grade != None:
                if grade > self.courses[course].grade:    
                    old_grade = self.courses[course].grade
                    self.gradeCount -= int(old_grade)
                    self.gradeList.remove(old_grade)
                    self.gradeList.append(grade)
                    self.courses[course].grade = grade
                    self.gradeCount += int(grade)
                else:
                    pass
            elif self.courses[course].grade == None: 
                self.courses[course].grade_add(grade) 
                self.gradeList.append(grade)
                self.gradeCount += int(grade)
 
    def add_credit(self, course, credit: int):
        self.courses[course] = Course(course)
        self.creditCount += int(credit)
        self.courses[course].credit_add(credit)
        
       
    def get_entry(self, course):
        if not course in self.courses:
            return None
        return f"{self.courses[course].course} ({self.courses[course].credits} cr) grade {self.courses[course].grade}"
        
class Course:
    def __init__(self, course):
        self.course = course
        self.grade = None
        self.credits = None
        
    
    def credit_add(self, credit):
        self.credits = credit
        
        
    def grade_add(self, grade):
        self.grade = grade
    
class Application:
    def __init__(self):
        self.courseList = Courses()
        
    def square_roots(numbers: list):
        return [sqrt(number) for number in numbers]
    
    def execute(self): 
        print("1 add course")
        print("2 get course data")
        print("3 statistics") 
        print("0 exit")  
        while True:
            command = input("command: ")
            if command == "1":
                self.add_course()
        
            elif command == "2":  
                self.get_data()          
        
            elif command == "3":     
                self.statistics()    
        
            elif command == "0":     
                break   
    
    def add_course(self):
        course = input("course: ")
        grade = input("grade: ")
        credits = input("credits: ")
        if not course in self.courseList.courses:
            self.courseList.add_credit(course, credits)
        self.courseList.add_grade(course, grade)
        
        
    def get_data(self):
        searched_course = input("course: ")
        data = self.courseList.get_entry(searched_course)
        if data==None:
            print("no entry for this course")
        else:
            print(data)
            
    def statistics(self): 
        grade5 = self.courseList.gradeList.count("5")
        grade4 = self.courseList.gradeList.count("4")
        grade3 = self.courseList.gradeList.count("3")
        grade2 = self.courseList.gradeList.count("2")
        grade1 = self.courseList.gradeList.count("1")
        mean = float(self.courseList.gradeCount / len(self.courseList.courses))
        print(f"{len(self.courseList.courses)} completed courses, a total of {self.courseList.creditCount} credits" )
        print(f"mean {mean:.1f}")
        print("grade distribution") 
        print("5: "+ "x"*grade5)
        print("4: "+ "x"*grade4)
        print("3: "+ "x"*grade3)
        print("2: "+ "x"*grade2)
        print("1: "+ "x"*grade1)    
 
course = Application()
course.execute()
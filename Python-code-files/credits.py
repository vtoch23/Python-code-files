from functools import reduce
 
class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits
 
    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"
 
def balance_sum_helper(sum, attempt):
    return sum + attempt.credits
 
def sum_of_all_credits(attempts):
    sum_of_credits = reduce(balance_sum_helper, attempts, 0)
    return sum_of_credits
 
def sum_of_passed_credits(attempts):
    passed = filter(lambda x: x.grade >= 1, attempts)
    sum_of_credits = reduce(balance_sum_helper, passed, 0)
    return sum_of_credits
 
def average(attempts):
    list = []
    passed = filter(lambda x: x.grade >= 1, attempts)
    for item in passed:
        list.append(item.grade)
    sum = reduce(lambda product, item: product + item, list)
    aver = sum / len(list)
    return aver
    
if __name__ == "__main__":
    course1 = input("Please enter first course name: ")
    course2 = input("Please enter second course name: ")
    course3 = input("Please enter third course name: ")
    grade1 = int(input("Please enter a grade for the first course: "))
    grade2 = int(input("Please enter a grade for the second course: "))
    grade3 = int(input("Please enter a grade for the third course: "))
    credits1 = int(input("Please enter credits for the first course: "))
    credits2 = int(input("Please enter credits for the second course: "))
    credits3 = int(input("Please enter credits for the third course: "))
    s1 = CourseAttempt(course1, grade1, credits1)
    s2 = CourseAttempt(course2, grade2, credits2)
    s3 = CourseAttempt(course3, grade3, credits3)
    ag = average([s1, s2, s3])
    totalcr=sum_of_passed_credits([s1, s2, s3])
    print(f"Average grade: {ag}")
    print(f"Total passed credits: {totalcr}")
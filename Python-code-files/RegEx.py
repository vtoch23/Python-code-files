import re
 
def is_dotw(my_string: str):
    expression = "Mon|Tue|Wed|Thu|Fri|Sat|Sun"
    if re.search(expression, my_string):
        return True
    else:
        return False
 
def all_vowels(my_string: str):
    expression = "[bcdfghjklmnpqrstvwxyz]"
    if re.search(expression, my_string):
        return False
    else:
        return True
def time_of_day(my_string: str):
    expression = "^([01]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$";
    if re.match(expression, my_string):
        return True
    else:
        return False
 
 
if __name__ == "__main__":
    print(time_of_day("12:43:01"))
    print(time_of_day("AB:01:CD"))
    print(time_of_day("17:59:59"))
    print(time_of_day("33:66:77"))
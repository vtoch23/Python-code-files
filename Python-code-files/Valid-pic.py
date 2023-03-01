from datetime import datetime
 
def is_it_valid(pic: str):
    
    list23 = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    
    if len(pic) == 11:        
        birthday = pic[0:6]
        day = birthday[0:2]
        day = int(day)
        month = birthday[2:4]
        month = int(month)
        year = birthday[4:]
        century = pic[6]
        personal_id = pic[7:10]
        control = pic[10] 
        result23 = birthday + personal_id
        result = int(result23)/31
        result = str(result)
        dot = result.find(".")
        left = result[0:dot]
        left = "0"
        parts2 = left+result[dot:]
        number = float(parts2)
        identifier = round(number*31) 
        
        if check_day(day, month, year, century) and check_month(month) and check_century(century) and check_control(list23, control, identifier):
            return True
        else:
            return False
    else:
        return False 
    
    return True
def leap_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
    elif year % 4 == 0:
        return True
    return False
 
def check_day(day, month, year, century):
    months31 = [1, 0o1, 3, 0o3, 5, 0o5, 7, 0o7, 8, 10, 12]
    months30 = [4, 0o4, 6, 0o6, 9, 11]
     
    if century == "-":
        year = "19"+year
    elif century == "+":
        year = "18" + year
    elif century == "A":
        year = "20"+year
    year = int(year)    
    if leap_year(year) == True and month == 2:
        return day > 0 and day <= 29
 
    elif leap_year(year) == False and month == 2:
        if month == 2:
            return day > 0 and day <= 28
    elif month in months31 or month == 8:
        return day > 0 and day <= 31
    elif month in months30 or month == 9:
        return day > 0 and day <= 30    
def check_month(month):
    return month > 0 and month <= 12
def check_century(century):
    return century == "+" or century == "-" or century == "A"
def check_control(list, control, identifier):
    control_character = list[identifier]
    return control_character == control
def check_year(year):
    return year > 0
 
 
if __name__ == "__main__":
    pic = input("Enter PIC: ")
    print(is_it_valid(pic))
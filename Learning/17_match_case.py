# Match-case-statements (switch ): An alternative to using many 'elif' statements
#                               Execute some code if value matches a 'case'
#                               Benifits: cleaner and syntax is more readable.

""" def day_of_Week(day):
    if day == 1:
        return "It is sunday"
    elif day == 2:
        return "It is monday"
    elif day == 3:
        return "It is tuesday"
    elif day == 4:
        return "It is wednesday"
    elif day == 5:
        return "It is thursday"
    elif day == 6:
        return "It is friday"
    elif day == 7:
        return "It is saturday"
    else:
        return "Not a valid day"
    
print(day_of_Week(9)) """

#using match-case:

""" def day_of_Week(day):
    match day:
        case 1:
            return "It is sunday"
        case 2:
            return "It is monday"
        case 3:
            return "It is tuesday"
        case 4:
            return "It is wednesday"
        case 5:
            return "It is thursday"
        case 6:
            return "It is friday"
        case 7:
            return "It is saturday"
        case _:
            return "Not a valid day"
        
print(day_of_Week(4)) """

# weekend Example:

""" def is_weekend(day):
    match day:
        case "sunday":
            return True
        case "monday":
            return False
        case "tuesday":
            return False
        case "wednesday":
            return False
        case "Thursday":
            return False
        case "Friday":
            return False
        case "saturday":
            return True
        case _:
            return False
print(is_weekend("monday")) """

# using OR statement:


""" def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday"| "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False
print(is_weekend("Monday")) """

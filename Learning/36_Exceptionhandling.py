# Exception : An event that interrupts the flow of program
#            (Zerodivision error, Type error, Value error)
#             1.Try, 2.Except, 3.Finally

try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can't divide by zero")

except ValueError:
    print("Enter only numbers please!")

except Exception:
    print("Something went wrong")

finally:
    print("Do some clean up here")
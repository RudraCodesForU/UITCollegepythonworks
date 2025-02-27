#Handling_an_exception
num=int(input("Enter the numerator :"))
deno=int(input("Enter the denominator :"))
try:
    quo=num/deno
    print("Quotient:",quo)
except ZeroDivisionError:
 print("Denominator can't be zero")



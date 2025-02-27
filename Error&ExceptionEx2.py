#Handling_an_exception

try:
    num=int(input("Enter the number :"))
    print(num**2)
    
except (KeyboardInterrupt,ValueError,TypeError):
 print("Pls Check before you enter.......Program Terminating")

print("Bye")



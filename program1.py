print("Hai", end="")
print("Aspirants")
r=200
print(r)
print("{0} are {1}!".format("YOU","ASPIRANTS",r))
print(type(r))
s="corona"
print(type(s))
s='C'
print(type(s))
a=10
b=3
print(a**b)
print(a%b)
print(a//b)
print(a/b)
#bitwise operators
## or operator
a=2
b=3
print(a|b)
## and gate
a=2
b=3
print(a&b)
##swap 
a=1
b=2
temp=a
a=b
b=temp
print(a,b)
##swap without temp using xor
a=2
b=3
a=a^b
b=a^b
a=a^b
print(a,b)
##bitwise shift 
a=4
b=a>>2
c=a<<2
print(b,c)
## compliment's
print(~10)
##logical operators
a=0
b=1
print(a and b)
print(a or b)
print(not b)
print(not a)
a=12
b=23
print(type(b))
print(a>b and b<a)
## Membership Operator 
## "in" TRUE if a value/sequence
print("t" in 'Aspirant')
print( 'k' not in 'yup')
x=5.123467890
print(type(x) is float)
print(type(89) is not type("haiii"))
print(type("hai") is type('a'))
## Precedence in python
print(5**(1+2))
## Control Statemments
a=20
b=50
if (a>b):
    print("a is bigger")
else:
    print("b is bigger")
##loops
y=11
for i in range(1,y):
    print(i)
c=int(input("Enter the value \n")) 
print(type(c))
##assignment password making with username
print("WELCOME TO SBI\n\nPlease insert your card. ")
password=1987
choice=0
Amount=0
Money=0
for i in range(3):
 pin=int(input("Enter your four digit pin"))
 if pin==password:
    print("pin confirmed!")
    print("WHAT DO YOU WANT TO DO ?")
    print("1==Balance")
    print("2==Deposit")
    print("3==Withdraw")
    print("4==Cancel")
    break
 else:
    print("PIN INCORRECT!!!!\n\nPlease Retry.")
    if i==2:
       print("Transaction Cancelled,RETRY!!")
       exit()
choice=int(input("Kindly select your chocee\n"))
if choice==1:
   print("Your Current Balance is 10000 rupees.")
elif choice==2:
    print("Enter the amount you want to deposit")
    Amount=int(input("amount ->"))
    b=10000+Amount
    print("THANK YOU For Your Transaction\nyour current balance is\n")
    print(b)
elif choice==3:
    print("Enter the amount you want to withdraw")
    Money=int(input("amount to withdraw ->"))
    c=10000-Money
    print("THANK YOU For Your Transaction\nyour current balance is\n")
    print(c)
elif choice==4:
   print("TRASACTION COMPLETED\n\nYOU CAN REMOVE THE CARD")
   

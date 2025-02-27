
'''num = int(input("Enter the numerator"))
##deno = int(input("Enter the denominator"))
##try:
  #  quo = num/deno
   # print("Quotient",quo)
#except ZeroDivisionError:
 #    print("Denominator can not be zero")'''

'''try:
    num = int(input("Enter the numerator"))
    print(num**2)
except (KeyboardInterrupt,ValueError,TypeError):
    print("PLS check before you enter....Prog Terminating")

print("BYE")'''
def ispalindrome(num):
    num_str = str(num)
    num_required = reversed(num_str)
    print(num_required)
    return(num_required==num)
n=int(input("Enter NO:"))
if ispalindrome(n):
    print("palindrome number")
else:
    print("not palindrome number")
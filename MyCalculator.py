# Calculator program
# The loop variable tells the while loop wether it should loop or not.
# 1 means loop. Anything else means don't loop.

def main():
    loop = 1
    choice = 0
    while loop == 1:
        print(' ')
        print("Welcome to the calculator program")
        print('Your options are: ')
        print()
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Exponents")
        print("6.Square Root")
        # Uncoded
        # print("7.Remainder")
        # print("8.Factorial")
        print("9.Quit the Calculator")
        print()

        choice = int(input('Choose your option: '))
        if choice == 1:
            add1=int(input("Add this: "))
            add2=int(input("to this: "))
            print(add1, "+", add2, "=", addit(add1, add2))
        elif choice == 2:
            sub2=int(input("Subtract this: "))
            sub1=int(input("from this: "))
            print(sub1, "-", sub2, "=", subit(sub1,sub2))
        elif choice == 3:
            mul1=int(input("Multiply this: "))
            mul2=int(input("with this: "))
            print(mul1, "*", mul2, "=", multiply(mul1,mul2))
            
        elif choice == 4:    
            div1=int(input("Divide this: "))
            div2=int(input("by this: "))
            
            # Can't divide by zero
            if div2==0:
                print('You cannot divide by zero.')
                print('The solution does not exist.')
            else:
                print(div1, "/", div2, "=", division(div1,div2))               
            
        elif choice == 5:
            exp1=int(input("Raise this: "))
            exp2=int(input("to this: "))
            print(exp1, "^", exp2, "=", exponential(exp1,exp2))

        elif choice == 6:
            squ1=int(input("Sguare root of: "))
            squ2=.5

            # Can't divide by a negative
            if squ1<=0:
                print('You cannot take the root of a negative.')
                print('It will result in an unreal result.')
            else:
                print('The Square root of', squ1, "=", square(squ1,squ2))

        elif choice == 9:

            #Sentinal Value to end
            loop = 0
            test=input()

def addit(a,b):
    return a+b
def subit(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
def exponential(a,b):
    return a**b
def square(a,b):
    return a**b




main()

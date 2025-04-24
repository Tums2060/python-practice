#2. Check if a number is even or odd

#MY LOGIC

#even numbers are those that are divisible by 2
#But i can't directly say if number is divisible by 2 it is odd, in code

#Although by use of modulus, i can say, if the remainder of a number,
#  when divided by 2 is 0, then it is even



def checker():
    #getting input from the user
    number = int(input("Enter number: "))

    #use of % to check if remainder is 0 or not
    if(number % 2 == 0):
        print(f"{number} is even")
    
    else:
        print(f"{number} is odd")
    
#calling the function
checker()
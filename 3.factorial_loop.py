#3 Compute factorial using a loop

#MY LOGIC

#factorial involves having a number n, and multiplying it by n-1
# consecutively until n=1

#i thought my loop to be like, range(start, stop, step)



def factorial():
    #input number
    number = int(input("Enter number to get is factorial: "))

    #constant to hold the  values of factorial, initially equal to 1
    constant = 1

    #It is not possible to get factorial of negative numbers
    if (number < 0):
        print("Enter a valid number")

    else:
        #range (start, stop, step)
        #start- we are starting from the number inputted
        #step- we are subtracting 1 i.e. (-1) and going downwards, from n*(n-1)...
        #stop- we stop calculation the moment i = 0 to avoid making whole thing 0

        for i in range(number, 0, -1):
            #e.g if number inputted was 2, we start with constant(1) = 1*2(i)
            #then i-1(2-1=1) then constant would be 2*1
            constant = constant*i
        print(f"The factorial of {number}: {constant}")

#calling the function    
factorial()
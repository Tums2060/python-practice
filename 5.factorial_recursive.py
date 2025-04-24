#5. Factorial (Recursive)

#Logic remained the same, but since recursion involves
#  a function calling itself i thought to create a function for inputting and another for computing

#function 1 factorial() enabled getting of the input and printing out the final result

#function 2 compute(n) is recursive in that it calls itself to multiply all
#   numbers consecutively down to 1


def factorial():
    #getting input
    number = int(input("Enter number for its factorial: "))

    def compute(n):
        #because 1! and 0! is always 1
        if n == 1 or n == 0:
            return 1
    
        else:   
            #this continues multiplying n by its value minus 1 until n = 1
            return n*compute(n-1)

    #Here i am passing what was inputted from the factorial() into the compute() to get a result  

    result = compute(number)
    print(f"Factorial of {number} is: {result}")

#calling the function 
factorial()

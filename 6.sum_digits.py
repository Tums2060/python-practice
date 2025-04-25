#6. Sum digits of a number

#--I assumed that this meant you can input 12 and get 3

#At first i thought of a list, but i realised elements are separated by comma

#But the question does't mean you put 10 and 10 then get 20
#it means if you put 10, you get 1

#MY LOGIC


#My first try;
# def sum_digits():
    
#     digits = int(input("Enter a number and get sum of its digits: "))

#     list_digits =[digits]

#     total = sum(list_digits)

#     print(total)

# sum_digits() ##I noticed when this function was called and i put 1 & 2 i got 12, instead of 3



    #The same case was for this code below;
# i = int(input("Enter elements: "))
# numbers = [i]
# total = 0

# for number in numbers:
#     total += number
# print(total)

#BREAKTHROUGH;
def sum_digits():
    numbers = input("Enter number do get sum of its digits: ")
    
    #since input() takes as string, i used map(int, ) to convert each input to an integer
    #i realised list() works like a convetional list i.e. [] and it is more flexible so i used it

    digits = list(map(int, numbers))

    #after converting the elements to a list, i used the sum() function to get the sum of each element

    total = sum(digits)
    print(total)
#calling the function
sum_digits()

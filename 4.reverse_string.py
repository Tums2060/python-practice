#4. Reverse a string(without using [::1] or built-in method)

#I first thought of seeing how an actual reverse function works
txt = "Hello World"[::-1]
print(txt)

#IMPLIMENTATION

#MY LOGIC
# i think to reverse say abc, i create an empty string variable
#then i loop through, so from below;
#for loop starts with the first character + reverse, so "a"+"" which is "a"

#second letter is "b" and since variable reverse in now equal to "a" and i am currently on character "b"
#new reverse becomes "b"+"a" therefore "ba"
#so on so forth
def reverse_string():
    sentence = input("Enter string to be reversed: ")
    #the empty string variable
    reverse = ""

    for character in sentence:
        #looping through each character from the first and adding the current character in the loop to the left of the previous character
        
        reverse = character + reverse

    print(reverse)

reverse_string()
    
# Program that uses a For Loop to display 15 numbers in order and
# determines if the number is even or odd. Then displays the
# result along side the number.

# Kenneth Seiler
# SDEV120
# Module 7 Assignment - Python using loops
# 12/01/2024

#Declare Variables
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#For Loop to output numbers in order 
for count in numbers:
    # If statement to determine if the number is even or odd
    # then display the result
    if (count % 2 == 0):
        # Convert even numbers into a string and print with another string
         print(str(count),"- the number is even")
    else:
        # Convert odd numbers into a string and print with another string
        print(str(count), "- the number is odd")

#enter the largest_number
largest_number = -999999999

#user inputs a number
number = int(input("enter a number or -1 to stop"))

#is users input the largest number
while number != -1:
    
    if number > largest_number:
        largest_number = number
        
    number = int(input("enter a number or -1 to stop :"))
    
print("the largest number is: ",largest_number)
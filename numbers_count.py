odd_numbers = 0
even_numbers = 0

number = int(input("enter a nmber or 0 to exit: "))

while number != 0 :
    
    if number % 2:
        odd_numbers += 1
        
    else:
        even_numbers += 1
    
    
    number = int(input("enter a number or 0 to exit: "))
    
print("count of odd numbers is: ",odd_numbers)
print("count of even numbers is: ",even_numbers)
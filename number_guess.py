print("###" * 15)
print("WELCOME TO THE NNUMBER GUESSING GAME")
print("###" * 15)

secret_number = 57


print ("Guess a number between 1-100.")
print ()
number = int(input("Guess the secret number: "))

total = 0
while number != secret_number:    
   total += 1
   try:
       
    number = int(input("Guess the secret number: "))

    if number > secret_number:
       
       print ("value greater than secret number.\n")
    elif number < secret_number:   
        print ("value less than secret number.\n")
    else:
       print ("That's the value\n")
   except:
      print ("No such kind of number.") 
else: 
    print ("Number found.")    

print ("Total number of tries: ",total)
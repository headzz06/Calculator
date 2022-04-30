numberOne = float(input("Enter the first number ")) #gets the input for first number
operator = input("Enter the operator ") #gets input for the operator
numberTwo = float(input("Enter the second number ")) #gets input for second number

if operator == "+":
    #add numbers
    answer = numberOne+numberTwo

elif operator == "-":
    #subtract numbers
    answer = numberOne-numberTwo

elif operator == "/":
    #divide numbers
    answer = numberOne/numberTwo

elif operator == "*":
    #multiply numbers
    answer = numberOne*numberTwo

else:
    exit("Invalid operator") #if anything other than the listed operaters is used, it will close the program

if answer%2 == 0:
    print(int(answer))  #if the operator is a whole number, print it as an int instead of float

else:
    print(answer)

name = input("What is your name?")
num1 = int(input("Enter a number"))
num2 = int(input("Enter a second number"))
asmd = input("Would you like to add, subtract, multiply, or divide the two number?" + '\n' + "Type '+' for addition, '-' for subtraction, '*' for multiplication, or '/' for division")
result = input
guess = float(input("What do you think the answer is? (to the nearest 2 decimal places)"))
      
if asmd == '+':
    result = num1 + num2
elif asmd == '-':
    result = num1 - num2
elif asmd == '*':
    result = num1 * num2
elif asmd == '/':
    result = num1 / num2

line1 = 'Thanks ' + name + "."
line2 = 'The first number you entered was ' + str(num1) + '.'
line3 = 'The second number you entered was ' + str(num2) + '.'
line4 = str(num1) + asmd + str(num2)

output = line1 + '\n' +  line2 + '\n' + line3 + '\n' + line4 +' = '+ str(round(result, 2)) + '\n'

print(output)

difference = result - guess

##allow for .05 margin of error
if difference <= .05:
    print("WOOHOO you were right!")
else:
    print("Better luck next time!")


    


#intro explainer and get first number
print('Hello!')
print('I will help you add numbers.')


num1 = input('What is your first number? ')
if num1.isdigit():
    num1 = int(num1)
else:
    print('That was not a number. Goodbye!')
    quit()


#get second number
num2 = input('What is your second number? ')
if num2.isdigit():
    num2 = int(num2)
else:
    print('That was not a number. Goodbye!')
    quit()

#add and print result
total_sum = num1 + num2
print(num1, '+', num2, '=', total_sum)


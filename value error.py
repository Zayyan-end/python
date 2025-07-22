try:
    number=int(input('Enter a number: '))
    print('The number entered is', number)
except ValueError as ex:
    print('Exception: ',ex)


try:
    num1,num2=eval(input('Enter two numbers,seperate by a coma: '))
    result=num1/num2
    print('Result is', result)
except ZeroDivisionError:
    print('Division by zero s error!!')
except SyntaxError:
    print('comma is missing. Enter number seperated by a comma like this, 1,2')
except:
    print('Wrong input')
else:
    print('No exceptions')
finally:
    print('This will execute no matter what')



valid=False
while not valid:
    try:
        n=int(input('Enter a number: '))
        while n%2==0:
            print('Bye')
        valid=True
    except ValueError:
        print('invalid')

        
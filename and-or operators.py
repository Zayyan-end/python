a=10
b=12
c=0
if a and b and c:
    print('All the numbers have boolean value of True')
else:
    print('Atleast one number has boolean value of False')


a=10
b=-10
c=0

if a > 0 or b > 0:
    print('Either of the number is greater than 0')

else:
    print('no number is greater than 0')

if b > 0 or c > 0:
    print('Either of the number is greater than 0')

else:
    print('no number is greater than 0')


a=10
b=12
c=12
print(a!= b)
print(b==c)
 
a='python'
b='coding'
if a!=b:
    print(a,'and',b,'are different')



a=int(input('enter a number'))
if a%2 !=0:
    print('your number is not even')
else:
    print('your number is even')

height=float(input('enter your hight in cm'))
weight=float(input('enter your weightin kg'))

BMI = weight / (height/100)**2
print('your BMI is: ' , BMI)
if BMI <= 18.4:
    print('You are Under weight')
elif BMI<= 24.9:
    print('you are healthy')
elif BMI <= 29.9:
    print('You are slightly over weight')
elif BMI <= 34.9:
    print('You are severley over weight')
elif BMI <= 39.9:
    print('You are obese')
else:
    print('You are severely obese')
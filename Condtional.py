num = 34

if num > 0:
    print(num,'is a positive number')
num = -1
if num > 0:
    print(num,'is a positive number')
else:
    print(num,'is a negitive number')


pa=int(input('enter purchase amount'))
sa=int(input('enter sale amount'))
if sa > pa:
    profit=sa-pa
    print('total profit is:',profit)

else:
    print(' you have no profit.')


i=int(input('enter a number'))
if(i < 15):
    print('i is smaller than 15')
    print('im in if Block')
else:
    print('i is greater than 15')
    print('im in else Block')
print('im not in in if and not in else block')


number= int(input('enter number'))
if number%2==0:
    print('this is an even number')
else:
    print('this is an odd number')
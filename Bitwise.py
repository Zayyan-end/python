x=5
if (type(x)is int):
    print('True')
else:
    print('False')

x=5.5
if (type(x)is float):
    print('True')
else:
    print('False')


a=10
b=-10
print('a>>1=', a>>1)
print('b>>1=', b>>1)
a=5
b=-10
print('a<<1=', a<<1)
print('b<<1=', b<<1)


print('Enter marks obtained of 5 subjects')
m1=int(input())
m2=int(input())
m3=int(input())
m4=int(input())
m5=int(input())

sum=m1+m2+m3+m4+m5
avg=sum/5
if avg>=91 and avg<= 100:
    print('Your Grade Is A1')
elif avg>=81 and avg<= 91:
    print('Your Grade Is A2')
elif avg>=71 and avg<= 81:
    print('Your Grade Is B1')
elif avg>=61 and avg<= 71:
    print('Your Grade Is B2')
elif avg>=51 and avg<= 61:
    print('Your Grade Is C1')
elif avg>=41 and avg<= 51:
    print('Your Grade Is C2')
elif avg>=33 and avg<= 41:
    print('Your Grade Is D')
elif avg>=21 and avg<33:
    print('Your Grade Is E1')
elif avg>=0 and avg<21:
    print('Your Grade Is E2')
else:
    print('invalid input')







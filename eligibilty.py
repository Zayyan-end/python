medical_cause=input('did you have a medical cause Y or N: ')
atten=int(input('Enter the attendance of the student: '))
if medical_cause=='Y':
    print('You are allowed.')
else:
    if atten >= 75:
      print('allowed.')
    else:
       print('not allowed')

units=int(input('Please enter amount of units consumed: '))
if (units<50) :
   amount=units * 2.60
   surcharge=25
elif (units<= 100) :
   amount= 130+162.50+((units-50)* 5.26)
   surcharge=45
amount=130+162.50+526+((units-200)* 8.45)
surcharge=75
total= amount+surcharge
print('\n Electricity bills=%.2f' %total)
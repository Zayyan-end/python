student_data = {'id1':
    {'name': ['Sara'],
     'class': ['V'],
    'subject_intergration': ['english,math,science']
    },



'id2':
{'name': ['David'],
     'class': ['V'],
    'subject_intergration': ['english,math,science']
    },
 'id3':
{'name': ['Sara'],
     'class': ['V'],
    'subject_intergration': ['english,math,science']
    },
'id4':
{'name': ['Surya'],
     'class': ['V'],
    'subject_intergration': ['english,math,science']
    },

}

result = {}
for key,value in student_data.items():
    if value not in result.values():
        result[key]= value

print(result)



test_dict={'codingal' : 2,'is' : 2, 'best' : 2, 'for' :2, 'coding' : 1}
print('The original dictionary: ' + str(test_dict))

K=2

res = 0
for key in test_dict:
    if test_dict[key] == K:
        res=res+1
print ('Frequency of K is :' +str(res))




country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}



print('Country code for India -')
print(country_code.get('India', 'not found'))



print('Country code for Japan -')
print(country_code.get('Japan', 'not found'))
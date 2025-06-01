tree1=98
tree2=94
tree3=41
tree4=95
tree5=11
sum=tree1+tree2+tree3+tree4+tree5
print('The sum all 5 of the trees is:' ,sum)
average=sum/5
print('The average of all 5 trees is:' , average)

amount=int(input('please enter the amount you want to withraw'))
note_1=amount //100
note_2=(amount %100)//50
note_3=((amount %100)%50)//10
print('Notes of hundred rupees:' ,note_1)
print('Notes of 50 rupees:' ,note_2)
print('Notes of 10 rupees:' ,note_3)

print('Marks in maths,english,science and Hindi')
Maths=int(input("Maths :"))
English=int(input("English :"))
Science=int(input("Science :"))
Hindi=int(input("Hindi :"))
sum = Maths + English + Science + Hindi
pr=(sum/400)*100
print('the percentage is:' ,pr)
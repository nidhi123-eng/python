#lists & tuples

'''
#list 
marks=[12,23.4,43,54.5]
print(marks)
print(len(marks))
print(type(marks))
print(marks[3])

student=["nidhi",123,8.38,"msc ai & ml"]
print(student[0])
student[0]="vidhi"
print(student)

#list methods
list=["apple","orange","banana","grapes"]
#print(list.append(3))
#print(list.sort())
#print(list.sort(reverse=True))
#print(list.reverse())
#list.pop(3)
#list.remove("banana")
#list.index(2,"banana")
print(list)

#tuples
#same as lists

#practise
#WAP to ask the user to enter names of their 3 fav movies & store them in list
movies=["jab we met","vivah","hum sath sath hain"]
str=input("enter your fav movie:")
movies.append(str)
print(movies)

#WAP to check if a list contains a palindrome of elements.(hint : use copy() method)
list1=[1,2,3,4,3,2,1]
list2=[1,2,3]
copy_list1 =list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print("list is palindrome")
else:
    print("list is not palindrome")

#WAP to count the number  of students with the "A" grade in the following list.tuple.
grades=["A","B","A","B","A","C","A","B","A"]
count=grades.count("A")
print("number of students with A grade is:",count)

#stores the above values in a list & sort them form "A" to "D".
grade=["A","B","A","B","A","C","A","B","A"]
grade.sort()
print(grade)
'''


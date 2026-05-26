student={   #creating dictionary
    'name':'purnima',
    'role':'intern'
}
print(student)
student={   #creating dictionary
    'name':'purnima',
    'role':'intern',
    'name':'ramya',
    'age':20
}
print(student) #replacing the name
print(student['age'])  #to get particular Index
print(student.get('name'))#for indexing
print(student.keys())#all keys in a list ->.keys()
print(student.items())#all items in a list->items()
print(student.values())#all values in a list->values()
student['clg']='MJR' #add new key-value pair
print(student)
student['age']=19  #modify value
print(student)
student.pop('age')#remove element
print(student)
student.update({'role number':12})#it will add in the dictionary if not present
print(student)
skills={'language':'python'}
print(skills.clear())#clear entire dictionary
#loop keys
for key in student: #loop through dictionary
    print(key)
    #loop values
    for value in student.values():
        print(value)
        print('name'in student)#checking existence
        print(len(student))#finding length
        new_student=student.copy  #copy dictionary
        print(new_student)  #nested dictionary
        p={'A1':{'name':'purnima'},
           'A2':{'age':20}
        }
        print(p)
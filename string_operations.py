name='purnima'
print(name[0])#indexing
print(name.index('a'))#finding index of character
len(name)#length of ab string
print(name+'manda')#append->add one or more elements
#print(name+'manda',sep='%')#error->one variable and one string function
#name.append('yadav')#attribute error
#name.extend('student')#no extend operator in string
print(name.upper())#uppercase letters
print(name.lower())#lowercase letters
print(name.title())#title
print(name.capitalize())#capitalize the first letter
print(name.strip())#remove white spaces before and after
print(name.lstrip())#remove left side whitespaces
print(name.rstrip())#remove whitespaces on right side
name.split(',')
print(name)
name.split()
print(name.count('manda'))#count no.of occurrences
print(name.startswith('manda'))
print(name.endswith('manda'))
skills=('python is backend language')
age='20'
print(skills.join(age))#to join the elements with special characters


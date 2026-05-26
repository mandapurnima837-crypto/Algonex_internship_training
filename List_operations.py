numbers=[10,20,30,40,50]
names=['gothami','ramya','purnima']
skills=['python','SQL','AI']
print(skills[0])#positive indexing
print(skills[-2])#negative indexing
print(numbers[0:4:1])#stop=stop-1
print(numbers[1:])#starts from 1 index to entire string
print(numbers[:1])#execute until last string
print(numbers[::2])#jump by 2 numbers
print(numbers[1:5:-1])
skills=['python','SQL','AI']
skills[1]='Git'  #modify the element at particular index
print(skills)
skills.append('power BI')#adding elements
print (skills)
print(numbers.extend(names))#combines list
skills.insert(1,"Fast API")#inserting elements
print(skills)
result=skills+numbers+names #concatinating list
print(result)
skills.remove('AI')#removing particular element
print(skills)
skills.pop()#removing last element
del skills[0]#deleting element at particular index
print(skills)
skills.clear()#clear entire list
print(skills)
print(len(names))#length of list elements
print('gowthami'in names)#check existence
print(numbers.count(1))#count no.of occurrences
print(names.index('ramya'))#finding index
numbers=[10,20,30,40,50]
numbers.sort()#ascending order default
numbers[::-1]#reverse list
new_list=numbers.copy()#copy list
print(new_list)
skills=['python''SQL''AI']# loop through list
for i in skills:
     print(i)
skills=['pyton''SQL''AI']#loop with index
for i in range(len(skills)):
     print(i,skills[i])
numbers=[1,2,3,4,5]
squares=[X*X for X in numbers]
print(squares)
student=[['gowthami',20],['ramya',19]]#nested list
print(student[0][0])#0 index in 0th index
print(student[0][-1])
for S in student:   #loop through nested list
     print(S)
for S in student:#nested loop
     for value in student:
          print(value)
names=['gowthami''ramya']
roles=['AI','python']
for n,r in zip(names,roles):
     print(n,r)  #combines list together
numbers=[10,20,30,40,50]
print(max(numbers))#maximum number in the list
print(min(numbers))#minimum number in the list
print(sum(numbers))#adds the total
print(numbers*2)#multiply the list
skills=['python','SQL','AI']
print(','.join(skills))


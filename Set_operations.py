name={'gowthami','purnima','ramya','gowthami'}
name.add('anjali')#add elementto the set
print(name)#removes duplicate values and result the unique values
name.update(['durga','ramana'])#adding multiple values->update()
print(name)
name.remove('anjali')#removing particular element->.remove(
print(name)   #if item is not present erroe occurs
name.discard('durga')#safe remove->discard()
print(name)#no error found if item is not there in the set
name.pop()#since sets are unordered random element is removed->pop(
print(name)
skills={'python','SQL','AI'}
skills.clear()  #deleting the entire set->.clear()
print(skills)
print('gowthami'in name)#checking the existence
 #MATHEMATICAL OPERATIONS IN SETS
name={'gowthami','purnima','ramya','gowthami'}
skills={'python','SQL','AI'}
print(name|skills) #UNION()-> combine all unique values
print(name.union(skills))
print(name&skills)# intersection()->common values only
print(name.intersection(skills))
print(name-skills) #names values present in the first set but not in the second set
print(skills-name)
print(name^skills) #symmetric difference(^) values that are not common in sets
print(name.issubset(skills))#SUBSET->true if first set exist in second one
print(skills.issubset(name) )
print(skills.issuperset(name))#superset
print(name.isdisjoint(skills))#disjoint->no common elements



student_skills=set(input("enter your skills:").split())
job_skills={'python','SQL','Git'}
matched=student_skills&job_skills
missing=job_skills-student_skills
print(matched)
print(missing)

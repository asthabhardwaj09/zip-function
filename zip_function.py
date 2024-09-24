# #set data type
# #unordered collection of unique items

s={1,2,3,4,5,6,7,8,9,10,2,2,3,4}
# print(s[1]) it will through an error
#it removes duplicate
s2=[1,2,3,4,5,6,7,7,8,9] 
s3=list(set(s2)) #it will first convert into set than in list and this is how we can remove duplicate from list
# # s2=dict(set(s))#set cannot convert into dictionary
print(s3)
s.add(11)
s.remove(1)
#s.remove(12) #it will through an error
s.discard(12)
#s.clear()
s1=s.copy()

print(s1)
print(s)
s2={1,1.1,2.3,'string'}
# s2={1,1.1,2.3,'string',[1],{1:1}}
#set do not contain tuple and dictionary
print(s2)


'''more about set'''

#in keyword in set and for loop

s={'a','b','c'}
#in keyword to check if item is present or not in set
if'a' in s:
    print("present")
else:
    print("not present")
    
#for loop
for item in s:
    print(item)
    
#set math
s1={1,2,3,4}
s2={3,4,5,6}

#union
#intersection
union_set=s1|s2    #   | (pipe)
print(union_set)
print(s1&s2)
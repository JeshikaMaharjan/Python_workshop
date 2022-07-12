#Datatypes in python

#List
mylist = ['name', 23, False, [1,2], []] #list is collection of anything. ( here,[] means empty list. yo ni halna milxa )
print(mylist[0]) #index is same as in array
print(mylist[3])
print(type(mylist[0]))

#Update
mylist[0] = "jess" 
mylist[3][0] = 5 #list vitra ko list update garna (first ma main list o index then vitra wala list ko index  )
print(mylist)

#Delete
mylist.pop(2) #pops according to index
mylist.clear() # clears the whole list
del mylist #deletes the list from memory as well


nextList = mylist[3] #esma nextList ko lai naya memory allocate hudaina
nextList.append(3) # yo garda mylist ma nii change auxa cuz heap ma store hunxa list  and [1,2] vanera rakheko thau ma actually reference or address hunxa
#nextList ma ni hamile same position ko address store gariraxa
print(nextList)                       
print(mylist)  # (saav address ma kaam hune vaera euta thau ko change arko ma ni auxa)

mylist.append('ftft') #append garda last ma add hunxa
mylist.insert(2,'ftft') #insert garda index diyera garne
print(mylist)

#--------------------------------------

#Primitive datatypes are immutable (unchanging over time or unable to be changed.)
#Non primitive are mutable.
#Every datatype is an object.

#--------------------------------------
#dictionary- curly braces
#list - square brackets

#Dictionary
#Syntax: variable = {key:value}

staff = {"name":"Ram", 
            "is_married":True,
            "children": ['Jenny', 'Rob'],
            "dob":{ "year":2000, 'month':'Feb', 'day':12}
        } #Dictionary vitra list or another dictionary pani rakhna milxa.

print(staff["name"]) #using key to access values. square brackets to access 


# #Update values
staff["name"]='Sita' #Key diyera update garne
staff["dob"]["year"] = 3000
staff["is_married"] = False
print(staff)

print(staff.items())  #[prints  (key,value)]
print(staff.values()) #[prints values only]
print(staff.keys()) #[ prints keys only]

staff.pop("children") #key as argument liyera remove gardinxa #last item pop hunxa vanne hudaina as in stack 
print(staff.items())

#--------------------------------------

#Tuples - small brackets
#Tuples values are unchangable. dictionary 

myTuple = (1,2,3)
myTuple[3] = 9 #error hanca (tuples are unchangable)

#--------------------------------------

#Set
#esma repeated values print hudaina. set is also a list

mySet = {1,1,2,2,4}
print(mySet)
#--------------------------------------

#Sorting

numbers = [2,3,56,78,1,0]
print("Normal" , numbers)

print("Sorted numbers:" , sorted(numbers)) # esma sorted(numbers) le original data lai hamper gardaina 
print("Normal", numbers)

numbers.sort()
print("Numbers.sort(): ", numbers)

numbers.sort(reverse = True) #descending order ma sort hunxa
print("Reverse:" ,numbers)

print("Reverse sorted:" ,sorted(numbers, reverse=True))
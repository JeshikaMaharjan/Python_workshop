
numbers = [1,2,3,4,5,6,7,8]


def determine_if_num_is_even(num):
    # print(num % 2 == 0)
    return num % 2 == 0

even = []
for num in numbers:
    if determine_if_num_is_even(num):
        even.append(num)
print(even)

#--------------------------------------

#Filter (function,iterable)
#mathi k0 kaam using filter

print(list(filter(determine_if_num_is_even,numbers))) #first parameter function, second data
#function lai as variable pass garna milxa and afai iterate ni garxa

#--------------------------------------

#Lambda

print(list(filter(lambda num: num % 2 == 0,numbers))) #lambda is inline function
#lambda iterable : condition, list

#--------------------------------------

names = ['kushal', 'Subash', 'Monika', 'Seeru', 'Tulasi', 'Buddhaa']

odd_names = list( filter( lambda name: ( len(name)%2 != 0 ), names ) )
print(odd_names)

#--------------------------------------

#map(function, iterable)
#item liyera kei kaam gardinxa

print(list(map(lambda num: num**2, numbers))) #esle num lai square gardinxa


print(list(map(lambda name: (len(name) % 2 != 0) , names))) #esle odd number of characters vako name ma True rakhdinxa

print(list(map(lambda name: "Odd" if (len(name) % 2 != 0) else "Even"  , names)))  

print(list(map(lambda name: '-'.join(name[::-1]) , names)))  #[::-1] reverses the string
#--------------------------------------

#reduce()

# print(list(reduce()))

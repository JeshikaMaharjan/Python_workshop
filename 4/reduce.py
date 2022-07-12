from functools import reduce

#reduce(function, iterable,initialize)
#euta matra output dinxa after some competition. kind of filter tara filter le list dinxa vane esle chai euta matra output dinxa

names = ['kushal', 'Subash', 'Monika', 'Seeru', 'Tulasi', 'Buddhaa']
numbers = [1,2,3,4,5,6,7,8]

print(reduce(lambda  a,b: a+b , numbers, 0 )) #esma  duita parameters liraxa lambda le a,b

print(reduce(lambda a,b:a if a>b else b,numbers))
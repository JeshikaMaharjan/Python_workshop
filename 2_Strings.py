name = 'Jeshika Maharjan'

print(name + "Jess")
print(name*5)

#--------------------------------------

#Slice indexing

print(name[1:4]) #[starting index : jata_samma_print_garaune_ho + 1 wala index]. Here  4 is not included to be printed
print(name[0:8:2]) #start_index : end_index+1 : step
print(name[0:-1:2])
print(name[0:]) #all
print(name[::-1]) #reverse
print(name[::-2]) #reverse in step 2

#--------------------------------------

#Functions

print(name.lower())
print(name.upper())
print(name.capitalize())
print(name.title()) # Every word ko first letter capitalize

#--------------------------------------

myName = ["jess" , "mhz"]
print(' '.join(myName)) # space le list ko items join garne
print(','.join(myName)) # comma le list ko items join garne


topic = ["This", "is", "our", "second", "day"]
print('-'.join(topic)) #hardcoded

topic1 = "This is our second day"
title =list(topic1.split(" "))
print('-'.join(title))


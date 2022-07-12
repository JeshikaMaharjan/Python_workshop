# Create a function that takes "staffs" as input and returns the output as expected below:

# Guide:
# 1. Evaluate the maximum value from the "scores" key of every dictionary.
# 2. Remove the "scores" from each dictionary and add the "max_score" key in the dictionary. 
#     "max_score" represents the maximum value among the "scores" list of respective dictionary.
# 3. Print the final output after receiving from the solution function


def take_input():
    staffs = [] 
    n = int(input("Enter no. of entries:"))   
    for i in range(n):
        roll = input("Enter roll: ")
        name = input("Enter name: ")
        score = input("enter your scores")
        score_list = list((score.split(',')))
        s = []
        for n in score_list:
            s.append(int(n)) #here n is not index. it is value of the list
        staffs.append({"roll" : roll, "name" : name, "score": s })
    return staffs

def update_max_score():
    staffs = take_input()
    numbers = []
    for staff in staffs:
        numbers = staff["score"]
        max_num = numbers[0]
        for num in numbers:
            if (num > max_num):
                max_num = num
        staff["score"] = max_num   
        print(staff)

update_max_score()

# Sample Input:
# staffs = [
#     {"roll": 3, "name": "Your Name Here", "scores": [1, 2, 3]},
#     {"roll": 10, "name": "Another Name Here", "scores": [4, 5, -6]},
#     {"roll": 20, "name": "Yet Another Name Here", "scores": [-7, 0, -8, -9]},
# ]

# Expected Outcome:
# [
#      {"roll": 3, "name": "Your Name Here", "max_score": 3, },
#      {"roll": 10, "name": "Another Name Here", "max_score": 5},
#      {"roll": 20, "name": "Yet Another Name Here", "max_score": 0},
#  ]
# staffs =[
#     { "roll" : 3, "name" : "Jeshika", "score" : [1,2,3]},
#     { "roll" : 10, "name" : "Malisha", "score" : [4,5,-6]},
#     { "roll" : 20, "name" : "Jenisha", "score" : [-7,0,-8,-9]}
# ]

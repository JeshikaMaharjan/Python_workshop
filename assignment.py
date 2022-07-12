staffs =[
    { "roll" : 3, "name" : "Jeshika", "score" : [1,2,3]},
    { "roll" : 10, "name" : "Malisha", "score" : [4,5,-6]},
    { "roll" : 20, "name" : "Jenisha", "score" : [-7,0,-8,-9]}
]

def update_max_score():
    numbers = []
    for staff in staffs:
        numbers = staff["score"]
        max_num = numbers[0]
        for num in numbers:
            if (num > max_num):
                max_num = num
        staff["score"] = max_num   


def display():
    update_max_score()
    for staff in staffs:
        print(staff)

display()

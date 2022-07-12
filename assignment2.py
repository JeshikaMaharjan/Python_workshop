# From the following list of accounts :
# 1) For account numbers having integer value, create a new key called "students"
#    [i.e. account_number=1,account_number=2 should have "students"]
# 2) Value of the key "students" should contain a list of dictionaries which contains the corresponding
#    ceiling value of the float number
#    [i.e. details of account_number= 1.1, account_number= 1.2 should be inside "students" of account_number 1]
# 3) Create another new key called "total_fees" which has the sum of "fees_paid" for each main account number
#    [i.e. account_number=1 should have "total_fees" which is sum of
#    "fees_paid by account_number= 1.1, account_number= 1.2"]

import math

accounts_for_level1 = [
    {"account_number": '1', 'title': 'First Year'},
    {"account_number": '1.1', 'title': 'Biswash', "fees_paid": 20000},
    {"account_number": '1.2', 'title': 'Nikita', "fees_paid": 48000},

    {"account_number": '2', 'title': 'Second Year'},
    {"account_number": '2.1', 'title': 'Yashmini', "fees_paid": 35000},
    {"account_number": '2.2', 'title': 'Anshul', "fees_paid": 27000},

    {"account_number": '3', 'title': 'Third Year'},
    {"account_number": '3.1', 'title': 'Arun', "fees_paid": 92000},
    {"account_number": '3.2', 'title': 'Jeshika', "fees_paid": 56000},

    {"account_number": '4', 'title': 'Fourth Year'},
    {"account_number": '4.1', 'title': 'Seeru', "fees_paid": 23000},
    {"account_number": '4.2', 'title': 'Kushal', "fees_paid": 87000},
]


def is_int(num):  
    check = num.find('.')
    if check == -1:
        return True
    else:
        return  False
    
accounts_list = list(filter(lambda account : is_int(account["account_number"]), accounts_for_level1))
students_list = list(filter(lambda account : is_int(account["account_number"]) == False, accounts_for_level1))


for dictionary in accounts_list:
    dictionary["students"] = []
    dictionary["total_fees"] = 0
    for student in students_list:
        if  math.floor(int(float(student["account_number"]))) == int(dictionary["account_number"]): #string(student["account_number"]) lai direct int ma lana namilera paila float then int ma lageko
            dictionary["students"].append(student)
            dictionary["total_fees"] += int(student["fees_paid"]) 
            

print(accounts_list)


    


# 1) Create a class called 'Student' which takes a name, score and total_score values.
# 2) Create a method in the class called 'get_percent' which gives the percentage (i.e. score/total_score * 100)
# 3) 'get_percent' function should have a decorator which takes the function as a whole, calculates the percentage
#    and returns the percentage as well as a grade [i.e. grade=percent/20, A+ if grade = 5, A if 4 ........and  D if
# 4) Finally print the result as [I am {name}, I got {percent}% and my grade is {grade}]

class Student:
    def __init__(self):       
        pass

    def get_grade(func):        
        def grade_calc(self,name,score,total_score):
            percent = func(self,name,score,total_score) #this parameter should match the parameters of function which it is decorating.
            percent_in_grade = percent / 20 
            if percent_in_grade >= 5:
                grade = 'A+'
            elif percent_in_grade >= 4:
                grade ='A'
            elif percent_in_grade >= 3:
                grade = 'B'
            elif percent_in_grade >= 2:
                grade = 'C'
            else:
                grade = 'D'
            print(f"I am {name}.I got {percent}% and my grade is {grade}")
            return func(self,name,score,total_score)
        return grade_calc

    @get_grade
    def get_percent(self,name, score, total_score):
        self.name =  name
        self.score = score
        self.total_score = total_score        
        return self.score/self.total_score * 100

S = Student()
S.get_percent("Jess",80,100)   




                
            

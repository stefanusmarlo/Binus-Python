class Student:
    stuCount = 0
    
    def __init__(self, name="None", score="None"):
        self.name = name
        self.score = score
        Student.stuCount +=1
        
    def displayCount(self):
        print("Total student: %d" % Student.stuCount)
    
    def printstudent(self):
        print("Name:", self.name, "\nscore:", self.score)  
        
    def getstudent(self, parameterType):
        if parameterType == "Name":
            return self.name
        elif parameterType == "Score":
            return self.score
        else:
            return "Data Not Found"
            
    def setstudent(self, name, score):
        self.name = name
        self.score = score

student1 = Student()
        
while(True):
    
    print("1. Declare Object")
    print("2. Display Object")
    print("3. Change Object Value")
    print("4. Delete Object")
    print("5. Exit Program")
    
    choice = input("Enter Your Choice (1/2/3/4/5): ")
            
    if choice == "1":
        name = input("Enter Your Name: ")
        score = input("Enter Your Score: ")
        print("Data Successfully Added")
        student1 = Student(name, score)
        
    elif choice == "2":
        student1.printstudent()
        
    elif choice == "3":
        name = input("Enter Your Name: ")
        score = input("Enter Your Score: ")
        
        student1.setstudent(name, score)
    
        print("Data Successfully Changed")
      
    elif choice == "4":
        student1.setstudent("None","None")
        
        print("Data Successfully Deleted")
        
    else:
        print("Thank you for using my program.") 
        break

class Student:
    "Common base class for all students"
    stuCount = 0
    
    def __init__(self, name="Student", nilai=100):
        self.name = name
        self.nilai = nilai
        Student.stuCount += 1
        
    def displayCount(self):
        print("Total Students: %d" % Student.stuCount)
    
    def printStudent(self):
        print("Name:", self.name, "\nNilai:", self.nilai)

student1 = Student("Stefanus", 100)

student1.printStudent()
student1.displayCount()

student2 = Student("Claudia", 75)

student2.printStudent()
student2.displayCount()

student3 = Student("Anggita", 50) 

student3.printStudent()
student3.displayCount()

input1 = input("Masukan Nama Siswa: ") 
input2 = input("Masukan Nilai Siswa: ") 

employee1 = Student(input1, input2)
employee1.printStudent() 
employee1.displayCount()

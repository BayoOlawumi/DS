class Student:
    def __init__(self, name, age, gender):
        self.name =name
        self.age =age
        self.gender = gender

    def graduate(self, old_class, new_class):
        print(f"You have successfully graduated from {old_class} to {new_class}")


femi = Student("Oluwafemi", 56, 'male')
femi.graduate("100 Level", '200 Level')

class Undergraduate(Student):
    def __init__(self, name, age, gender, matric_no, cgpa):
        super().__init__(name, age, gender)
        self.matric_no =matric_no
        self.cgpa = cgpa

    def calculate_cgpa(self, first_semester, second_semester):
        return (first_semester+second_semester)/2

felix = Undergraduate('OluwaFelix', 78, 'male', 'EEE/12/2EDSF',5.0)
felix.graduate('ss3','100level')
felix_result = felix.calculate_cgpa(4.5,4.8)
print(felix_result)
import random
futa_matric_nums = []
class Student:
    def __init__(self, name, age, phone_number, dept):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.dept = dept

    def matric_num_generator(self):
        generated_mat_num = random.randint(1000,9999)
        while generated_mat_num in futa_matric_nums:
            generated_mat_num = random.randint(1000,9999)
        self.mat_num = self.dept + '/' + str(generated_mat_num)
        futa_matric_nums.append(generated_mat_num)

    def details_merger(self):
        details = "name: " + self.name + "\n" + 'matric number: ' + str(self.mat_num) + '\n' + "age: " + str(self.age) + '\n' + 'phone number: ' + self.phone_number
        return details


for each_student in range(1,4):
    name = input(f"Please enter the name of student {each_student}")
    age = int(float(input(f"Please enter the age of student {each_student}")))
    phone_number = input(f"Please enter the phone number of student {each_student}")
    department = input(f"Please enter the department of student {each_student}")


    new_student = Student(name, age, phone_number, department)
    new_student.matric_num_generator()
    print(new_student.details_merger())

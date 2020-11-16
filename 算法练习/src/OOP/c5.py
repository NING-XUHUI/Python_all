from c6 import People


class Student(People):
    #
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
    #     self.__score = 0
    #     self.__class__.sum += 1
    def __init__(self, school, name, age):
        self.school = school
        super(Student, self).__init__(name, age)


    def do_homework(self):
        super(Student, self).do_homework()
        print('english homework')

stu = Student("xatu", '石敢当', 18)
stu.do_homework()
Student.do_homework(stu)
# print(stu.sum)
print(Student.sum)
print(stu.name)
print(stu.age)
# stu.get_name()

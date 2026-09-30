# class college:
#     def __init__(self,s,t):
#         self.student=s
#         self.teacher=t

# class student:
#     def __init__(self,r,n,m,a):
#         self.roll=r
#         self.name=n
#         self.marks=m
#         self.address=a



# class teacher:
#     def __init__(self,nam,s,dep,a):
#         self.name=nam
#         self.salary=s
#         self.deparement=dep
#         self.address=a


# class address:
#     def __init__(self,c,p):
#         self.city=c
#         self.pincode=p
# a=address("Pune",422303)

# s=student(21,"pratiksha",90,a)
# t=teacher("Radhika",250000,"computer science",a)
# c = college(s, t)

# print("College Details")
# print("Student Roll:", c.student.roll)
# print("Student Name:", c.student.name)
# print("Student Marks:", c.student.marks)
# print("Student City:", c.student.address.city)
# print("Student Pincode:", c.student.address.pincode)


# print("Teacher Details")
# print("Teacher Name:", c.teacher.name)
# print("Teacher Salary:", c.teacher.salary)
# print("Teacher Department:", c.teacher.deparement)
# print("Teacher City:", c.teacher.address.city)
# print("Teacher Pincode:", c.teacher.address.pincode)


# Output
# College Details
# Student Roll: 21
# Student Name: pratiksha
# Student Marks: 90
# Student City: Pune
# Student Pincode: 422303

# Teacher Details
# Teacher Name: Radhika
# Teacher Salary: 250000
# Teacher Department: computer science
# Teacher City: Pune
# Teacher Pincode: 422303



class Student:
    def __init__(self, n, a, s):
        self.name = n
        self.age = a
        self.subjects = s


s = Student("Pratiksha", 20, ["Python", "Java", "Data Analytics"])

print(s.name)
print(s.age)
print(s.subjects)

print(s)
print(type(s))
print(id(s))

# Output
# Pratiksha
# 20
# ['Python', 'Java', 'Data Analytics']
# <__main__.Student object at 0x000002C1D69E6A50>
# <class '__main__.Student'>
# 3031552649808
# from enum import IntEnum
#
# class StudentEnm(IntEnum):
#     NAME=0
#     AGE=1
#     SEX=2
#     EMAIL=3

from collections import namedtuple

Student=namedtuple('student',['name','age','sex','email'])
s2=Student('Jim', 16, 'male', 'jim@qq.com')
print(s2.name)

# Name=0
# AGE=1
# SEX=2
# EMAIL=3

# Name, AGE, SEX, EMAIL = range(4)


# def XXX_func(student):
#     if student[AGE] < 18:
#         pass
#     if student[SEX] == 'male':
#         pass
#
#
# student = ('Jim', 16, 'male', 'jim@qq.com')
# XXX_func(student)

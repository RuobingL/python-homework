class Student:
    def __init__(self, id):
        self.id = id;

class Class:
    '''
     * Declare a constructor with a parameter n which is the total number of
     * students in the *class*. The constructor should create n Student
     * instances and initialized with student id from 0 ~ n-1
    '''
    def __init__(self, num):
        # cls = []
        # for i in range(num):
        #     cls.append(Student(i))
        self.students =  [Student(i) for i in range(num)]

if __name__ == '__main__':
    cls = Class(3)
    print cls.students[0]
    print cls.students[1]
    print cls.students[2]



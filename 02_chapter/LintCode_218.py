class Student:
    score = 0
    '''
     * Declare a constructor expect a name as a parameter.
    '''
    # write your code here
    def __init__(self, name):
        self.name = name

    '''
     * Declare a public method `getLevel` to get the level(char) of this student.
    '''
    # write your code here
    def getLevel(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 80 and self.score < 90:
            return 'B'
        elif self.score >= 60 and self.score < 80:
            return 'C'
        else:
            return 'D'

if __name__ == '__main__':
    student = Student("Zuck")
    student.score = 10
    print student.getLevel() # should be 'D'
    student.score = 60
    print student.getLevel() # should be 'C'
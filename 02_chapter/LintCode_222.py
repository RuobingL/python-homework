class School:
    name = ''
    '''
     * Declare a setter method `setName` which expect a parameter *name*.
    '''
    # write your code here
    def setName(self, name):
        self.name = name

    '''
     * Declare a getter method `getName` which expect no parameter and return
     * the name of this school
    '''
    # write your code here
    def getName(self):
        return self.name

if __name__ == '__main__':
    school = School();
    school.setName("MIT")
    print school.getName() # should return "MIT" as a result.
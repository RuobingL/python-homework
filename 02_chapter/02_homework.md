# 阶梯训练  2 - Function & Class
## 1. LintCode_454 矩阵面积
**描述：**
```
实现一个矩阵类Rectangle，包含如下的一些成员变量与函数：

两个共有的成员变量 width 和 height 分别代表宽度和高度。
一个构造函数，接受2个参数 width 和 height 来设定矩阵的宽度和高度。
一个成员函数 getArea，返回这个矩阵的面积。
```

**样例：**
```
Java:
    Rectangle rec = new Rectangle(3, 4);
    rec.getArea(); // should get 12

Python:
    rec = Rectangle(3, 4)
    rec.getArea()
```

**Code:**
```
class Rectangle:

    '''
     * Define a constructor which expects two parameters width and height here.
    '''
    def __init__(self, width, height):
        self.width = width
        self.height = height

    '''
     * Define a public method `getArea` which can calculate the area of the
     * rectangle and return.
    '''
    def getArea(self):
        return self.width * self.height
```

## 2. LintCode_222 Getter与Setter
**描述：**
实现一个School的类，包含下面的这些属性和方法:
- 一个string类型的私有成员name.
- 一个setter方法setName，包含一个参数name.
- 一个getter方法getName，返回该对象的name。

**样例：**
```
Java:
    School school = new School();
    school.setName("MIT");
    school.getName(); // should return "MIT" as a result.

Python:
    school = School();
    school.setName("MIT")
    school.getName() # should return "MIT" as a result.
```

**Code:**
```
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
```

## 3. LintCode_455 学号
**描述：**
```
实现一个名为Class的类，包含如下的一些属性和方法：

一个public的students属性，是一个Student类的数组。
一个构造函数，接受一个参数n，代表班级里有n个学生。构造函数需要创建n个学生的实例对象并放在students这个成员中，每个学生按照创建的顺序，学号需要依次标记为0, 1, 2 ... n-1。
```
**样例：**
```
Java:
    Class cls = new Class(3)
    cls.students[0]; // should be a student instance with id = 0
    cls.students[1]; // should be a student instance with id = 1
    cls.students[2]; // should be a student instance with id = 2

Python:
    cls = new Class(3)
    cls.students[0] # should be a student instance with id = 0
    cls.students[1] # should be a student instance with id = 1
    cls.students[2] # should be a student instance with id = 2
```



**Code:**
```
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
        self.students = [Student(i) for i in range(num)]
```


## 4. LintCode_218 乘积等级
**描述：**
实现一个学生的类 Student. 包含如下的成员函数和方法：

1. 两个公有成员name和score。分别是字符串类型和整数类型。
2. 一个构造函数，接受一个参数name。
3. 一个公有成员函数getLevel() 返回学生的成绩等级（一个字符）。

等级表如下：

- A: score >= 90
- B: score >= 80 and < 90
- C: score >= 60 and < 80
- D: score < 60

**样例：**
```
Java:
    Student student = new Student("Zuck");
    student.score = 10;
    student.getLevel(); // should be 'D'
    student.score = 60;
    student.getLevel(); // should be 'C'

Python:
    student = Student("Zuck")
    student.score = 10
    student.getLevel() # should be 'D'
    student.score = 60
    student.getLevel() # should be 'C'
```

**Code:**
```
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
```

## 5. LintCode_497 形状工厂
**描述：**
```
工厂模式是一种常见的设计模式。实现一个形状工厂 ShapeFactory 来创建不同的形状类。这里我们假设只有三角形，正方形和矩形三种形状。
```

**样例：**
```
ShapeFactory sf = new ShapeFactory();
Shape shape = sf.getShape("Square");
shape.draw();
>>  ----
>> |    |
>> |    |
>>  ----

shape = sf.getShape("Triangle");
shape.draw();
>>   /\
>>  /  \
>> /____\

shape = sf.getShape("Rectangle");
shape.draw();
>>  ----
>> |    |
>>  ----
```

**Code:**
```
"""
Your object will be instantiated and called as such:
sf = ShapeFactory()
shape = sf.getShape(shapeType)
shape.draw()
"""
class Shape:
    def draw(self):
        raise NotImplementedError('This method should have implemented.')

class Triangle(Shape):
    def draw(self):
        print '  /\\  '
        print ' /  \\ '
        print '/____\\'


class Rectangle(Shape):
    def draw(self):
        print ' ---- '
        print '|    |'
        print ' ---- '


class Square(Shape):
    def draw(self):
        print ' ---- '
        print '|    |'
        print '|    |'
        print ' ---- '


class ShapeFactory:
    # @param {string} shapeType a string
    # @return {Shape} Get object of type Shape
    def getShape(self, shapeType):
        return {
            'Triangle': Triangle(),
            'Rectangle': Rectangle(),
            'Square': Square()
        }[shapeType]
```

## 6. LintCode_498 停车场
**描述：**
```
设计一个停车场
1. 一共有n层，每层m列，每列k个位置
2.停车场可以停摩托车，公交车，汽车
3.停车位分别有摩托车位，汽车位，大型停车位
4.每一列，摩托车位编号范围为[0,k/4),汽车停车位编号范围为[k/4,k/4*3),大型停车位编号范围为[k/4*3,k)
5.一辆摩托车可以停在任何停车位
6.一辆汽车可以停在一个汽车位或者大型停车位
7.一辆公交车可以停在一列里的连续5个大型停车位。
```

**样例：**
```
level=1, num_rows=1, spots_per_row=11
parkVehicle("Motorcycle_1") // return true
parkVehicle("Car_1") // return true
parkVehicle("Car_2") // return true
parkVehicle("Car_3") // return true
parkVehicle("Car_4") // return true
parkVehicle("Car_5") // return true
parkVehicle("Bus_1") // return false
unParkVehicle("Car_5")
parkVehicle("Bus_1") // return true
```


**Code:**
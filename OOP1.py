# Java is nearly 100%

# Object Oriented Prog.


# class Uday 
# {
#     int id;   // 2
#     char name[10]; // 10
#     float marks;  // 4

#         Uday(int id, int marks)   // Parametrized Constructor
#         {
#              this->id = id;
#              this->marks = marks;
#         }

# Uday u1(10, 89)
#     void set_data()
#     {
#         printf("ENter Id, Name, MArks");
#         strcpy(name, "Manoj");
#         scanf("%d%f",&id,&marks);
#     }

#     void display()
#     {
#         printf("Id = %d\nName = %s\nmarks = %f",id,name,marks);
#     }

# };



# // 16 Bytes

# main()
# {
#             int   a;   // 2 Byte
#     # struct Uday  u1, u2;   // 16 Byte
#              Uday  u1, u2;  // Uday is Class, u1,u2 is Objects

#     u1.set_data();
#     u1.display();
# }


# Variables : 1. Instance Variable     2. Class Variable
# Methods   : 1. Instance Method  2. Static Method   3. Class Method


# Constructor : It is a Special Method, It Solves Intialization Problem, Autocalling, No return Type

# Self ---> like This Keyword in CPP


class Student:
    school_name = "HBK"    # class Variable


    def __init__(self):   # Constructor
        self.id = int(input("Enter Id: "))   # Instance Variable
        self.name = input("Enter Name: ")    # Instance Variable

        print("This is Default Constructor")


    def display_data11111(self):    # Instance Method
        print(self.name,"'s Id = ",self.id)


    @classmethod   # Decorator
    def change_school(cls):
        cls.school_name = input("Enter School Name: ")

# Student harsh;   in CPP

harsh = Student()
parth = Student()

harsh.display_data11111()
parth.display_data11111()

print(harsh.school_name)
print(parth.school_name)


# harsh.school_name = 'Delta Sci'


# print(harsh.school_name)
# print(parth.school_name)

# print(Student.school_name)

# Student.school_name = "Delta Science"
harsh.change_school()

print(harsh.school_name)
print(parth.school_name)

Student.change_school()


print(harsh.school_name)
print(parth.school_name)

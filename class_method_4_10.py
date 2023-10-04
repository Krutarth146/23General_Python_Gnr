# class Student
# {
#     int id;
#     char name[10];
#     float marks;


#     void edit_marks()
#     {
#         arin.id
#         arin.name
#     }

#     void display()
#     {
#         print(Data)
#     }
# };

# struct Employee
# {
#     int id;
#     char name[10];
#     float marks;
# };


# main()
# {
#             int       a;
#     struct Student   arin, nupur;
#            Student   s1;
# }

# ----------------------------------------------

class Student:

    Institute = "Royal"   # Class Variable
    Agee = 90

    # def __init__(self) -> None:
    #     self.id = int(input())   # Instance Variable
    #     self.name = input()
    #     self.marks = float(input())


    def __init__(self, id, name1, marks1) -> None:
        self.id = id   # Instance Variable
        self.name = name1
        self.marks = marks1


    def show_marks(self):        # Instance Method
        print('Your Marks are Good',self.marks)

    def edit_marks(self):
        self.marks = float(input("Enter Marks: "))


arin = Student(10, "Arin", 900)
yash = Student(20, "Manoj", 800)

arin.edit_marks()


arin.show_marks()
yash.show_marks()

print(arin.Institute)   # View Access
print(yash.Institute)    # View Access
print(Student.Institute)  # View, Edit

arin.Institute = "PhysicsWala"  # Edit



print(arin.Institute)   # PhysicsWala
print(yash.Institute)   # Royal
print(Student.Institute)  # View, Edit


Student.Institute = "Bothra"

print(arin.Institute)   # PhysicsWala
print(yash.Institute)   # Bothra
print(Student.Institute)  # Bothra
print(Student.Agee)  # 90


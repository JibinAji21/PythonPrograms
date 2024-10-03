# polymorphism

# Two types of polymorphism 

# 1) Method overloading ( not supported in python )

# 2) Method overriding ( supports in python )


# example 1:

# class school:
#     def notes():
#         print("notes in school")
# class student(school):
#     def notes(self):
#         print("notes in student")
# s=student()
# s.notes()

# # output

# notes in student


# # example 2:

# class bank:
#     def __init__(self):
#         print("add bank dtls")
# class users(bank):
#     def __init__(self):
#         print("add user dtls")
# sbi=bank()
# jo=users()

# # output

# add bank dtls
# add user dtls


# super() ( super function is used to solve polymorphism )

# example

# class school:
#     def notes(self,sub):
#         print("notes",sub)
# class student(school):
#     def notes(self):
#         print("notes in student")
#         super().notes('py')

# john=student()
# john.notes()


# passing avalue to parent class


# class school:
#     def notes(self,sub):
#         print("notes",sub)
# class student(school):
#     def notes(self,sub):
#         print("notes in student")
#         super().notes(sub)

# john=student()
# john.notes('py')




    

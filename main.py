# print statements
print("Enter 1 for battleship")
print("enter 2 for students_to_teacher")
print("enter 3 for exam_stats")

#user input panel
demand = input("Enter Your Choice Which You want..::")
if demand == "1":
    import battleship
    battleship.battleship()
elif demand== "2":
    import students_to_teacher
    students_to_teacher.students_to_teacher()
elif demand== "3":
    import exam_stats
    exam_stats.exam_stats()
else:
    print ("you donot enter according to given instuctions")

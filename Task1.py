student_marks = {"Dhruvil": 90, "Rohit": 80, "Shubham": 50, "Sujal": 40}

student_name = input("Enter your name: ")

if student_name in student_marks:
    print(student_name + "'s marks :", student_marks[student_name])
else:
    print(student_name, "doesn't exist")
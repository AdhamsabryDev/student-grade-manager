print('=' * 80)
print("welcome to grade manager".title().center(80))
print('=' * 80)

g1,g2,g3 =80,70,90
student={
    "adham":{
     'grade1':g1,
    'grade2':g2,
    'grade3':g3,
    'average':(g1+g2+g3)/3   
        }
    
    }
while True :
    print('1_add student\n2_show student\n3_search student\n4_exit'.title())
    userchoose=input('Choose the number 1:4 ').strip()

    if userchoose=="1":
        name=input("enter student name: ").lower().strip()
        g1=float(input("enter grade 1: "))
        g2=float(input("enter grade 2: "))
        g3=float(input("enter grade 3: "))

        avg=(g1+g2+g3)/3

        student[name]={
            'grade1':g1,
            'grade2':g2,
            'grade3':g3,
            'average':avg
        
        }
        print(f"student {name} added successfully")

    elif userchoose=="2":
        if student:
            print("Registered students: ")
            for s_name in student:
                print(f"-{s_name.title()}")
        else:
            print("No students found")

    elif userchoose=='3':

        inputstudent=input("what is the student name ").lower().strip()

        if inputstudent in student:
            studentdata=student[inputstudent]

            for key , value in studentdata.items():
                print(f"{key}:{value}")


            if studentdata["average"]>= 50:
                print("passed")

            else:
                print("failed")

        else:
            print("student not found")

    elif userchoose=="4":
        print("Goodbye")
        break
    else:
        print("pls select number from 1 to 4")


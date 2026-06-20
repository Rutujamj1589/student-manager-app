import json
students = {}

try:                             # file handling concept
    with open("students.json", "r") as file:
        students = json.load(file)
except FileNotFoundError:
    students = {}

while True:
    print("\n --- Welcome to Students Manager App ---")
    print("1. Add Students")
    print("2. View Students")
    print("3. Delete Students")
    print("4. Check Result")
    print("5. Update Students Data")       
    print("6. Exit")

    choice = input("Select the Option")

      
    
    if choice == "1":

        name = input("Enter Student Full name.")
                      
        roll_no = int(input("Enter Student Roll Number."))
        duplicate = False

        for details in students.values():

            if details["roll_no"] == roll_no:
                duplicate = True
                break

        if duplicate:
            print("Roll Number already exists!")
            continue


        branch = input("Enter Student Branch ..")
        marks = int(input("Enter Student marks."))
        age = int(input("Enter Student age."))
        gender = input("Enter Student Gender")
        division = input("Enter Student Division ")

        students[name]= {
            "roll_no": roll_no,
            "branch": branch,
            "marks": marks,
            "age": age,
            "gender": gender,
            "division": division
        }
        
        print(f"{name}  Added Successfully!")


        with open("students.json", "w") as file:
            json.dump(students, file, indent=4)

    elif choice == "2":
        if not  students:
            print("Student is not Present.")

        else:
            for name, details in students.items():
                print(

                "\nName:", name,
                "\nRoll No:", details["roll_no"],
                "\nBranch:", details["branch"],
                "\nMarks:", details["marks"],
                "\nAge:", details["age"],
                "\nGender:", details["gender"],
                "\nDivision:", details["division"]

                )
                

    elif choice == "3":


        roll_no = int(input("Enter Roll Number of that student: "))

        student_to_delete = None

        for name, details in students.items():

            if details["roll_no"] == roll_no:
                student_to_delete = name
                break

        if student_to_delete:

            del students[student_to_delete]

            print("Student Deleted Successfully")

            with open("students.json", "w") as file:
                json.dump(students, file, indent=4)

        else:

            print("Student Not Found.")


    elif choice =="4":
        roll_no = int(input("Enter Roll Number of that student"))

        found= False

        for name, details in students.items():
            if details["roll_no"]== roll_no:
                found = True
                
                print("\nStudent Name:", name)
                print("Marks:", details["marks"])

                if details["marks"] >= 35:
                     
                     print("Result: PASS")

                else:
                                    
                    print("Result: FAIL")

                break

        if not found:
          print("Student Not Found")
                
         

    


    elif choice == "5":
        roll_no = int(input("Enter Roll Number of that student"))

        found= False

        for name, details in students.items():
            if details["roll_no"]== roll_no:
                found = True

                while True:
                    print("---- updated menu ----")
                    print("1. Branch")
                    print("2. marks")
                    print("3. age")
                    print("4. gender")
                    print("5. division")
                    print("6.Back to main menu")


                    update_choice = input("Select Option: ")


                    if update_choice == "1":


                        new_branch = input("Enter New Branch: ")
                        details["branch"] = new_branch

                        print("Branch updated successfully.")

                        with open("students.json", "w") as file:
                            json.dump(students, file, indent=4)

                    elif update_choice == "2":

                        new_marks = int(input("Enter New Marks: "))
                        details["marks"] = new_marks

                        print("Marks Updated Successfully.")

                        with open("students.json", "w") as file:
                            json.dump(students, file, indent=4)

                    elif update_choice == "3":

                        new_age = int(input("Enter New Age: "))
                        details["age"] = new_age

                        print("Age Updated Successfully.")

                        with open("students.json", "w") as file:
                            json.dump(students, file, indent=4)

                    elif update_choice == "4":

                        new_gender = input("Enter New Gender: ")
                        details["gender"] = new_gender

                        print("Gender Updated Successfully.")

                        with open("students.json", "w") as file:
                            json.dump(students, file, indent=4)

                    elif update_choice == "5":

                        new_division = input("Enter New Division: ")
                        details["division"] = new_division

                        print("Division Updated Successfully.")

                        with open("students.json", "w") as file:
                            json.dump(students, file, indent=4)

                    elif update_choice == "6":

                        print("Exiting Update Menu...")
                        break

                    else:
                        print("Invalid Choice !!!!!!")

                break

        if not found:
              
          print("Student Not Found.")
    

    elif choice == "6":
           
        print("Thank you for Visiting us.!!!!")
        break

                
                    





























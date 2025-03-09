import os

def calculate_grade(percentage):
    if percentage >= 80:
        return "A+"
    elif percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "F"
    else:
        return "Fail"

def get_student_data():
    students = []
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nEnter Student Details:")
        name = input("Student Name: ")
        roll_number = input("Roll Number: ")
        
        subjects = ["Math", "Physics", "Urdu", "English", "Computer"]
        marks = {}
        
        for subject in subjects:
            while True:
                try:
                    marks[subject] = int(input(f"Enter marks for {subject}: "))
                    if 0 <= marks[subject] <= 100:
                        break
                    else:
                        print("Marks should be between 0 and 100. Try again.")
                except ValueError:
                    print("Invalid input! Please enter numeric marks.")
        
        total_marks = sum(marks.values())
        percentage = total_marks / len(subjects)
        grade = calculate_grade(percentage)
        
        students.append({
            "Name": name,
            "Roll Number": roll_number,
            "Marks": marks,
            "Total Marks": total_marks,
            "Percentage": percentage,
            "Grade": grade
        })
        
        print(f"\nRecord of {name} inserted successfully.")
        more = input("Do you want to insert more? (Y/N): ").strip().lower()
        if more != 'y':
            break
    return students

def generate_report(students):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nStudent Report Cards:")
    for student in students:
        print("\n--------------------------------------")
        print(f"Student Name: {student['Name']}")
        print(f"Roll Number: {student['Roll Number']}")
        print("Marks:")
        for subject, mark in student['Marks'].items():
            print(f"  {subject}: {mark}")
        print(f"Total Marks: {student['Total Marks']}")
        print(f"Percentage: {student['Percentage']:.2f}%")
        print(f"Grade: {student['Grade']}")
        print("--------------------------------------")

def main():
    students = get_student_data()
    generate_report(students)

if __name__ == "__main__":
    main()


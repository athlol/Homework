def calculate_average_grade():
    num_subjects = int(input("Enter the number of subjects: "))
    grades = []

    for i in range(num_subjects):
        grade = float(input(f"Enter the grade for subject {i + 1}: "))
        grades.append(grade)

    total_grades = sum(grades)
    average_grade = total_grades / num_subjects

    print(f"Average grade: {average_grade:.2f}")

calculate_average_grade()

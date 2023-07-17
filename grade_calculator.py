def calculate_average_grade():
    num_subjects = int(input("Enter the number of subjects: "))
    grades = []

    for i in range(num_subjects):
        grade = float(input("Enter the grade for subject {}: ".format(i + 1)))
        grades.append(grade)

    total_grades = sum(grades)
    average_grade = total_grades / num_subjects

    print("Average grade: {:.2f}".format(average_grade))

calculate_average_grade()
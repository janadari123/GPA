def calculate_gpa(course_grades):
    grade_points = {'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'F': 0.0}

    total_credits = 0
    total_grade_points = 0

    for course, grade, credits in course_grades:
        if grade in grade_points:
            total_credits += credits
            total_grade_points += grade_points[grade] * credits

    if total_credits == 0:
        return None

    gpa = total_grade_points / total_credits
    return gpa

def main():
    num_courses = int(input("Enter the number of courses: "))
    course_grades = []

    for _ in range(num_courses):
        course = input("Enter course name: ")
        grade = input("Enter grade (A, A-, B+, etc.): ")
        credits = int(input("Enter credits: "))
        course_grades.append((course, grade, credits))

    gpa = calculate_gpa(course_grades)
    
    if gpa is not None:
        print(f"Your GPA is: {gpa:.2f}")
    else:
        print("No valid courses provided.")

if __name__ == "__main__":
    main()

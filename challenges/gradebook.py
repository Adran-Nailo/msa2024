import color_testing
color = color_testing.Color()
print(color.clear)

gradebook = [[61, 74, 69, 62, 72, 66, 73, 65, 60, 63, 69, 63, 62, 61, 64],
             [73, 80, 78, 76, 76, 79, 75, 73, 76, 74, 77, 79, 76, 78, 72],
             [90, 92, 93, 92, 88, 93, 90, 95, 100, 99, 100, 91, 95, 99, 96],
             [96, 89, 94, 88, 100, 96, 93, 92, 94, 98, 90, 90, 92, 91, 94],
             [76, 76, 82, 78, 82, 76, 84, 82, 80, 82, 76, 86, 82, 84, 78],
             [93, 92, 89, 84, 91, 86, 84, 90, 95, 86, 88, 95, 88, 84, 89],
             [63, 66, 55, 67, 66, 68, 66, 56, 55, 62, 59, 67, 60, 70, 67],
             [86, 92, 93, 88, 90, 90, 91, 94, 90, 86, 93, 89, 94, 94, 92],
             [89, 80, 81, 89, 86, 86, 85, 80, 79, 90, 83, 85, 90, 79, 80],
             [99, 73, 86, 77, 87, 99, 71, 96, 81, 83, 71, 75, 91, 74, 72]]
def get_assignment_average():
    assignment_averages = []
    for index in range(len(gradebook[0])):
        column_total = 0
        for row in range(len(gradebook)):
            column_total += gradebook[row][index]
        column_average = column_total / len(gradebook)
        assignment_averages.append(column_average)
    return assignment_averages

def get_student_average():
    student_average_list = []
    for row in range(len(gradebook)):
        row_total = 0
        for length in range(len(gradebook[row])):
            row_total += gradebook[row][length]
        student_average = row_total / len(gradebook[row])
        student_average_list.append(student_average)
    return student_average_list


def main():
    assignment_average_list = get_assignment_average()
    student_average_list = get_student_average()
    print("\n\nAssignment Averages:\n-----------------")
    for number in range(len(assignment_average_list)):
        print(f"Assignment {number + 1}: {assignment_average_list[number]:.2f}")
    print("\n\nStudent Averages:\n-----------------")
    for number in range(len(student_average_list)):
        print(f"Student {number + 1}: {student_average_list[number]:.2f}")
    print("\n\n")
main()
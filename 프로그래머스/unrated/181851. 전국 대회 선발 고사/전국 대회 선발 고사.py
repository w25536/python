def solution(rank, attendance):

    student_with_ranks =[]

    for i, r in enumerate(rank):
        student_with_ranks.append((i, r))

    students_sorted_by_ranks = sorted(student_with_ranks, key=lambda student: student[1])

    eligible_student = []

    for student_num, student_rank in students_sorted_by_ranks:
        if attendance[student_num]:
            eligible_student.append(student_num)
    
    
    top_three_students = eligible_student[:3]
    a, b, c = top_three_students
    
    return 10000 * a + 100 * b + c
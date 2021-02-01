n = int(input()) # 학생 수 입력
student_list = []

for _ in range(n):
    student_list.append(list(input().split()))

# 학생의 점수 순으로 정렬
student_list.sort(key=lambda student: int(student[1]))

# 점수순으로 정렬된 학생들의 이름 출력
for student_name, _ in student_list:
    print(student_name, end=' ')
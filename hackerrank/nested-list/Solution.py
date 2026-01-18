if __name__ == '__main__':
    students = []
    names = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    min_sc = min(student[1] for student in students)
    sec_min_sc = min(student[1] for student in students if student[1] > min_sc)

    for student in students:
        if student[1] == sec_min_sc:
            names.append(student[0])

    for name in sorted(names):
        print(name)

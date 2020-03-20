if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    lowest_score = students[0][1]

    for i in range(1, len(students)):
        lowest_score = min(students[i][1], lowest_score)

    students = [st for st in students if st[1] != lowest_score]
    lowest_score = students[0][1]

    for i in range(1, len(students)):
        lowest_score = min(students[i][1], lowest_score)

    students = [st[0] for st in students if st[1] == lowest_score]
    students.sort()

    for st in students:
        print(st)

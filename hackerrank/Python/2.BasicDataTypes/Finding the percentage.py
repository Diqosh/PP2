
def pr_avg(dic, name):
    for key, value in dic.items():
        if key == name:
            return sum(value)/len(value)


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(format(pr_avg(student_marks, query_name), '.2f'))
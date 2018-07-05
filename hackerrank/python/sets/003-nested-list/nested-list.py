inputs = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    inputs.append([name, score])

students = {}
scores = set()
for name, score in inputs:
    if score not in students:
        students[score] = [name]
    else:
        students[score].append(name)
    scores.add(score)
scores = list(scores)
scores.sort()
second_bests = sorted(students[scores[1]])
for name in second_bests:
    print(name)
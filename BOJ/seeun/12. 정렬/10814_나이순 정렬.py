n = int(input())
people = []
for _ in range(n):
    age, name = input().split()
    people.append([int(age), name])

people.sort(key=lambda x:x[0])
for i in range(n):
    print(people[i][0], people[i][1])
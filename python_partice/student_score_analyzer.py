students = {
    "Alice": 85,
    "Bob": 45,
    "Charlie": 92,
    "David": 60
}

n = 0
total = 0

for i in students:
    total = total + students[i]
    if students[i] >= 60:
        n = n + 1
        print(i,students[i],"PASS")
    else:
        print(i,students[i],"FAIL")

avg = total/len(students)
print(f"Passed students = {n}")
print(f"Average score = {avg:.2f}")

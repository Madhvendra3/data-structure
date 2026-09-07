marks = [78, 65, 92, 56, 84, 73, 88, 61]

print("Number of marks:", len(marks))
print("First mark:", marks[0])
print("First 3 marks:", marks[:3])

print("All marks:")
for mark in marks:
    print(mark)

total = sum(marks)
average = total / len(marks)

print("Total:", total)
print("Average:", average)
print("Smallest:", min(marks))
print("Largest:", max(marks))
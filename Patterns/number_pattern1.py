# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

rows = int(input("Enter number of rows: "))

for i in range(1,rows + 1):
    for j in range(i):
        print(i, end = " ")
    print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
print()
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(i):
        print(j+1, end = " ")
    print()

print()

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
rows = int(input("Enter the number of rows: "))

num = 0
for i in range(1, rows + 1):
    for j in range(i):
        num += 1
        print(num, end = " ");
    print()
print()

# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5
rows = int(input("Enter number of rows: "))
b = 0
for i in range(rows, 0, -1):
    b+=1;
    for j in range(1, i+1):
        print(b, end = " ")
    print()
print()

# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end = " ");
    print()

print()

# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4
#5
rows = int(input("Enter the number of rows: "))
for i in range(rows, 0, -1):
    for j in range(i, 0, -1):
        print(j, end = " ")
    print()

print()

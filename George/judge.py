size1 = int(input("What's the size of the first square matrix? (Type and press Enter) "))
size2 = int(input("What's the size of the second square matrix? (Type and press Enter) "))

while (size1 != size2):
    print("Invalid matrices size!")
    print("Both matrices must have the same size in order to be multiplied!")
    size1 = int(input("What's the size of the first square matrix? (Type and press Enter) "))
    size2 = int(input("What's the size of the second square matrix? (Type and press Enter) "))

matrix1 = []
matrix2 = []

print("What are the elements of the first matrix?")
print("(Write them from left to right, then from top to bottom. Press Enter after each element!)")
for i in range (size1):
    matrix1.append([])
    for j in range (size1):
        element = float(input())
        matrix1[i].append(element)

print("What are the elements of the second matrix?")
print("(Write them from left to right, then from top to bottom. Press Enter after each element!)")
for i in range (size1):
    matrix2.append([])
    for j in range (size1):
        element = float(input())
        matrix2[i].append(element)

matrix3 = []

for i in range(size1):
    matrix3.append([])
    for j in range(size1):
        sum = 0
        for k in range(size1):
            sum += matrix1[i][k] * matrix2[k][j]
        matrix3[i].append(sum)

print("The product of the first matrix and the second matrix results in: ")
for i in range(size1):
    for j in range(size2):
        print(matrix3[i][j], end=" ")
    print("")
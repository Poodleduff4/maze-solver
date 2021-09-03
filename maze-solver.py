import numpy as np

def printArray():
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(m[i][j], end = ' ')
        print()

a = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

start = 1, 1
end = 2, 5

m = []
for i in range(len(a)):
    m.append([])
    for j in range(len(a[i])):
        m[-1].append(0)

i,j = start

m[i][j] = 1
printArray()

def makeStep(k):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if m[i][j] == k:
                print(str(i) + ' | ' + str(j))
                if m[i-1][j] == 0 and a[i-1][j] == 0:
                    m[i-1][j] = k + 1

                if m[i+1][j] == 0 and a[i+1][j] == 0:
                    m[i+1][j] = k + 1

                if m[i][j-1] == 0 and a[i][j-1] == 0:
                    m[i][j-1] = k + 1

                if m[i][j+1] == 0 and a[i][j+1] == 0:
                    m[i][j+1] = k + 1

k = 0

while m[end[0]][end[1]] == 0:
    k += 1
    makeStep(k)

printArray()
print()
print()
print()
print()



i, j = end
k = m[i][j]
path = [(i, j)]
while k > 1:
    if i > 0 and m[i-1][j] == k-1:
        i, j = i-1, j
        path.append((i, j))
        k -= 1
    elif i < len(m) - 1 and m[i+1][j] == k-1:
        i, j = i+1, j
        path.append((i, j))
        k -= 1
    elif j > 0 and m[i][j-1] == k-1:
        i, j = i, j-1
        path.append((i, j))
        k -= 1
    elif j < len(m[i]) - 1 and m[i][j+1] == k-1:
        i, j = i, j+1
        path.append((i, j))
        k -= 1

print(path)
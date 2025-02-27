#AIM: Write a program for generating derivation sequence / language for the given sequence of productions.
def printArray(arr, size):
    for i in range(size):
        print(arr[i], end=" ")
    print()
    return

def getSuccessor(arr, k, n):
    p=k-1
    while (arr[p] == n and 0 <= p < k):
        p -= 1
    if (p < 0):
        return 0
    arr[p] = arr[p] + 1
    i = p + 1

    while(i < k):
        arr[i] = 1
        i += 1
    return 1

def printSequences(n, k):
    arr = [0]*k
    for i in range(k):
        arr[i] = 1
        while(1):
            printArray(arr, k)
            if getSuccessor(arr, k, n) == 0:
                break
n = 3
k = 2
printSequences(n, k)

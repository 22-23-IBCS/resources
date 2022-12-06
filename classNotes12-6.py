import random
import time

def main():

    L = []
    n = 15000
    for i in range(n):
        L.append(random.randint(0, n))

    #print(L)
    print("commence selection sort")

    #sort with Selection Sort

    start = time.time()
    for i in range(len(L) - 1):
        curMin = L[i]
        indMin = i
        for j in range(i, len(L)):
            if L[j] < curMin:
                curMin = L[j]
                indMin = j
        #swap
        temp = L[i]
        L[i] = L[indMin]
        L[indMin] = temp

    stop = time.time()
    total = stop - start
    print("done")
    #print(L)
    print("For " + str(n) + " elements...")
    print("Time passed: " + str(total) + " seconds")


if __name__ == "__main__":
    main()

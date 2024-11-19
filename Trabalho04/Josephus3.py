import numpy as np

def josephus3(n, k):
    a = np.full(n, True)
    visited = 1
    alive = n
    lastVisited = None
    
    while alive > 1:
        for i in range(0, n):
            if a[i] == True:
                if visited == k:
                    a[i] = False
                    visited = 1
                    alive -= 1
                else:
                    visited += 1
                    lastVisited = i+1
                    
    print("Result: ", lastVisited)

def josephus3Debug(n, k):
    a = np.full(n, True)
    visited = 1
    alive = n
    lastVisited = None
    
    while alive > 1:
        for i in range(0, n):
            if a[i] == True:
                if visited == k:
                    a[i] = False
                    visited = 1
                    alive -= 1
                    print("Killed ", i+1)
                else:
                    visited += 1
                    lastVisited = i+1
                    print("Visited ", i+1)
                    
    print("Result: ", lastVisited)
    print("Debug: ", a)

##Com Short-Circuit - Depois notei que não funcionava no Oz pois o Array nem pode ser mudado nem ser sobreescrito no Oz. Em Python, ele não pode ser mudado, mas pode ser sobreescrito.

def josephus3SC(n, k):
    a = np.arange(1, n+1)
    visited = 1
    alive = n
    lastVisited = None
    killed = None
    
    while alive > 1:
        for i in range(0, a.size):
            if visited == k:
                killed = np.insert(killed, 0, i)
                visited = 1
                alive -= 1
            else:
                visited += 1
                lastVisited = a[i]
        while killed[0] is not None:
            a = np.delete(a, killed[0])
            killed = np.delete(killed, 0)
                    
    print("Result: ", lastVisited)
    

##Com Short-Circuit - Compatível com Oz <- Na verdade é mais lento lmao

def nextAlive(array, i):
    i = i%array.size
    if(array[i] == -1):
        return i
    else:
        return nextAlive(array, array[i])

def josephus3SCOz(n, k):
    a = np.full(n, -1)
    visited = 1
    alive = n
    lastVisited = None
    
    while alive > 1:
        for i in range(0, n):
            if a[i] == -1:
                if visited == k:
                    a[i] = nextAlive(a, i+1)
                    visited = 1
                    alive -= 1
                else:
                    visited += 1
                    lastVisited = i+1
            else:
                i = nextAlive(a, i)
    print("Result: ", lastVisited)

def josephus3SCOzDBG(n, k):
    a = np.full(n, -1)
    visited = 1
    alive = n
    lastVisited = None
    
    while alive > 1:
        for i in range(0, n):
            if a[i] == -1:
                if visited == k:
                    a[i] = nextAlive(a, i+1)
                    print("a[",i,"] set to ", a[i], sep='')
                    visited = 1
                    alive -= 1
                else:
                    visited += 1
                    lastVisited = i+1
            else:
                i = nextAlive(a, i)
                print("i set to ", i, sep='')
    print("Result: ", lastVisited)
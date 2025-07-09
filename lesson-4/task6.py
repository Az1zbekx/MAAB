for i in range(2, 101):  
    b = True
    for j in range(2, i):
        if i % j == 0:
            b = False
            break
    if b:
        print(i, end=' ')

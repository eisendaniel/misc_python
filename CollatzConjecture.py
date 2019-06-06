for i in range(1, 11):
    while i > 1:
        print(i)
        if i % 2 == 0:
            i *= 0.5
        else:
            i = 3*i + 1
    print(i, end='\n\n')

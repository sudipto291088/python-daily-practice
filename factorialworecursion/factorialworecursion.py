def factworecursion(a):
    l = a
    if a>1:
        while a>1:
            a = a-1
            print(l,'*',a,'=',l*a)
            l = l*a
    else:
        print(1)

m = int(input('Enter a number to find the factorial: '))
factworecursion(m)
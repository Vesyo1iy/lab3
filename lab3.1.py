def triangle():
    a = int(input())
    b = int(input())
    c = int(input())
    if a + b > c and a + c > b and b + c > a:
        print('Можно')
    else:
        print('Нельзя')
triangle()
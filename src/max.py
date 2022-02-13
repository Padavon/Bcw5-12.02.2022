if __name__ =='__main__':
    num = input()
    num.strip()

    num = num.split()
    num = list(map(int, num))

    a, b, c, d, e = num

    if a >= b & a >= c & a >= d & a >= e:
        print(a)
    elif b >= a & b >= c & b >= d & b >= e:
        print(b)
    elif c >= a & c >= b & c >= d & c >= e:
        print(c)
    elif d >= a & d >= b & d >= c & d >= e:
        print(d)
    else:
        print(e)

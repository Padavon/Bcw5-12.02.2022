def array_scan():
    return [int(n) for n in input().strip().split()]


def array_print(array):
    out = [str(n) for n in array]
    out = ' '.join(out)
    print(out)


def array_increment(array):
    for i in range(len(array)):
        array[i] += 1


if __name__ == '__main__':
    arr = array_scan()
    array_increment(arr)
    array_print(arr)


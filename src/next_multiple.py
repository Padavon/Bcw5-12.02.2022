if __name__ == "__main__":
    num = input()
    num.strip()

    res = None

    num = num.split()
    num = list(map(int, num))

    divident, divisor = num

    if divisor < 0:
        divisor *= -1

    res = divident % divisor

    if res > 0:
        divident += divisor

    result = divident - res

    print(result)
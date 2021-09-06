# print each number from A to B (including)
def one():
    a = int(input("a: "))
    b = int(input("b: "))
    for i in range(a, b + 1):
        print(i)


#   [print(i) for i in range(int(input("a: ")), int(input("b: ")) + 1)]


# print each number from A to B (including) if its digits sum equals R
def two():
    def s_digit(num):
        return sum(map(int, str(num)))

    r = int(input("r: "))

    a = int(input("a: "))
    b = int(input("b: "))

    for i in range(a, b + 1):
        if s_digit(i) == r:
            print(i)


#   (lambda r, a, b: [print(i) for i in range(a, b + 1) if (r == sum(map(int, str(i))))])(int(input("r: ")), int(input("a: ")), int(input("b: ")))


# print each number from A to B (including) if it is palindrome and it contains three equal digits
def three():
    def check_digit_count(num, count):
        return len([i for i in range(10) if (str(num).count(str(i)) == count)]) > 0

    a = int(input("a: "))
    b = int(input("b: "))

    for i in range(a, b + 1):
        if check_digit_count(i, 3) and str(i) == str(i)[::-1]:
            print(i)

#   [print(i) for i in range(int(input("a: ")), int(input("b: ")) + 1) if (lambda num, count: len([i for i in range(10) if (str(num).count(str(i)) == count)]) > 0)(i, 3) and str(i) == str(i)[::-1]]

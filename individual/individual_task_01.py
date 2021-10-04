def task01():
    n = int(input("N:"))
    number_list = [int(input()) for _ in range(n)]
    digit_map = {}

    for number in number_list:
        for digit in hex(number)[2:]:
            if digit in digit_map:
                digit_map[digit] += 1
            else:
                digit_map[digit] = 1

    print("Digits: ", digit_map)

    even_odd_list = list(map(lambda x: x % 2, digit_map.values()))
    odd = even_odd_list.count(1)
    if odd <= 1:
        print(1)
    else:
        print(0)


task01()

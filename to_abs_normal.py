from itertools import product
from string import ascii_lowercase as alpha


def to_normal(a: list, b: list, n: int) -> (str, str):
    res_1, res_2 = [], []

    for row in range(2**n):
        buf_1, buf_2 = [], []
        if b[row]: 
            for i in range(n):
                buf_1 += [alpha[i]] if a[row][i] else ['!'+alpha[i]]
            res_1.append("(" + " & ".join(buf_1) + ")")

        else:
            for i in range(n):
                buf_2 += ["!"+alpha[i]] if a[row][i] else [alpha[i]]
            res_2.append("(" + " | ".join(buf_2) + ")")

    return " | ".join(res_1), " & ".join(res_2)  # СДНФ, СКНФ


def num_to_table(f: int, n: int) -> (tuple, tuple):
    b = list(map(int, list(bin(f)[2:].zfill(2**n))))
    a = [row for row in product((0, 1), repeat=n)]

    return a, b


def main():
    f = 145
    a, b = num_to_table(f, 3)
    dis, con = to_normal(a, b, 3)
    print("СДНФ:", dis)
    print("СКНФ:", con)


if __name__ == '__main__':
    main()

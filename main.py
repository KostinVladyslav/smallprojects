def chunks(lm, n):
    if len(lm) >= n:
        r = (lm[i:i + n] for i in range(0, len(lm), n))
        return r


def ZadNumber(number):
    a = float('{:.2f}'.format(number))
    return a


def funcsum(alist, blist):
    a = [x for x in alist if x not in blist]
    return a

# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    # 2 задание
    name = str(input('Введите имя = '))
    surname = str(input('Введите фамилию = '))
    print("Здраствуйте, {0} {1} ".format(name, surname))

    # 3 задание
    numberfloat = float(input("Введите число = "))
    v = ZadNumber(numberfloat)
    print(v)

    # 4 задание
    listb = ["price b", "hifu oejf", "dwhi price", "doekjdoj"]
    listtext = [x.upper() for x in listb if "price" in x]
    print(listtext)

    # 5 задание
    b = ['1', '2', '3']
    f = chunks(b, 2)
    print(f)

    # 6 задание
    listnames = "Денис, Олег, Вася, Петя,Дима,Женя"
    a = listnames.split(',')
    for i in range(len(a)):
        a[i] = a[i].strip()
    print(a)

    # 7 задание
    print(",".join(a))
    # 8 задание
    lm = []
    k = 0
    for i in lm:
        if int(i) == 777:
            break
        k += 1
        if k == 100:
            raise Exception("Sorry,k = 100")
    # 9 задание
    a = [1, 2, 3, 4, 5]
    b = [1, 2, 4, 5]
    d = funcsum(a, b)
    print(d)

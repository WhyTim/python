for i in range(1111):
    my_number = int(input())

    s11to19 = int(str(my_number)[-2:])
    if 11<=s11to19<=19:
        print(str(my_number) + ' дней назад')
        continue
    last_number = int(str(my_number)[-1])

    if last_number==1:
        print(str(my_number) + ' день назад')
    if 2<=last_number<=4:
        print(str(my_number) + ' дня назад')
    if 5<=last_number<=9 or last_number==0:
        print(str(my_number) + ' дней назад')

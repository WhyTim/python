import os
import shutil
import time

def check_identical_files(name_dir):
    # проверка на наличие одинакового файла, если есть - оставляем на месте
    link=str(b)+str(r'\{}'.format(name_dir))
    os.chdir(link)
    files2=os.listdir(path='.')
    for i in files2:
        if file==i:
            global next
            next=True
    os.chdir(b)

def ends(c):
    my_number = c
    s11to19 = int(str(my_number)[-2:])
    if 11<=s11to19<=19:
        print('Рабочий стол очищен от ' + str(my_number) + ' файлов!')
    else:

        last_number = int(str(my_number)[-1])

        if last_number==1:
            print('Рабочий стол очищен от ' + str(my_number) + ' файла!')
        if 2<=last_number<=4:
            print('Рабочий стол очищен от ' + str(my_number) + ' файлов!')
        if 5<=last_number<=9 or last_number==0:
            print('Рабочий стол очищен от ' + str(my_number) + ' файлов!')

c=0
a=os.getenv("USERPROFILE")
b=str(a)+str('\Desktop')
os.chdir(b)
files=os.listdir(path='.')
for file in files:

    if '.jpg' in file or '.png' in file:

        next=False

        check_identical_files(name_dir='1. screens')


        # если найдётся одинаковое имя файла, то при повторном перемещении выскочит ошибка
        # обходим её с помощью try, тем самым пропустив перемещение
        if next==True:
            pass
        else:
            try:
                shutil.copyfile(str(file), r'1. screens/{}'.format(str(file)))
                os.remove(file)
                print(file)
            except:
                print(file)
            c+=1

    if '.psd' in file:
        next=False

        check_identical_files(name_dir='2. photoshop')

        if next==True:
            pass
        else:
            try:
                shutil.copyfile(str(file), r'2. photoshop/{}'.format(str(file)))
                os.remove(file)
            except:
                pass
            c+=1

    if '.py' in file:
        next=False

        check_identical_files(name_dir='3. python')

        os.chdir(b)
        if next==True:
            pass
        else:
            try:
                shutil.copyfile(str(file), r'3. python/{}'.format(str(file)))
                os.remove(file)
            except:
                pass
            c+=1

    time.sleep(0.05)

print('---------------------------------')
ends(c)
print('---------------------------------')

#авто закрытие консоли через 3 секунды
for i in range(3):
    time.sleep(1)

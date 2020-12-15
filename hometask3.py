"""
Оба for, разобранные в предыдущем файле можно
использовать для создания новых списков,
например так мы создадим список состоящий
из 7 одинаковых чисел 18:
"""
l = []
for i in range(7):
    l.append(18)
print("Список из 18", l)
"""
А так создадим список из чисел
от 5 до 23. В этом нам поможет то,
что for и range меняют нам i
по определенным правилам и ими мы заполняем
новый список
"""
l = []
for i in range(5, 23):
    l.append(i)
print("Список с числами от 5 до 23\n", l)

"""
Вот пример заполнения списка отрицательными
числами
"""
l = []
for i in range(-10, 0):
    l.append(i)
print("Список с отрицательными числами\n", l)

"""
А вот с числами, идущими через 3
"""
l = []
for i in range(1, 25, 3):
    l.append(i)
print("Числа с шагом 3\n", l)


##########################################
# TODO задание 1
##########################################
"""Заполнить список числами от 5 до 17"""
print("Результат задания 1")
l = [] # здесь я задала пустой список за вас, но потом не забывайте делать это сами
# здесь ваш for
for i in range(5,18):
    l.append(i)
print(l)

##########################################
# конец задания
##########################################


"""
Помимо изменения правил по которым менякется i 
(это делается в range)
мы так же можем взаимодействовать с самим i
перед добавлением его в список
например увеличивать в 5 раз
"""
l = []
for i in range(0, 25):
    l.append(i*5)
print("Числа большие в 5 раз начальных\n", l)

##########################################
# TODO задание 2
##########################################
"""Заполнить список числами увеличенными в 3 раза
и с добавлением 7
(number*3 + 7)"""
print("Результат задания 2")
# здесь ваш код
for i in range(len(l)):
    l[i] = l[i]*3 + 7
print(l)

##########################################
# конец задания
##########################################


##########################################
# TODO задание 3 усложненное
##########################################
"""Придумайте как с помощью изученного
можно было бы заполнить список числами
101, 201, 301, 401, 501"""
print("Результат задания 3")
# здесь ваш код
l = []
for i in range(101,502,100):
    l.append(i)
print(l)

##########################################
# конец задания
##########################################

"""
Можно так же создавать списки на основе тех,
которые уже существуют используя вторую версию for,
например создадим список значения которого в 5 раз
больше значений из старого списка
"""
old_l = [3, 1, 4, 6, 2, 4, 6]
l = []
for i in old_l:
    l.append(i*5)
print("Числа большие в 5 раз начальных\n", l)

"""
Или список в котором числа на 1 меньше начальных
"""
old_l = [3, 1, 4, 6, 2, 4, 6]
l = []
for i in old_l:
    l.append(i-1)
print("Числа большие на 1 меньше начальных\n", l)

##########################################
# TODO задание 4
##########################################
"""Создать список на основе старого в котором
числа будут в 2 раза меньше"""
print("Результат задания 4")
old_l = [1, 2, 31, 12, 5, 3]
# здесь ваш код
new_l = []
for i in range(len(old_l)):
    new_l.append(old_l[i]/2)
print(new_l)

##########################################
# конец задания
##########################################

##########################################
# TODO задание 5 усложненное
##########################################
"""Создать список на основе старого в котором
числа будут двойками в степени старого числа"""
print("Результат задания 5")
old_l = [1, 2, 31, 12, 5, 3]
# здесь ваш код
new_l = []
for i in range(len(old_l)):
    new_l.append(2**old_l[i])
print(new_l)

##########################################
# конец задания
##########################################
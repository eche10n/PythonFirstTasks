"""
В течени практики, мы с вами учились писать
такие фигуры:
=
==
===
====
=====
Для этого мы выясняли какие символы в них есть,
сколько их и как они изменяются и использовали for
Например здесь быд такой код
"""
for i in range(1, 7):
    print(i*"=")
"""
а в таком случае
     =
    ==
   ===
  ====
 =====
======
код выглядед так:
(сколько-то пробелов + сколько-то '=')
"""
for i in range(1, 7):
    print((7-i)*" " + i*"=")


##########################################
# TODO задание 1
##########################################
"""Напищите код, изображающий фигуру
======
 =====
  ====
   ===
    ==
     =
     """
print("Результат задания 1")

# здесь ваш код
for i in range(6):
    print(" "*i + "="*(6-i))

##########################################
# конец задания
##########################################

##########################################
# TODO задание 2
##########################################
"""Напищите код, изображающий фигуру
    =    
   ===   
  =====  
 =======
=========
(подумайте о том, из сокольки частей состоит фигура,
например x*" " + y*"=" + z * " ")
     """
print("Результат задания 2")

"""у меня всегда не получаются такие задачи"""
"""всего 9 символов в строке, с каждым разом увеличиваем середину на 2"""
"""написал алгоритм и подобрал начальные значения, чтобы алгоритм работал"""
length = 10
root = -1
for i in range(5):
    length -= 2
    space = int(length/2)
    root +=2
    print(space*" " + root*"=" + space*" ")
# здесь ваш код


##########################################
# конец задания
##########################################


##########################################
# TODO задание 3
##########################################
"""Напищите код, изображающий фигуру
=========
 =======
  =====  
   ===
    =
     """
print("Результат задания 3")

# здесь ваш код
length = 9
space = 0
for i in range(6):
    print(space * " " + length * "=" + space * " ")
    length -= 2
    space +=1
##########################################
# конец задания
##########################################


##########################################
# TODO задание 4 дополнительное
##########################################
"""Напищите код, любую красивую фигуру по
вашему желанию
     """
print("Результат задания 4")
left = 0
right = 0
# здесь ваш код
for i in range(15):
    if i%2==0:
        left+=1
    else:
        right+=1
    print(" "*left + "#"* right)

##########################################
# конец задания
##########################################
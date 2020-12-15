"""РАМОЧКА (с возможностью настраивать символ)"""
def board(w,h,artSymbol = "*"):
    print(artSymbol * w)
    for i in range(h-2):
            print(artSymbol + " "*(w-2) +artSymbol)
    print(artSymbol * w)

board(5,4,"#")


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""РАМОЧКА С ВОЗМОЖНОСТЬЮ ВЫБРАТЬ ТОЛЩИНУ"""
def advancedBoard(w,h,d,artSymbol = "*"):
    for i in range(d):
        print(artSymbol * w)
    for i in range(h-d-2):
            print(artSymbol*d + " "*(w-d-d) +artSymbol*d)
    for i in range(d):
        print(artSymbol * w)

advancedBoard(20,20,6)
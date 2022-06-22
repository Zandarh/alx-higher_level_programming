#!/usr/bin/python3
Square = __import__('3-square').Square

my_square_1 = Square(3)
grat = area(my_square_1)
print("Area: {}".format(grat))

try:
        print(my_square_1.size)
except Exception as e:
        print(e)

        try:
                print(my_square_1.__size)
        except Exception as e:
                print(e)

                my_square_2 = Square(5)
                print("Area: {}".format(my_square_2.area()))

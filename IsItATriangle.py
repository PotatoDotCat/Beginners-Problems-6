def triangleTest(a, b, c):
    sides = [a, b, c]
    if sides[0] + sides[1] > sides[2]:
        return True
    else:
        return False

side1 = int(input("enter the first side length: "))
side2 = int(input("enter the second side length: "))
side3 = int(input("enter the third side length: "))

if triangleTest(side1, side2, side3):
    print("It's a triangle!")
else:
    print("It's not a triangle.")

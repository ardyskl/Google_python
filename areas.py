#!/usr/bin/env python3

#importing maths module
import math
import sys
import traceback

def main():
    try:

        print("Welcome to our simple Areas app!")

        def triangle(base, height):
            return (1/2 *base*height)

        def square(side):
            return side ** 2

        def circle(radius):
            return math.pi * (radius * radius)

        def rectangle(length, width):
            return length * width

        def pallelogram(base, height):
            return base * height

        def trapezoid(height, baseA, baseB):
            return (baseA + baseB)/2 * height

        def ellipse(radiusA, radiusB):
            return math.pi * (radiusA * radiusB)

        def cube(side):
            return 6 * (side ** 2)

        def sphere(radius):
            return (4 * math.pi) * (radius ** 2)

        def cylinder(radius, height):
            return 2 * (math.pi * radius ** 2) + (2 * math.pi * radius * height)

        def cone(radius, side):
            return math.pi * radius * side

        def torus(radiusR, radiusr):
            return (2 * math.pi * radiusR) * (2 * math.pi * radiusr)

        cont = "y"
        while(cont.lower() == "y"):

            choice = ['triangle', 'square', 'circle', 'torus', 'cone', 'cylinder', 'sphere', 'cube', 'ellipse', 'pallelogram', 'trapezoid', 'rectangle']
            for element in choice:
                print(element)

            choice_input = input("Please choose a shape: [use lowercase]: ")

            if choice_input == 'triangle':
                num1 = float(input("Enter base: "))
                num2 = float(input("Enter height: "))
                print("Area of the triangle = {0} meter square".format(triangle(num1, num2)))

            if choice_input == 'cone':
                num1 = float(input("Enter radius: "))
                num2 = float(input("Enter side: "))
                print("Area of the cone = {0} meter square".format(cone(num1, num2)))

            elif choice_input == 'trapezoid':
                num1 = float(input("Enter height: "))
                num2 = float(input("Enter first base: "))
                num3 = float(input("Enter second base: "))
                print("Area of the trapezoid = {0} meter square".format(trapezoid(num1, num2, num3)))

            elif choice_input == 'cube':
                num1 = float(input("Enter side: "))
                print("Area of the cube = {0} meter square".format(cube(num1)))

            elif choice_input == 'square':
                num1 = float(input("Enter side: "))
                print("Area of the square = {0} meter square".format(square(num1)))

            elif choice_input == 'sphere':
                num1 = float(input("Enter radius: "))
                print("Area of the sphere = {0} meter square".format(sphere(num1)))

            elif choice_input == 'circle':
                num1 = float(input("Enter radius: "))
                print("Area of the circle = {0} meter square".format(circle(num1)))

            elif choice_input == 'pallelogram':
                num1 = float(input("Enter base: "))
                num2 = float(input("Enter height: "))
                print("Area of the pallelogram = {0} meter square".format(pallelogram(num1, num2)))

            elif choice_input == 'rectangle':
                num1 = float(input("Enter length: "))
                num2 = float(input("Enter width: "))
                print("Area of the rectangle = {0} meter square".format(rectangle(num1, num2)))

            elif choice_input == 'ellipse':
                num1 = float(input("Enter value of first radius: "))
                num2 = float(input("Enter value of second radius: "))
                print("Area of ellipse = {0} meter square".format(ellipse(num1, num2)))

            elif choice_input == 'torus':
                num1 = float(input("Enter value of major radius (R): "))
                num2 = float(input("Enter value of minor radius (r): "))
                if num1 > num2:
                    print("Area of torus = {0} meter square".format(torus(num1, num2)))
                else:
                    print("Invalid input: make sure R > r")

            elif choice_input == 'cylinder':
                num1 = float(input("Enter value of radius: "))
                num2 = float(input("Enter value of height: "))
                print("Area of cylinder = {0} meter square".format(cylinder(num1, num2)))

            else:
                print("Please choose a shape from options")


            cont = input("Do you want to calculate the area of another shape? [y to continue] & [n to exit]: ")

            if cont == "n":
                print("Thanks for using our Areas app!")
                quit()

    except KeyboardInterrupt:
        print("\n--- Shutdown requested exiting ---")

    except Exception:
        traceback.print_exc(file=sys.stdout)
        sys.exit(0)

if __name__ == "__main__":
    main()

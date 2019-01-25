# HOMEWORK 2 --- ES2
# Triangle Calculator

# FILL THESE COMMENTS IN
#*****************************************
# YOUR NAME: Patrick Wright
# NUMBER OF HOURS TO COMPLETE: 1.5, 2-2.5 with extra credit (please track how long this homework takes you to complete).
# YOUR COLLABORATION STATEMENT(s) (refer to syllabus): None
#
#*****************************************

#In this homework,the ultimate goal is to create a function called areaofatriangle,
#which takes six parameters which represent three intersecting lines
#of the form y = (m * x) + b that mark the three sides of the triangle.

#In order to accomplish this you will need functions which determine
#where two lines intersect (x and y), a function which determines the distance between
#two points represented by (x,y) coordinates, and a function which determines
#the area of a triangle using three side lengths(using Heron's Formula).

#Please complete the four required functions below:

import math #This line allows you to use math functions. Importantly, math.sqrt(#) which will produce the square root of the number inside the parentheses.


def intersectionoftwolines_x(m1, b1, m2, b2):
    # Calculate x for the point where two equations:
    # y = (m1 * x) + b1 and y = (m2 * x) + b2 intersect.
    # m1 * x - m2 * x = b2 - b1
    # x(m1 - m2) = (b2 - b1)
    # x = (b2 - b1)/(m1 - m2)

    # EC: The lines will not intersect if they are parallel; this occurs when m1 = m2.
    # EC: I will create an error message for this using if statements
    if m1 == m2:
        print("Lines are parallel -- no intersection!")
    else:
        x = (b2 - b1)/(m1 - m2) #replace this with your calculation for x
        return x

def intersectionoftwolines_y(m1, b1, m2, b2):
    # Calculate y for the point where two equations:
    # y = (m1 * x) + b1 and y = (m2 * x) + b2 intersect.
    #Since I know that y = m1 * x + b1, I can simply plug in x to find the y value at which they intersect

    # EC: I will copy the same code to test for parallelness above because it applies in the same way
    if m1 == m2:
        print("Lines are parallel -- no intersection!")
    else:
        y = (m1 * (b2 - b1)/(m1 - m2)) + b1 #replace this with your calculation for y
        return y


def distancebetweenpoints(x1, y1, x2, y2):
    # Calculate the linear distance between two points
    # (x1, y1) and (x2, y2).
    # This is a pythagorean thm. problem. I will use D = math.sqrt(a^2 + b^2)...
    # Where a and b are the horizontal and vertical distances between the points.
    # a (horizontal dist.) = (x2 - x1)
    # b (vertical dist.) = (y2 - y1)
    # Therefore D = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) # replace with your calculation for distance
    return distance

def heronsformula(a, b, c):
    # Calculate the area of a triangle with three known side lengths.
    # You may want to look up Heron's formula online.
    # Heron's formula states that:
    # Atriangle = math.sqrt(s*(s-a)*(s-b)*(s-c)) where s is defined as...
    # s = (a + b + c)/2
    # To find the area using Heron's formula, I will define the variable s as (a + b + c)/2
    # Then I will use the s variable in the area = statement below

    s = (a + b + c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c)) #replace this with your calculation for area
    return area

def areaofatriangle(m1, b1, m2, b2, m3, b3):
    # Using the three functions above, now calculate the area of a
    # triangle when the three sides are described by three linear equations
    # y = (m1 * x) + b1;  y = (m2 * x) + b2; and y = (m3 * x) + b3
    # First I will find the x-coords of the 3 possible intersections and store them as variables i1x, i2x, and i3x.
    # I solved for the general equation of intersections earlier, so I will use my previous result in these new cases
    # EC: before I assign variables, I will check for parallelness
    if m1 == m2 or m1 == m3 or m2 == m3:
        print("1 or more lines are parallel -- do not intersect to form a triangle!")
    else:
        i1x = (b2 - b1)/(m1 - m2) # Intersection of first (m1, b1) and second (m2, b2) lines
        i2x = (b3 - b1)/(m1 - m3) # Intersection of first (m1, b1) and third (m3, b3) lines; follows same form as above
        i3x = (b3 - b2)/(m2 - m3) # Intersection of second (m2, b2) and third (m3, b3) lines
        # To define the values for y-coordinates of the intersections, I will use variables i1y, i2y, and i3y
        # As I did above, I will simply plug the inx values into y = mn * x + bn to find iny
        i1y = (m1 * i1x) + b1   # I use the m and b values for line 1 because the intersection occurs on line 1
        i2y = (m1 * i2x) + b1   # I use the m and b values for line 1 because the intersection occurs on line 1 (even though line 3 is involved)
        i3y = (m3 * i3x) + b3   # I use the m and b values for line 3 because the intersection occurs on line 3

    # Now I have to calculate the distance between 3 points: 1: (i1x, i1y), 2: (i2x, i2y), and 3: (i3x, i3y)
    # I already know the distance formula (defined above), so I will use it again.
    # I will define a as the distance between points 1 and 2; b between 1 and 3; and c between 2 and 3
    a = math.sqrt((i2x - i1x)**2 + (i2y - i1y)**2)
    b = math.sqrt((i3x - i1x)**2 + (i3y - i1y)**2)
    c = math.sqrt((i3x - i2x)**2 + (i3y - i2y)**2)

    # Now that I have 3 side lengths, I can use Herod's formula to calculate area as I have done above
    s = (a + b + c)/2
    # I will define my area below as the final step in Herod's formula

    # EC: the lines all intersect at one point iff i1x == i2x == i3x and i1y == i2y == i3y
    # EC: I will set up a conditional error statement for this case
    if i1x == i2x == i3x and i1y == i2y == i3y:
        print("Lines intersect at one point -- no triangle formed!")
    else:
        area = math.sqrt(s*(s-a)*(s-b)*(s-c)) #replace this with your calculation for area
        return area


#TEST CASES
#These print statements will be true when your functions are working.

print("Distance between Points:")
#If these are both true, it is likely that your function is working.
print(distancebetweenpoints(0, 0, 3, 4) == 5)
print(distancebetweenpoints(0, 0, 1, 1) == math.sqrt(2))
print("*********")

print("Intersection of Two Lines:")
#If these are all true, it is likely that your function is working.
print(round(intersectionoftwolines_x(3, -3, 2.3, 4),2) == 10)
print(round(intersectionoftwolines_y(3, -3, 2.3, 4),2) == 27)
print(round(intersectionoftwolines_x(10, 10, 30, 0),2) == .5)
print(round(intersectionoftwolines_y(10, 10, 30, 0),2) == 15)
print("*********")

print("Heron's Formula:")
print(round(heronsformula(5, 5, 8), 2) == 12)
print(round(heronsformula(5, 5, 6), 2) == 12)
print("*********")

print("Area of a Triangle:")
#If these are both true, it is likely that your function is working.
print(round(areaofatriangle(10, 10, 20, 0, 30, 0),2) == 2.5)
print(round(areaofatriangle(0, 0, 1, 0, -1, 10),2) == 25)
print("*********")
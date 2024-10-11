x = int(input("Enter the x-coordinate: "))
y = int(input("Enter the y-coordinate: "))

if x > 0 and y > 0:
    print("point (", x, ",", y,") lies in the 1st quadrant.")
elif x < 0 and y > 0:
    print("point (", x, ",", y,") lies in the 2nd quadrant.")
elif x < 0 and y < 0:
    print("point (", x, ",", y,") lies in the 3rd quadrant.")
elif x > 0 and y < 0:
    print("point (", x, ",", y,") lies in the 4th quadrant.")
elif x == 0 and y == 0:
    print("point (", x, ",", y,") lies in the origin.")
elif x == 0:
    print("point (", x, ",", y,") lies on the x-axis")
elif y == 0:
    print("point (", x, ",", y,") lies on the y-axis")
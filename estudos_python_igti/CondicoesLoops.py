""" IF ELIF LOOPs(FOR) WHILE """

# IF
x = 100
y = 35
if x > y:
    print("X é > que Y - O valor de X é:", x)


# ELIF
x = 35
y = 35
if x > y:
    print("X é > que Y - O valor de X é:", x)
elif x == y:
    print("X é = a Y  - O valor de X é:", x )


# LOOPs (FOR , BRAKE, RANGE)
x = (1, 2, 3, 4, 5, 6, 7, 8, 9)
for i in x:
    print(i)
    if i >= 5:
        print("i >= 5 : Pausado")
        break


for i in range(1,12):
    print(i)

# WHILE
i = 1
while i < 15:
    print(i)
    i += 1




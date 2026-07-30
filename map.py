import math

minimum = math.inf
maximum = -math.inf

while True:

    n = float(input("Enter a value (0 to 1): "))

    if n < minimum:
        minimum = n

    if n > maximum:
        maximum = n

    print("Minimum =", minimum)
    print("Maximum =", maximum)

    if minimum != maximum:

        angle = ((n - minimum) * 180) / (maximum - minimum)

        print("Angle =",angle, "°")
    else:
        print("Need another different value")


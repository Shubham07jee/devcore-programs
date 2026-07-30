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

# Output:

# Enter a value (0 to 1): 0.5
# Minimum = 0.5
# Maximum = 0.5
# Need another different value

# Enter a value (0 to 1): 0.8
# Minimum = 0.5
# Maximum = 0.8
# Angle = 180.0 °

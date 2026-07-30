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

# """
#Output
# Enter a value (0 to 1): 0.8
# Minimum = 0.8
# Maximum = 0.8

# Enter a value (0 to 1): 0.6
# Minimum = 0.6
# Maximum = 0.8

# """

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

    # choice = input("Continue? (y/n): ").lower()
    # if choice != 'y':
    #     break
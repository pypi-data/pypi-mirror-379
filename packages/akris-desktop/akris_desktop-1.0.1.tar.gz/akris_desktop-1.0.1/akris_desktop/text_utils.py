import random


def colorize(speaker):
    # Set the seed based on the peer name
    random.seed(speaker)

    # Generate random RGB values for lighter colors
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    # Generate the color code
    color_code = "#{:02X}{:02X}{:02X}".format(r, g, b)

    return color_code

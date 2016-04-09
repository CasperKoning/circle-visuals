from math import sqrt


def in_circles(x, y, r1, r2, x_center, y_center):
    """Determines whether or not a pixel [x,y] is contained within two circles of radius r1 and r2,
    spanned from the center of an image with center pixel [x_center, y_center]
    :param x: x coordinate of the pixel
    :param y: y coordinate of the pixel
    :param r1: radius of the inner circle
    :param r2: radius of the outer circle
    :param x_center: x coordinate of the center of the image
    :param y_center: y coordinate of the center of the image
    :return: True if pixel is contained within the two circles
    """
    x_dist = abs(x-x_center)
    y_dist = abs(y-y_center)
    r = sqrt(x_dist*x_dist + y_dist*y_dist)
    return r1 < r < r2

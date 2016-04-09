import argparse
import os.path
import random
import string

p = argparse.ArgumentParser(description="write some image on top of another, but contained within two circles")
p.add_argument("general_image_path", help="the path of the general image")
p.add_argument("circle_image_path", help="the path of the image in the circle")
p.add_argument("-r1", "--inner_radius", help="inner circle radius, defaults to 0", type=int, default=0)
p.add_argument("-r2", "--outer_radius", help="outer circle radius, defaults to 0", type=int, default=0)
p.add_argument("-o", "--output", help="the output path, defaults to a randomly generated filename in current folder")
__args = p.parse_args()


def validate_input():
    assert(inner_radius >= 0)
    assert(inner_radius <= outer_radius)
    assert(os.path.isfile(general_image_path))
    assert(os.path.isfile(circle_image_path))


def read_output_image_path():
    if __args.output:
        return __args.output
    else:
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(10)) + ".jpg"


inner_radius = __args.inner_radius
outer_radius = __args.outer_radius
general_image_path = __args.general_image_path
circle_image_path = __args.circle_image_path
output_path = read_output_image_path()
validate_input()

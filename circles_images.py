import argparams
import circle_utils
try:
    import Image
except ImportError:
    from PIL import Image


def main():
    print("Opening circle image...")
    circle_image = Image.open(argparams.circle_image_path)
    circle_image.convert('RGBA')
    data_circle = circle_image.load()

    print("Opening general image...")
    general_image = Image.open(argparams.general_image_path)
    general_image.convert('RGBA')
    data_general = general_image.load()

    print("Combining images...")
    pixels = []
    width = general_image.size[0]
    height = general_image.size[1]
    for y in range(height):
        pixels.append([])
        for x in range(width):
            if circle_utils.in_circles(x, y, argparams.inner_radius, argparams.outer_radius, width/2, height/2):
                pixels[y].append(data_circle[x, y])
            else:
                pixels[y].append(data_general[x, y])
    combined_image = Image.new('RGBA', general_image.size)
    for y in range(height):
        for x in range(width):
            combined_image.putpixel((x, y), pixels[y][x])

    print("Saving output...")
    combined_image.save(argparams.output_path)


if __name__ == '__main__':
    main()

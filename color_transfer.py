import sys
import random
from PIL import Image

def color_transfer(image_path, color_replace_dict):
    im = Image.open(image_path)
    pixel_data = im.load()
    colors = im.getcolors()
    new_color_dict = {}

    if color_replace_dict and all(color_replace_dict.values()):
        new_color_dict = color_replace_dict
    else:
        for i in range(len(colors)):
            color = colors[i][1]
            if color != (0, 0, 0, 255):
                R = random.randint(0, 255)
                G = random.randint(0, 255)
                B = random.randint(0, 255)
                new_color_RGB = (R, G, B, 255)
                new_color_dict[color] = new_color_RGB

    for x in range(im.size[0]):
        for y in range(im.size[1]):
            pixel_color = pixel_data[x, y]
            if pixel_color != (0, 0, 0, 255) and pixel_color != (0, 0, 0, 0):
                pixel_data[x, y] = new_color_dict[pixel_color]
    return im

if __name__ == '__main__':
    original_image_path = sys.argv[1]
    new_image_path = sys.argv[2]
    color_replace_dict = {
            (118, 228, 250, 255): (225, 225, 139, 255),
            (28, 57, 83, 255): (138, 94, 13, 255),
            (17, 107, 162, 255): (3, 91, 117, 255),
            (245, 254, 254, 255): (0, 128, 178, 255),
            (64, 112, 144, 255): (246, 254, 251, 255),
            (1, 184, 253, 255): (254, 229, 8, 255),
            (24, 22, 23, 255): (24, 16, 13, 255),
            (0, 0, 0, 255): (0, 0, 0, 255)
            }
    using_random_color = 0
    if len(sys.argv) > 3:
        using_random_color = int(sys.argv[3])
    if using_random_color:
        im = color_transfer(original_image_path, None)
    else:
        im = color_transfer(original_image_path,color_replace_dict)
    im.show()
    im.save(new_image_path)

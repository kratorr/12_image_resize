from PIL import Image
import argparse
#width, height


def resize_image_scale(image, scale):
    new_size = tuple(map(lambda size: int(size*scale), image.size))
    return image.resize(new_size)


def resize_image_with_one_side(image, **kwargs):
    image_width, image_height = image.size
    if kwargs.get("width"):
        new_width = kwargs["width"]
        coefficient = (new_width / image_width)
    else:
        new_height = kwargs["height"]
        coefficient = (new_height / image_height)
    new_size = tuple(map(lambda size: int(size*coefficient), image.size))
    return image.resize(new_size)


def resize_image_with_two_side(image, new_width, new_height):
    return image.resize((new_width, new_height))


if  __name__ == "__main__":
    path_to_original = "1.png"
    path = "4.png"
    input_image = Image.open(path_to_original)
    #x = resize_image_with_1side(input_image, width=120)
    #resize_image_with_1side(input_image, height=300)
    x = resize_image_with_two_side(input_image, 480, 365)
    #resized_image = resize_image_scale(input_image, 60)
    #resized_image.save(path)
    #coefficient_width = new_width / image_width
    #coefficient_height = new_height / image_height

    #print(coefficient_width, coefficient_height)
    #print(x)
    x.save(path)
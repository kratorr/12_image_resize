from PIL import Image
import argparse
import os


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scale", type=float)
    parser.add_argument("--width", type=int)
    parser.add_argument("--height", type=int)
    parser.add_argument("input_file")
    parser.add_argument("output_file", nargs="?")
    return parser


def resize_image_scale(image, scale):
    new_size = tuple(map(lambda size: int(size*scale), image.size))
    return image.resize(new_size), new_size


def resize_image_with_one_side(image, **kwargs):
    image_width, image_height = image.size
    if kwargs.get("width"):
        new_width = kwargs["width"]
        coefficient = (new_width / image_width)
    else:
        new_height = kwargs["height"]
        coefficient = (new_height / image_height)
    new_size = tuple(map(lambda size: int(size*coefficient), image.size))
    return image.resize(new_size), new_size


def resize_image_with_two_side(image, new_width, new_height):
    return image.resize((new_width, new_height)), (new_width, new_height)


def get_new_file_name_with_ext(input_name, size):
    filename, file_extension = os.path.splitext(input_name)
    print(filename, file_extension)
    return str(filename+"__"+str(size[0])+"x"+str(size[1])+file_extension)


if __name__ == "__main__":
    arg_parser = create_parser()
    arg_namespace = arg_parser.parse_args()

    try:
        input_image = Image.open(arg_namespace.input_file)
    except FileNotFoundError:
        exit("File not found")

    if arg_namespace.scale:
        resized_image, new_size = resize_image_scale(
            input_image, arg_namespace.scale
        )
    elif arg_namespace.height and arg_namespace.width:
        resized_image, new_size = resize_image_with_two_side(
            input_image, arg_namespace.width, arg_namespace.height
        )
    elif arg_namespace.height or arg_namespace.width:
        sizes = {"height":arg_namespace.height, "width":arg_namespace.width}
        resized_image, new_size = resize_image_with_one_side(
            input_image, **sizes
        )
    else:
        print("Not enough arguments")

    if arg_namespace.output_file:
        try:
            resized_image.save(arg_namespace.output_file)
        except KeyError:
            exit("Input output filename with extansion")
    else:
        new_file_name = str(get_new_file_name_with_ext(
            arg_namespace.input_file, new_size)
        )
        resized_image.save(new_file_name, format=None)


    #resized_image.save(path)
    #coefficient_width = new_width / image_width
    #coefficient_height = new_height / image_height


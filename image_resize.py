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


def resize_image_scale(image, size_dict):
    new_size = tuple(map(lambda size: int(size * size_dict["scale"]), image.size))
    return image.resize(new_size)


def resize_image_with_one_side(image, size_dict):
    image_width, image_height = image.size
    if size_dict.get("width"):
        new_width = size_dict["width"]
        coefficient = (new_width / image_width)
    else:
        new_height = size_dict["height"]
        coefficient = (new_height / image_height)
    new_size = tuple(map(lambda size: int(size * coefficient), image.size))
    return image.resize(new_size)


def resize_image_with_two_side(image, size_dict):
    return image.resize((size_dict["width"], size_dict["height"]))


def get_new_file_name_with_ext(arg_namespace, size_dict):
    if arg_namespace.output_file:
        return arg_namespace.output_file
    else:
        filename, file_extension = os.path.splitext(arg_namespace.input_file)
        return filename + "__" + str(size_dict["width"]) + \
               "x" + str(size_dict["height"]) + file_extension


def get_func_to_resize(arg_namespace):
    if arg_namespace.scale:
        return resize_image_scale
    elif arg_namespace.height and arg_namespace.width:
        return resize_image_with_two_side
    elif arg_namespace.height or arg_namespace.width:
        return resize_image_with_one_side


def aspect_ratio_is_saved(image, size_dict):
    original_width, original_height = image.size
    coefficient_width = size_dict["width"] / original_width
    coefficient_height = size_dict["height"] / original_height
    if coefficient_width == coefficient_height:
        return True


if __name__ == "__main__":
    arg_parser = create_parser()
    arg_namespace = arg_parser.parse_args()
    try:
        input_image = Image.open(arg_namespace.input_file)
    except FileNotFoundError:
        exit("File not found")
    resize_func = get_func_to_resize(arg_namespace)
    new_size_dict = {
        "width": arg_namespace.width,
        "height": arg_namespace.height,
        "scale": arg_namespace.scale
    }
    resize_func = get_func_to_resize(arg_namespace)
    if resize_func == resize_image_with_two_side:
        if not aspect_ratio_is_saved(input_image, new_size_dict):
            print("Aspect ratio does not match the original image")
    resized_image = resize_func(input_image, new_size_dict)
    resized_image.save(get_new_file_name_with_ext(arg_namespace, new_size_dict))



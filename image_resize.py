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


def get_new_file_name_with_ext(arg_namespace, size):
    if arg_namespace.output_file:
        return arg_namespace.output_file
    else:
        filename, file_extension = os.path.splitext(arg_namespace.input_file)
        res_str = str(size[0]) + "x" + str(size[1])
        file_name_with_ext = "{filename}__{res_str}{ext}".format(
            filename=filename,
            res_str=res_str,
            ext=file_extension
        )
        return file_name_with_ext


def get_new_size(arg_namespace, input_image_size):
    if arg_namespace.scale:
        new_size = (
            int(input_image_size["width"]*arg_namespace.scale),
            int(input_image_size["height"]*arg_namespace.scale)
        )
    elif arg_namespace.height and arg_namespace.width:
       new_size = (arg_namespace.width, arg_namespace.height)
    elif arg_namespace.height or arg_namespace.width:
        if arg_namespace.width:
            coefficient = (arg_namespace.width / input_image_size["width"])
        else:
            coefficient = (arg_namespace.height / input_image_size["height"])
        new_size = (
            int(input_image_size["width"] * coefficient),
            int(input_image_size["height"] * coefficient)
        )
    return new_size


def is_aspect_ratio_saved(input_image_size_dict, new_size):
    width, height = new_size
    coefficient_width = width / input_image_size_dict["width"]
    coefficient_height = height / input_image_size_dict["height"]
    return coefficient_width == coefficient_height


if __name__ == "__main__":
    arg_parser = create_parser()
    arg_namespace = arg_parser.parse_args()
    try:
        input_image = Image.open(arg_namespace.input_file)
    except FileNotFoundError:
        exit("File not found")
    original_image_width, original_image_height = input_image.size
    input_image_size_dict = {
        "width": original_image_width,
        "height": original_image_height
    }
    new_size = get_new_size(arg_namespace, input_image_size_dict)
    resized_image = input_image.resize(new_size)
    if arg_namespace.width and arg_namespace.height:
        if not is_aspect_ratio_saved(input_image_size_dict, new_size):
            print("Aspect ratio does not match the original image")
    resized_image.save(get_new_file_name_with_ext(arg_namespace, new_size))

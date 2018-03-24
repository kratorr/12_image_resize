# Image Resizer

Program for resizing images. The program has 3 types of resizing by scale, by width or height and by both sides.

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:
```bash
pip install -r requirements.txt # alternatively try pip3
```
Remember, it is recommended to use virtualenv/venv for better isolation.

# Quickstart

The program must be run using the console, required argument is path to image. If you do not specify a path to the output file, the file will be created in the same directory.

How to run:
```bash
$ python3 image_resize.py --scale 2 image_file resied_file
```
Example, a picture size of 200x100, at the output we get resized.jpg a scaled image(400x200):
```bash
$ python3 image_resize.py --scale 2 img.jpg resized.jpg
```
Example, a picture size of 200x100, at the output we get img__300x500.jpg file.
```bash
$ python3 image_resize.py --width 300 --height 500 img.jpg
```
Example, a picture size of 400x200, at the output we get img__800x400.jpg file with original aspect ratio.
```bash
$ python3 image_resize.py --width 800 img.jpg
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

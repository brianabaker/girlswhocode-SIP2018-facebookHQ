# Rename this file to be "filters.py"
# Add commands to import modules here.

from PIL import Image


def load_img(filename):
    im = Image.open(filename)
    return im


def show_img(im):
    im.show()


def save_img(im, filename):
    im.save(filename)
    show_img(im)

# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(im):

    pixels = im.getdata()

    new_pixels = []

    darkBlue = (0, 51, 76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)

    for pixel in pixels:

        intensity = pixel[0] + pixel[1] + pixel[2]

        if intensity < 182:
            new_pixels.append(darkBlue)

        elif intensity >= 182 and intensity < 364:
            new_pixels.append(red)

        elif intensity >= 364 and intensity < 546:
            new_pixels.append(lightBlue)

        elif intensity >= 546:
            new_pixels.append(yellow)

    new_image = Image.new("RGB", im.size)
    new_image.putdata(new_pixels)
    return new_image

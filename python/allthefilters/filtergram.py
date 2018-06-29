import filters



def main():
    filename = input('Enter the name of the image file to edit: ')

    img = filters.load_img(filename)

    obamicon_image = filters.obamicon(img)

    filters.save_img(obamicon_image, "recolored.jpg")

if __name__ == '__main__':
    main()

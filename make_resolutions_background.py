import Image


def make_image(name, size, ext):
    targetImage = Image.new("RGB", size, (71, 134, 21))

    bandWidth = 10
    centerColorBoundWidth = 2

    w = size[0]
    h = size[1]
    max_x = w - 1
    max_y = h - 1

    def is_band(x, y):
        return 0 <= x and x < bandWidth or max_x - bandWidth <= x and x <= max_x or 0 <= y and y < bandWidth or max_y - bandWidth <= y and y <= max_y

    for x in range(w):
        for y in range(h):
            if is_band(x, y):
                targetImage.putpixel((x, y), (127, 0, 0))

    filename = name + "." + ext
    targetImage.save(filename, "png")


if __name__ == '__main__':

    image_names = ["bg240x160", "bg~iphone", "bg~ipad", "bg@2x~iphone", "bg@2x~ipad"]
    sizes = [(240, 160), (480, 320), (1024, 768), (960, 640), (2048, 1536)]

    for i in range(len(image_names)):
        make_image(image_names[i], sizes[i], "png")

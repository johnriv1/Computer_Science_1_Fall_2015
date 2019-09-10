from PIL import Image

def make_square(image):
    w,h = image.size
    if w>h:
        image = image.crop((0,0,h,h))
    else:
        image = image.crop((0,0,w,w))
    return image    
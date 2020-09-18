import random
from PIL import Image, ImageDraw, ImageFilter

WHITE = (255, 255, 255)
BLACK = (54, 53, 71)
GREY = (242, 248, 255)
GREEN = (81, 119, 46)
ORANGE = (230, 160, 75)
SIZE = 250


def mask_circle_transparent(pil_img, blur_radius, offset=0):
    offset = blur_radius * 2 + offset
    mask = Image.new("L", pil_img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((offset, offset, pil_img.size[0] - offset, pil_img.size[1] - offset), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))
    result = pil_img.copy()
    result.putalpha(mask)

    return result


def generate_random_image():
    colors = [BLACK, GREY, GREEN, ORANGE]
    circles = ['a', 'b', 'c', 'd']

    im = Image.new('RGB', (SIZE, SIZE), WHITE)
    draw = ImageDraw.Draw(im)
    base_color = random.choice(colors)
    draw.ellipse((0, 0, SIZE, SIZE), fill=base_color, outline=base_color)
    colors.remove(base_color)

    for i in range(3):
        color = random.choice(colors)
        x = random.randint(int(SIZE / 4), int(SIZE / 1.7))
        y = random.randint(int(SIZE / 2.2), int(SIZE / 1.2))
        r = random.choice(circles)
        if r == 'a':
            draw.chord((-SIZE, -SIZE, y, y), start=0, end=360, fill=color, outline=color)
        elif r == 'b':
            draw.chord((-SIZE, x, y, SIZE * 2), start=0, end=360, fill=color, outline=color)
        elif r == 'c':
            draw.chord((x, -SIZE, SIZE * 2, y), start=0, end=360, fill=color, outline=color)
        else:
            draw.chord((x, x, SIZE * 2, SIZE * 2), start=0, end=360, fill=color, outline=color)
        circles.remove(r)
        colors.remove(color)

    im_thumb = mask_circle_transparent(im, 0)
    im_thumb.save('pillow_imagedraw.png', quality=100)


if __name__ == "__main__":
    generate_random_image()

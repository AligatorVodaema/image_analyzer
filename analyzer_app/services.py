from PIL import Image


WHITE_PIXEL_IN_PNG = (255, 255, 255, 255)
BLACK_PIXEL_IN_PNG = (0, 0, 0, 255)
WHITE_PIXEL_IN_JPG = (0, 0, 0)
BLACK_PIXEL_IN_JPG = (255, 255, 255)


def check_mode_of_image_and_convert(image):
    """Сheck mod image. Based on mod turn convertation mod.
    Return pillow instance."""

    img = Image.open(image)

    if img.mode in ('P', 'L'):
        img = img.convert('RGBA')
    return img

def count_pixels_from_image(image):
    """Open image in pillow and convert to RGB for counting black
    and white pixels."""
    
    img = check_mode_of_image_and_convert(image)

    if img.mode == 'RGB':
        black_pixel, white_pixel = BLACK_PIXEL_IN_JPG, WHITE_PIXEL_IN_JPG
    elif img.mode == 'RGBA':
        black_pixel, white_pixel = BLACK_PIXEL_IN_PNG, WHITE_PIXEL_IN_PNG
    number_of_whites, number_of_blacks = [0, 'White'], [0, 'Black']
    
    for pixel in img.getdata():
        if pixel == black_pixel:
            number_of_blacks[0] += 1
        if pixel == white_pixel:
            number_of_whites[0] += 1

    dominated_pixel = sorted([number_of_whites, number_of_blacks],
        reverse=True, key=lambda x: x[0])

    return (f'The "{dominated_pixel[0][1]}" pixels is dominated in image. '
            f'White pixels: {number_of_whites[0]}, Black pixels: {number_of_blacks[0]}')
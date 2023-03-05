from PIL import Image, ImageDraw


#Example 1 - Rotating an image.
with Image.open("Uc Logo.jfif") as picture:
    picture.rotate(45).show()

#Example 2 - Drawing Line on A Picture
with Image.open("Uc Logo.jfif") as picture2:
    draw = ImageDraw.Draw(picture2)
    draw.line((0,0) + picture2.size, fill=200)
    picture2.show()

#Example 3 - Counting Pixels in an image
def pixel_number(item):
    width, height = Image.open(item).size
    return height*width

print(pixel_number("Uc Logo.jfif"))
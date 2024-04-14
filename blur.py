from PIL import Image, ImageFilter

before = Image.open("python.bmp")
after = before.filter(ImageFilter.BoxBlur(10))
after.save("out.bmp")